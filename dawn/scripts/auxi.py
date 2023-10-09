import os.path # auxiliary:補助
import sys
import ctypes
import tkinter as tk 
import datetime 
import math 
import numpy
import ls
import sync
import ext
import room
import temp
import edit
import fx
import sct
import sti
import data
import call

class wid():                     
    def forget(root):
        children = root.winfo_children() 
        for child in children:
            child.destroy() 
            
    def reme(dd_,  sub ): # remeasurement:再計測
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        if dd_ == '再計測': 
            wid.forget(sub)
        elif dd_ != '再計測':   
            pass
        
    def SetCursorPos( x, y):
        ctypes.windll.user32.SetCursorPos(x, y)
    
    def frames(root,  cc_, dic):
        frame = tk.Frame(root) 
        frame0 = tk.Frame(frame)
        frame0.pack(side='right')  
        frame1 = tk.Frame(frame, bg=ls.cl()[1])
        frame2, frame3, lblframe, frame4, frame9 = (
            tk.Frame(frame1),
            tk.Frame(frame1),
            tk.LabelFrame(frame1, bg= temp.cnfg.bg(dic)),
            tk.Frame(frame1),
            tk.Frame(frame1)
            )  

        for f in [frame2, frame3, lblframe, frame4, frame9]:
            f.pack( fill=tk.BOTH if f == frame4 else None)

        frame1.pack(side='right')  
        frame5 = tk.Frame(frame)
        frame5.pack(side='right')
        frame.pack(side='right' if type(cc_) is int else 'left')
        south = tk.Frame(root)
        south.place( relx=0.002, rely=0.919)  

        return frame, frame0, frame2, frame3, lblframe, frame4, frame5, frame9, south    

class jump: 
    def __init__(self, a):
        self.a = a  
    def front(self,*args):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()
        lst = ls.customer()
        start = ls.start()
        my = lst[start].get(ls.kb())
        num = 0
        for i,item in enumerate(lst[start:]):
            if my != item[ls.kb()]:
                num = i
                break                      
        return num + start         
    
    def back(self,*args):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()
        lst = ls.customer()
        end = ls.start() if ls.start() != 0 else ls.end()
        dviz = [item[ls.kb()] for item in lst] #division
        edge= [i for i in range(end)][-1]
        my = lst[end].get(ls.kb())
        kb = lst[edge].get(ls.kb())
        tub= []
        start = 0
        ###     
        fx.a.u(end,my,kb)
        for i, item in enumerate( dviz[end::-1] ):
            tub.append(item)
            pail=len(tub)
            fx.a.u(i,item,len(tub[:-1]))
            if kb != lst[ end - pail][ ls.kb()]: 
                start = end - i
                break
            else:
                start = end - i
        return start
      
class adju: # adjustment:調整,加減,
    
    def renw( start, end): # 顧客情報の編集or追加、その顧客情報のみを表示させる為の加減、'幅'を取得させる。
        renew = ext.reader('renew.txt')
        (start, end, renew)
        if renew['number'] != False and renew['relord'] == True or renew['number'] == 0 and renew['relord'] == True: 
            start = renew['number'] 
            end = start + 1 
            if end >= len(ls.customer()): # 最後尾,list overへの対処,
                start = len(ls.customer())-1
                end = len(ls.customer())
        else:
            pass
        return start, end
            
class unit:
    def preview( frame, dic): # 試演、試写
        wid.forget(frame)
        up___ = tk.Frame(frame)
        up___.pack(side="top")
        und_r = tk.Frame(frame)   
        und_r.pack(side="top")
        now = datetime.datetime.now() # モジュール（module）
        fram_ = tk.Frame(up___)
        fram_.pack(side="right")  
        wr = ext.lmen( dic.get(ls.mm()[1]), 14, '') # メモ１   
        for item in wr:
            tk.Label(fram_,text=ext.tategaki( item), bg= sti.S.M_S( now, item), ).pack(side="right")
        wr = ext.lmen( dic.get(ls.mm()[2]), 14, '') # メモ2     
        for item in wr:
            tk.Label(fram_,text=ext.tategaki( item),bd=1,fg=ls.cl()[3],bg=ls.cl()[1]).pack(side="right")
        fram_ = tk.Frame(up___)
        fram_.pack(side="right",pady=1)    
        fra__ = tk.Frame(fram_) # 新聞名
        fra__.pack()
        for w in dic.keys():
            if w not in ls.kl():#ls.tm() + ls.m2() + ls.ic()
                tk.Label(fra__, width=2, text= ext.gomoji(w), fg=ext.font_clr(dic, w), bg= ext.clr(w)).pack(padx=0,pady=0,side="right")
        fra__ = tk.Frame(fram_) # 部数  
        fra__.pack() 
        for  w in dic.keys():  
            if w not in ls.kl():
                tk.Label(fra__, width=2, text = ext.ich(dic.get(w)) ,relief= "groove",fg=ls.cl()[0] ,bg=ls.cl()[1] ).pack(side="right")
        fra__ = tk.LabelFrame(fram_)
        fra__.pack()         
        tk.Label(fra__, name= '号数', text= dic.get(ls.gs()), bg=ls.cl()[1] , fg=room.wdgt.f_g(dic) ).pack(padx=0,pady=0)#, font=("",ls.ft()[2])  
        tk.Label(fra__, name= '一時止', text=temp.cnfg.tx(dic), font=("TkDefaultFont", ls.ft()[1]), fg= temp.cnfg.fg(dic), bg= temp.cnfg.bg(dic) ).pack( padx=0, pady=0, side="top") 
        tk.Label(fra__, name= '名称1', text= ext.tategaki(dic.get(ls.mi())[:5]), relief ="flat",bg=ls.cl()[1], height=5).pack(padx=0,pady=0,side="right")##名称1  
        fram_ = tk.Frame(up___)
        fram_.pack(side="right")       
        wr = ext.lmen( dic.get(ls.mm()[3]), 14, '') # メモ3    

        for item in wr:
            tk.Label(fram_,text=ext.tategaki( item ), bd=1,bg=ls.cl()[1]).pack(side="right")
        wr = ext.lmen( dic.get(ls.mm()[4]), 14, '') # メモ4   
    
        for item in wr:
            tk.Label(fram_,text=ext.tategaki( item ), bd=1,fg=ls.cl()[3],bg=ls.cl()[1]).pack(side="right")
        fram_ = tk.Frame(und_r)
        fram_.pack()  
        tk.Button(frame,font=("",7)).pack( fill=tk.X)
    
    def brnc( aa_:int, fra__, fra_e, boolean:bool, dic:dict, prfl:dict, sub): # conditional branch:条件分岐
        stt = sync.cnc.stte( boolean, "disabled") # stt
        for i, ke_ in enumerate( ls.wd()):
            if ke_ in [ ls.kb()]: # 区分
                fr___ = tk.Frame( fra__)    
                fr___.pack()            
                btn = tk.Button( fr___, state= stt, text=ke_, relief="raised")
                btn.bind('<1>', unit.stte( btn["state"], lambda event:edit.cmp( aa_,event.widget["text"],dic,prfl,sub).divi()) )
                btn.bind('<Return>', unit.stte( btn["state"], lambda event:edit.cmp( aa_,event.widget["text"],dic,prfl,sub).divi()) )
                lbl = tk.Label( fr___, width= 13, text= dic.get(ke_), anchor= 'w', relief="groove" )
                pack_pad.post(btn,lbl)
                
            elif ke_ in [ ls.mi()]: # 名称１
                fr___ = tk.Frame(fra__)    
                fr___.pack()            
                btn = tk.Button(fr___, state= stt, text=ke_, relief="raised")
                btn.bind('<1>', unit.stte( btn["state"], lambda event:edit.cmp(aa_,event.widget["text"],dic,prfl,sub).txst()))
                btn.bind('<Return>', unit.stte( btn["state"], lambda event:edit.cmp(aa_,event.widget["text"],dic,prfl,sub).txst()))
                lbl = tk.Label(fr___, width= 13, text= dic.get(ke_), anchor= 'w', relief= "groove")
                pack_pad.post(btn,lbl)
    
            elif ke_ in [ ls.kk()]: # 区間
                fr___ = tk.Frame(fra_e)
                fr___.pack()
                btn = tk.Button(fr___, text=ke_, state= stt, relief="raised" )
                btn.bind('<1>', unit.stte( btn["state"], lambda event:sct.cmp(aa_,event.widget["text"],dic,prfl,sub).post()) )
                btn.bind('<Return>', unit.stte( btn["state"], lambda event:sct.cmp(aa_,event.widget["text"],dic,prfl,sub).post()) )
                lbl = tk.Label(fr___, width= 13, text= dic.get(ke_),  anchor= 'w', relief="groove")
                pack_pad.post(btn,lbl)
                
            elif ke_ in [ ls.gs()]: # 号数
                fr___ = tk.Frame(fra_e)
                fr___.pack()
                btn = tk.Button(fr___, text=ke_, state= stt, relief="raised",fg=ls.cl()[3] if ke_== ls.mm()[2] or ke_== ls.mm()[4] else ls.cl()[0] )
                btn.bind('<1>', unit.stte( btn["state"], lambda event:room.cmp(aa_,event.widget["text"],dic,prfl,sub).post()) )
                btn.bind('<Return>', unit.stte( btn["state"], lambda event:room.cmp(aa_,event.widget["text"],dic,prfl,sub).post()) )
                lbl = tk.Label(fr___, width= 13, text= dic.get(ke_), fg=room.wdgt.f_g(dic), anchor= 'w', relief="groove")
                pack_pad.post(btn,lbl)
                           
            elif ke_ in [ ls.ic()]: # 一時止
                fr___ = tk.Frame(fra_e)
                fr___.pack()
                btn = tk.Button(fr___, state= stt, text= unit.tategaki( dic, ke_), relief= "raised")
                btn.bind("<1>", unit.stte(btn["state"], lambda event:temp.cmp(aa_,event.widget["text"],dic,prfl,sub).post()) )
                btn.bind("<Return>", unit.stte(btn["state"], lambda event:temp.cmp(aa_,event.widget["text"],dic,prfl,sub).post()) )
                lbl= tk.Label(fr___, width=11, relief="groove", text="{0}月{1}日{2}～\n{3}月{4}日{5}迄\n{6}".format(dic[ ls.tm()[0] ], dic[ ls.tm()[1] ], dic[ ls.tm()[2] ], dic[ ls.tm()[3] ], dic[ ls.tm()[4] ],dic[ ls.tm()[5] ],dic[ ls.tm()[6] ]) if dic[ ls.tm()[0] ] !="" else '',anchor = 'w' )
                pack_pad.post(btn,lbl)
                
            elif ke_ in ls.mm()[1:]: # メモ1~4
                fr___ = tk.Frame(fra_e)
                fr___.pack()
                btn = tk.Button(fr___,text=ke_, state= stt, relief="raised",fg=ls.cl()[3] if ke_== ls.mm()[2] or ke_== ls.mm()[4] else ls.cl()[0] )
                btn.bind('<1>', unit.stte( btn["state"], lambda event:edit.cmp(aa_,event.widget["text"],dic,prfl,sub).txst()))
                btn.bind('<Return>', unit.stte( btn["state"],lambda event:edit.cmp(aa_,event.widget["text"],dic,prfl,sub).txst()))
                lbl = tk.Label(fr___, width= 13, text= dic.get(ke_), anchor= 'w', relief="groove")
                pack_pad.post(btn,lbl)      

    # widgetの有効・無効
    def stte( ele:str, func): # State
        if ele == "normal":
            return func
        elif ele == "disabled":
            return None
    # 縦書き  
    def tategaki( dic:dict, ke_:str)->str:
        ele = dic[ix.vc()['取扱']] 
        if ele in ix.vc().values():
            return ext.tategaki(ke_)
        else:
            return ke_
        
        
class nine(): 
    # 数学者George Boole（ジョージ・ブール）:ブールが創り上げた代数学は真か偽かを”計算”できるというものであった。
    # 代数学:数の代わりに文字を用いて方程式の解法などを研究する学問
    def wdgt( frame, i, w:str, disp, issue, font:tuple, lst ):
        int9 = data.I.LD_I_S( lst, i, w) # int
        bools = data.B.LD_I_S( lst, i, w) # 最初かどうかブールで返す。
        ( int9, i, w, bools ,)
        
        b9 = tk.Label( frame, text = int9, font = font, relief= sti.S.T_L(( w , disp), issue), width = 2, fg= "SystemButtonFace" )
        # '区間'が　""のみ表示。　A,Bなど指定があると値を表示しない。
        if lst[i].get('区間') != '': 
            pass
            b9.config#( text= "" )
        # 一般紙は値を表示しない。
        if w in ls.nw()[0]:
            b9.config( fg= "SystemButtonFace" )
        elif w not in ls.nw()[0] :
            if bools and w in issue:#
                b9.config( fg= "black" )
        else:
            b9.config( fg= "SystemButtonFace" )
        b9.bind( '<Enter>' ,lambda event:event.widget.config( fg= "black" ))
        b9.bind( '<Leave>' ,lambda event:event.widget.config( fg= "SystemButtonFace" ))
        b9.pack( side= "right")
        
    def clr(txt):
        color = ''
        if txt in sti.L.issue( [] ):
            color = 'coral'
        else:
            color = None
        return color    
    
class fix: # fixed point :定点観測
    def u(*args):
        for i in args:
            pass
        ("")
        
class ix():  #index
    def vc(): #vocabulary:用語
        return {'取扱':'取扱','有':'有','無':'無'}   
     
class pack_pad: # 設定の追加
    def post(*args):  
        type(args)
        for a in args:
            a.pack_configure(side="left",ipadx=2,padx=2,ipady=1)
    def child():
        return #ipadx=1,padx=1,ipady=1,pady=1
        
array = []
class duble_click():
    # 1秒以内のダブルクリック禁止, 
    def boolean( flo:float): # ban:禁止, 停止, 禁制, 
        global array
        (flo) # 788.3213283
        if len(array) == 0:
            array.insert( 0, math.floor(flo))
        elif len(array) > 0 :
            array.insert( 0, math.floor(flo))
            ( array)
            arr = array[:2] # [788, 789]
            nparr = - numpy.array( arr) # numpy array, 負→正
            diff = numpy.diff( nparr) # [0]
            ( diff)
            lb = [ bool( i > 1 ) for i in diff ] # [True], list in boolean
            ( lb)
            if True in lb : #
                return True
        if len( array) == 1 :
            return True
        
    # 指定時間内のダブルクリック禁止,         
    def ban( flo:float): # ban:禁止, 停止, 禁制, 
        global array
        (flo) # 788.3213283
        if len(array) == 0:
            array.insert( 0, math.floor(flo))
        elif len(array) > 0 :
            array.insert( 0, math.floor(flo))
            (array)
            arr = array[:2] # [788, 789]
            nparr = - numpy.array(arr) # numpy, 負→正
            diff = numpy.diff(nparr) # [0]
            (diff)
            lb = [ bool( i <= 1 ) for i in diff ] # [True], list in boolean
            (lb)
            if True in lb: # 1秒以内のダブルクリック禁止
                duble_click.stop() # tk.Tk作成
                
    # 新規に作成されたtk.Tkが削除されるまでクリックを受け付けない。理由は不明。
    def stop(): # bindとは、イベントと関数の実行を紐付けるもの
        root = tk.Tk()  
        root.withdraw() # rootを表示しない。
        root.after( 1500, root.destroy)
        root.mainloop()
        
class button(tk.Button):
    def __init__( self, **d):
        self.text = d.get('text')      
        super().__init__( master= d.get('master'), width= d.get('width'), text= d.get('text'), font= d.get('font'), relief= d.get('relief'), fg= d.get('fg'), bg= d.get('bg') )
        self.config( command = lambda: call.cnsl( self.text, None,None,None, tk.Toplevel()).post())
        self.bind( '<1>', lambda event: ( self.text), '+')
        self.pack( side= d.get('side'), padx=d.get('padx'), pady=d.get('pady'), ipadx=d.get('ipadx'), ipady=d.get('ipady'), fill=d.get('fill'))
        
class label(tk.Label):
    def __init__( self, **d):
        self.text = d.get('text')      
        super().__init__( master= d.get('master'), width= d.get('width'), text= d.get('text'), font= d.get('font'), relief= d.get('relief'), fg= d.get('fg'), bg= d.get('bg') )
        self.bind("<1>", lambda event: ( type(self)))
        self.bind("<1>", lambda event: ( self.text), '+')
        self.pack( side= d.get('side'), padx=d.get('padx'), pady=d.get('pady'), ipadx=d.get('ipadx'), ipady=d.get('ipady'))
        
    def brand(self): # 新聞,銘柄
        self.configure( text= ext.gomoji(self.text))
        
    def quantity(self): # 新聞,部数,数量
        self.configure( text= ext.ich(self.text))
        
        
if __name__ == '__main__':   
    duble_click.ban(788.3213283)
    duble_click.boolean(788.3213283)