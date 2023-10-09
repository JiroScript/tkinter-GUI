import os.path #infix:挿入
import tkinter as tk
from collections import defaultdict
import ls
import sys
import call
import edit
import auxi
import ext
import notice

class infix(ls.sp): #infix:挿入
    def __del__(self):
        pass
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp( aa_, bb_, cc_, dd_, ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        prfl = {**dd_, 'ファイル名':os.path.basename(__file__), 'クラス名': __class__.__name__, '関数名': sys._getframe().f_code.co_name}###profile:、何らかの対象に関する属性や設定などの情報を列挙した、ひとまとまりのデータの集合のことを指す
        
        sub = ee_ ##tk.Toplevel()
        sub.title(None)
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh))
        
        if ix.ky()['ステータス'] not in prfl.keys():###initial state:初期状態,,,type(cc_) != list and 
            wdgt.forget(ee_)
            dic = { ky : "" for ky in ls.kl() }      
            dic[ls.hb()] = sub.winfo_width() # 幅  
            dic[ls.kp()] = '無効' # 改ページ
            dic[ls.nw()[0][3]] = '1' # 'サ': '1'
            prfl['ステータス']='初期値'
        elif ix.ky()['ステータス'] in prfl.keys() : #  type(cc_) == list and 
            wdgt.forget(ee_)
            dic= cc_
        
        { ky : dic.get(ky) for ky in dic  if ky not in ls.kl()}
        cvs = call.wdgt.scrollbar( sub, ww, wh, dic)        
        frame = tk.Frame(cvs) 
        rig_t = tk.LabelFrame(frame, text="プレビュー")  
        auxi.unit.preview(rig_t, dic)
        rig_t.pack(side="right",padx=10,pady=1)   

        left = tk.Frame(frame) 
        f_ame = tk.LabelFrame(left, text="挿入する顧客情報を入力して下さい", labelanchor="n")
        fram_ = tk.Frame(f_ame)                
        fra__ = tk.LabelFrame(fram_, text="必須", fg="gray", borderwidth=4)
        fra__.pack() 
        fra_e = tk.LabelFrame(fram_)
        fra_e.pack() 
        boolean = True
        auxi.unit.brnc(aa_,fra__,fra_e,boolean,dic,prfl,sub)
        
        fram_.pack(side="right")
        fram_ = tk.LabelFrame(f_ame,text="必須",fg="gray", borderwidth=4)
        scrollbar = tk.Scrollbar(fram_)
        scrollbar.pack(side="right",fill="y")
        var = tk.StringVar()
        listbox = tk.Listbox(fram_,listvariable=var,heigh=10,width=11,font=9)
        listbox.config(yscrollcommand=scrollbar.set)
        for i, ke_ in enumerate(dic):
            if not ke_ in ls.kl():      
                listbox.insert(tk.END, [ ke_,dic.get(ke_) ])
        listbox.pack()
        listbox.bind("<<ListboxSelect>>", lambda event:edit.cmp(aa_, listbox, dic, prfl, sub).bind_select() )
        scrollbar.config( command=listbox.yview)        
        fram_.pack(side="right")
        f_ame.pack()        
        left.pack()
        
        fram_ = tk.Frame(frame)
        tk.Button(fram_, text="挿入", command = lambda:infix( aa_, None, dic, prfl, ee_).save() if infix.req(dic) else infix.alr(fram_,dic), borderwidth=4).pack( side="left", padx=4, pady=4) #anchor="e"

        cancel = tk.Button(fram_, text="戻る" , command =lambda: call.cnsl(aa_, None, None, None, sub).post()  )
        cancel.focus_set() 
        cancel.bind('<Return>', lambda event: edit.cmp.jnc(aa_, bb_, cc_, prfl, ee_) )
        cancel.pack(side="left", padx=4, pady=4)
        fram_.pack(side="bottom", padx=4)        
        frame.pack()  
        sub.mainloop()    
                     
        
    def req(dic): # required:必須
        if dic.get(ls.kb()) == "": # 区分
            return False#True#
        elif dic.get(ls.mi()) == "": # 名称1
            return False#True#
        else:
            return True
        
    def alr(frame,dic): # alert  
        if dic.get(ls.kb()) == "": # 区分
            return tk.Label(frame, text = ls.kb() + 'が未入力です', bg='yellow').pack()
        elif dic.get(ls.mi()) == "": # 名称1
            return tk.Label(frame, text = ls.mi() + 'が未入力です', bg='yellow').pack()
        else:
            return None
    def save(self):         
        aa_ = self.a #
        bb_ = self.b #
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.customer()  
        dic = cc_
        prfl = dd_
        aa_ = aa_+ prfl[ ix.ky()['顧客情報を末尾に挿入']]
        lst.insert( aa_, dic)
        ext.store( "customer.txt", lst)
        ext.renew( aa_, True, os.path.basename(__file__))
        ins = notice.save(None,None,None,None,ee_)
        ins.complete()                
        
class test:
    def defaultdict():
        dct = defaultdict( int)
        dct[0] += 88
        dct[0] += 12
        dct
        
class ix():###index
    def ky():###
        return { '顧客情報を末尾に挿入':'顧客情報を末尾に挿入', 'ファイル名':os.path.basename(__file__), 'ステータス':'ステータス'}
        
class wdgt:#widget                       
    def forget(root):
        children = root.winfo_children() 
        for child in children:
            child.destroy() 
        
if __name__ == '__main__': ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    prfl = { ix.ky()['顧客情報を末尾に挿入']:0, 'ファイル名':os.path.basename(__file__)}
    infix( 0,None,None,prfl,root).post()
    test.defaultdict()
