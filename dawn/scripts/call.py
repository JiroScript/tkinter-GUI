import os.path 
import tkinter as tk
import notice
import ls
import sys
import ext
import infi
import delete
import sync 
import edit
import auxi
import log
import sl

class cnsl(ls.sp): 

    def post(self):       
        ls.sp(self.a,self.b,self.c,self.d,self.e).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        if type(self.c) != dict and self.c == None: # 新規
            dic = ls.customer()[ self.a]
        elif type(self.c) == dict : # 戻り
            dic = self.c
        cnsl.gdgt( self.a, dic, self.e)
    
    def gdgt(aa_:int, dic:dict, sub): 
        sub.title(dic.get('名称1'))        
        ww, wh = sub.winfo_screenwidth(), sub.winfo_screenheight()
        sub.geometry(ls.ge(ww,wh))
        sub.option_add( '*font', [ 'TkDefaultFont', ls.ft()[1] ] )
        wdgt.forget(sub)
        
        cvs = wdgt.scrollbar( sub, ww, wh, dic)        
        frame = tk.Frame(cvs) 
        frame.pack()
        r1__, r2__ = Frames.rows (frame)
        c1__, c2__, c3__, c4__, c5__ = Frames.row1 (r1__)
        
        prfl = { 'ファイル名':os.path.basename(__file__), 'クラス名': __class__.__name__, '関数名': sys._getframe().f_code.co_name}
        auxi.unit.preview( c5__, dic)
        if None :boolean = sync.cnc.smb()[0] # SMBConnection通信の確立, 
        boolean = True
        stt = sync.cnc.stte( boolean, "disabled")
        
        tk.Label(c2__, text= '顧客番号: ' + str(aa_)).pack( )
        
        listbox, scrollbar = wdgt.create_listbox(c2__, listvariable = tk.StringVar(value = sl.LL.D_S_L(dic, "not in", ls.kl())), heigh = 10, width = 11)
        listbox.bind("<<ListboxSelect>>", cnsl.stte(stt, lambda event: edit.cmp(aa_, listbox, dic, prfl, sub).bind_select()))

        # 名称1、号数、一時止め、メモ、など
        auxi.unit.brnc( aa_, c3__, c3__, boolean, dic, prfl, sub)
        tk.Button(c2__, text= '削除', command = cnsl.stte( stt, lambda: delete.cfm(aa_,None,None,None,sub).post()),fg='white', bg= 'red' , relief= 'raised', bd=5, state= stt, ).pack(pady=4 )
        tk.Button(c4__, text= ext.tategaki("顧客情報を挿入"), command = cnsl.stte( stt, lambda:infi.infix(aa_,None,None,({**prfl, ix.ky()['顧客情報を末尾に挿入']:0}),sub).post()), state= stt, width=3,heigh=12).pack()
        
        if aa_== len(ls.customer()) -1 or None == None : #
            tk.Button(c1__, state= stt, text= ext.tategaki( ix.ky()['顧客情報を末尾に挿入']), command= lambda:infi.infix( aa_ ,None,None,({**prfl, ix.ky()['顧客情報を末尾に挿入']:1}), sub).post(), width=3,heigh=12 ).pack(side="right",padx=2)
        
        c1__, c2__ = Frames.row2( r2__)
        btn = tk.Button( c2__, text="保存", state= stt, command = lambda:cnsl( aa_, None, dic, prfl, sub).save() if cnsl.req(dic) else cnsl.alr(c2__,dic), borderwidth=4, width=8)
        btn.bind('<Return>', lambda event:cnsl( aa_, None, dic, prfl, sub).save() if cnsl.req(dic) else cnsl.alr( c2__, dic) )
        btn.pack( side='left', padx= 4) #anchor="e"
        btn.focus_set() 
        wdgt.cancel(c2__, sub)
        
        # 改ページ
        vR = tk.IntVar()
        vR.set(dic.get('改ページ'))
        wdgt.new_page(c1__, vR, dic)

        sub.mainloop()

    
    def sngl(listbox, dic:dict, arg): # リストボックスの項目追加
        [ listbox.insert( tk.END, [ k, v ]) for k, v in dic.items() if k not in arg ]
              
    
    def stte( ele:str, func): # State
        if ele == "normal":
            return func
        elif ele == "disabled":
            return None
        
    def save(self):        
        lst = ls.customer()  
        dic = self.c
        lst[self.a] = dic        
        ext.storage('D:/', "customer.txt", lst)
        ext.store("customer.txt", lst)
        ext.renew(self.a, True, os.path.basename(__file__))
        log.dirc.actv('customer.txt') # ログを作成
        ins = notice.save(None, None, None, None, self.e)
        ins.complete()                           
        
    def req(dic): # required:必須
        if dic.get(ls.kb()) == "": # 区分
            return False # True#
        elif dic.get(ls.mi()) == "": # 名称1
            return False # True#
        else:
            return True
        
    def alr(frame,dic): # alert  
        if dic.get(ls.kb()) == "": # 区分
            return tk.Label(frame, text = ls.kb() + 'が未入力です', bg='yellow').pack()
        elif dic.get(ls.mi()) == "": # 名称1
            return tk.Label(frame, text = ls.mi() + 'が未入力です', bg='yellow').pack()
        else:
            return None
              
class ix(): 
    def ky()-> dict:
        return { '顧客情報を末尾に挿入':'顧客情報を末尾に挿入', 'ファイル名':os.path.basename(__file__)}
    def vc(): #vocabulary:用語
        return {'取扱':'取扱','有':'有','無':'無'}
    
class wdgt:       
    def create_listbox(container, **config):
        scrollbar = tk.Scrollbar(container)
        scrollbar.pack(side="right", fill="y")
        
        listbox = tk.Listbox(container, **config)
        listbox.config(yscrollcommand=scrollbar.set)
        listbox.pack(padx=2)
        
        scrollbar.config(command=listbox.yview)
        return listbox, scrollbar
    
    def new_page(c1__, vR, dic):
        rdo1 = tk.Radiobutton( c1__, value='有効', command=lambda:wdgt.incl('改ページ', dic, rdo1['text']), variable=vR, text= '有効')        
        rdo1.pack(side='left')
        rdo2 = tk.Radiobutton( c1__, value='無効', command=lambda:wdgt.incl('改ページ', dic, rdo2['text']), variable=vR, text= '無効')
        rdo2.pack(side='left')
        
    def incl(key:str, dic:dict, val:str)->dict: # include:含める,加える
        dic[key] = val
        return dic            
    
    def forget(root:tk.Tk):
        children = root.winfo_children() 
        for child in children:
            child.destroy() 
            
    def scrollbar(fram_:tk.Frame, ww:int, wh:int, dic:dict):
        canvas = tk.Canvas(fram_, width=ww, height=wh)
        ybar = tk.Scrollbar(fram_, orient="vertical")
        ybar.pack_forget()#(side="right", fill="y")
        ybar.config(command= canvas.yview)
        xbar = tk.Scrollbar(fram_, orient="horizontal")
        # 任意の条件でクロールバーが非表示になる
        xbar.pack_forget() if wdgt.lmen(dic) else xbar.pack(side="bottom", fill="x")        
        xbar.config(command=canvas.xview)
        canvas.config(yscrollcommand=ybar.set, xscrollcommand=xbar.set) # Canvasのサイズ変更をScrollbarに通知
        canvas.config(scrollregion=(0,0,ww,wh/2)) #スクロール範囲
        canvas.pack( side="top", fill=tk.BOTH, expand=True, padx=2, pady=2)
        cvs = tk.Frame(canvas)
        canvas.create_window((0,0), window= cvs, anchor= tk.NW, width=0, height=0)
        return cvs
    
    def lmen(dic:dict)->bool: # 閾値:limen
        lis = sl.L.L_S_L( dic.keys(),"not in", ls.kl()) # ['ア', 'マ', 'ヨ', 'サ',  'ト', ]
        arr = [ i for i in ls.mm()[1:] if len( dic.get(i)) >= 9 ] # ['メモ1']
        if len(lis) <= 2 and len(arr) == 0:
            return True
        else:
            return False
        
    def cancel(frame, sub):
        btn = tk.Button( frame, text = "✕", command = sub.destroy, font=('TkDefaultFont', 14)) 
        btn.bind('<Return>', lambda event:sub.destroy() )
        btn.pack(padx=4)
        
class Frames:
    @staticmethod # インスタンス化されていないクラスからも呼び出せるようにる。
    def rows(frame): 
        (__class__.__name__,sys._getframe().f_code.co_name)
        # ラベルフレームを作成してパック、タプルに格納
        frames = tuple(tk.LabelFrame(frame) for _ in range(5))
        
        # すべてのフレームをパック
        for frm in frames:
            frm.pack(padx=1, pady=1)
        
        # 最初の2つのフレームを返す
        return frames[:2]
    
    @staticmethod
    def row1(frame):
        # フレームの作成とパッキングを同時に行います
        frames = (
            tk.Frame(frame),
            tk.LabelFrame(frame, text='顧客情報', bd=5),
            tk.Frame(frame),
            tk.Frame(frame),
            tk.Frame(frame)
        )
        for frm in frames:
            frm.pack(side='left', fill=tk.X, padx=1, pady=1)
        
        # f2__の中に2つのフレームを作成します
        f1, f2 = (tk.Frame(frames[1]) for _ in range(2))
        f1.pack(side='left')
        f2.pack(side='left')
        
        return frames[0], f1, f2, frames[3], frames[4]
    
    @staticmethod
    def row2(frame):
        # ラベルフレームを作成し、タプルに格納
        frames = (
            tk.LabelFrame(frame, text=ls.pg()[0]),
            tk.LabelFrame(frame),
            tk.LabelFrame(frame),
            tk.LabelFrame(frame),
            tk.LabelFrame(frame)
        )
        
        # すべてのフレームをパック
        for frm in frames:
            frm.pack(side='left', fill=tk.X, padx=1, pady=1)
        
        # 最初の2つのフレームを返す
        return frames[:2]
    

if __name__ == '__main__':       
    root = tk.Tk() 
    
    cnsl( 0, None, None, None, root).post() 
    
    lst = ls.customer()
    ld = [{**{ k:v for k,v in dic.items() if k in [ '区分', '名称1', '号数']}
          ,**{ k:v for k,v in dic.items() if k not in ls.kl()}} for dic in lst ]
    ll = [ [ k + ' ' + v for k,v in dic.items() ] for dic in ld  ]
    (ll)
    l = '\n'.join([' '.join([i for i in l ]) for l in ll ])
    (l) 
    