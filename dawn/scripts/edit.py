import os.path 
import tkinter as tk
import optionmenu
import ls
import sys
import ext
import infi
import call

class LF(tk.LabelFrame):
    def __init__( self, tpl):
        i, txt, dic, dct, sub = tpl
        self.i = i
        self.txt = txt
        self.dic = dic
        self.dct = dct
        self.sub = sub
        self.tpl = tpl
        self.sub.title( self.txt)
        super().__init__( master= self.sub, text= '編集') # 継承した親クラスのメソッドを使えるようになる、
        self.pack()
        self.bind("<Enter>", self.getEventEnter )
        self.bind("<Leave>", self.getEventLeave, '+')
        self.widgets()

    # オブジェクトを定義し,その後のオブジェクト()の記述で、__call__が呼び出される特殊なメソッド
    # __call__にはreturnを記載することが出来る    
    def __call__(self, event=None):
        return self.sVar2
        
    def btn_(self):
        self.label.configure( bg="yellow")
        self.label.configure( text= self.sVar2.get())
        
    def widgets(self):
        self.sVar1 = tk.StringVar()
        self.sVar1.set('カテゴリ')
        self.sVar2 = tk.StringVar()
        self.sVar2.set(self.dic.get(self.txt))
        self.opm1 = tk.OptionMenu(self, self.sVar1, *ls.pa() ,command=lambda event:self.menu_add() )
        self.opm1.pack(side='left')
        self.opm2 = tk.OptionMenu(self, self.sVar2, *ls.ea()[0], *ls.ea()[1])
        self.opm2.config(relief=tk.GROOVE)
        self.opm2.pack(side='left')    
        self.button = tk.Button( self, text='次へ', command=lambda :cmp.jnc( self.i, self.txt, {**self.dic, **{ self.txt: self.sVar2.get()}}, self.dct, self.sub), relief="groove",bd=4, )
        self.button.pack( side='left')
        
    def menu_add(self):
        d = self.d() # 
        l = d.get( self.sVar1.get()) # 
        self.opm2['menu'].delete( 0, tk.END)
        for s in l : # ['人事院', '弁護士会館', '富国生命', 
            self.opm2['menu'].add_command( label= s , command= tk._setit( self.sVar2, s, None))  # tk._setit、値iをウィジェット変数sVar2に格納。

    def d(self): # {'内幸町': ['人事院', '弁護士会館', '富国生命', 'プレスセンター', '厚生労働省', '日比谷国際ビル', 'パークフロント'], '永田町': ['国会議事堂', '総理大臣官邸', '国会図書館']}
        return { ls.pa()[0]:ls.ea()[0], ls.pa()[1]:ls.ea()[1]}
        
    def getEventEnter( self, event):
        self.configure( relief= 'ridge')
        
    def getEventLeave( self, event):
        self.configure( relief= 'groove')

class cmp(ls.sp):#compilation:編集
    def divi(self):         
        tpl = self.a, self.b, self.c, self.d, self.e 
        # 23 区分 {'区分': '弁護士会館', '区間': '', '名称1': '日本弁護士連合会', '号数': '日', '赤字': '赤字', '一時止': '', '始月': '', '始日': '', '始刊': '', '終月': '', '終日': '', '終刊': '', '取扱': '', '改ページ': '無効', '幅': 258, 'メモ1': '。弁護士会館。', 'メモ2': '梱包⇦', 'メモ3': '', 'メモ4': '', 'ア': '4', 'マ': '4', 'ヨ': '4', 'サ': '5', '産': '3', 'ト': '4', 'A': '1'} {'ファイル名': 'call.py', 'クラス名': 'cnsl', '関数名': 'gdgt'} .!toplevel        
        sub = self.e 
        wdgt.forget( sub)
        sub.geometry( ls.ge( sub.winfo_screenwidth(), sub.winfo_screenheight()) )    
        LF(tpl)
        cmp.cancel( *tpl)
        
    def cancel(*tpl):
        sub = tpl[-1]
        btn = tk.Button( sub, text= 'キャンセル', command = lambda: cmp.jnc(*tpl),) 
        btn.bind( '<Return>', lambda: cmp.jnc(*tpl))
        btn.pack( padx=4, pady=4)
        
    def txst(self):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()         
        aa_, bb_, cc_, dd_, ee_ = self.a, self.b, self.c, self.d, self.e 
        tpl = self.a, self.b, self.c, self.d, self.e     
        dic, sub =  cc_, ee_
        wdgt.forget( ee_)
        ww, wh = sub.winfo_screenwidth(), sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh))
        fram_ = tk.Frame( sub)
        tk.Label( fram_,text=bb_,width=6).pack(side="left")  
        validate = sub.register( ext.elim)
        entry_val = tk.StringVar()
        etr= tk.Entry(fram_, validate="key", validatecommand = (validate, "%P"), textvariable= entry_val ,relief="groove",bd=4,width=60)
        etr.focus_set() 
        etr.insert('end',str(dic.get(bb_)))
        etr.pack(side="left",fill="x",padx=1,pady=1)                 
        btn= tk.Button(fram_, text='次へ', command= lambda :cmp.jnc(aa_, bb_, { **cc_, **{ bb_: etr.get()}}, dd_, ee_), relief="groove",bd=4)
        btn.bind('<Return>',lambda event:cmp.jnc(aa_, bb_, { **cc_, **{ bb_: etr.get()}}, dd_, ee_) )
        btn.pack()  
        fram_.pack()
        cmp.cancel( *tpl)
        
    def bind_select(self): # confirm:確認
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        aa_, bb_, cc_, dd_, ee_ = self.a, self.b, self.c, self.d, self.e  
        listbox = self.b #    
        dic, sub =  cc_, ee_
        tpl = self.a, self.b, self.c, self.d, self.e   
        i, = listbox.curselection()
        (i, list(listbox.curselection()))
        bb_, txt = listbox.get( i )
        agrm = { ky : dic.get(ky) for ky in dic  if ky not in ls.kl()}   #契約:Agreement     
        wdgt.forget( ee_)   
        sub.title(None)
        ww, wh = sub.winfo_screenwidth(), sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        
        fram_ = tk.LabelFrame(sub, text = '挿入')
        cmp.front_insert(aa_,bb_,cc_,dd_,ee_,sub,fram_,dic)
        fram_.pack(padx=1,pady=1) 
        fram_ = tk.LabelFrame(sub, text = '編集')
        cmp.edit(aa_,bb_,cc_,dd_,ee_,sub,fram_,dic)
        fram_.pack(padx=1,pady=1)
   
        fram_ = tk.LabelFrame(sub, text = '末尾に挿入')
        cmp.end_insert(aa_,bb_,cc_,dd_,ee_,sub,fram_,dic)
        fram_.pack(padx=1,pady=1)
        if len(agrm) > 1 :            
            fram_ = tk.LabelFrame(sub, text = '削除')
            cmp.delete(aa_,bb_,cc_,dd_,ee_,sub,fram_,dic)
            fram_.pack( )           
        cmp.cancel( *tpl)
      
            
    # 辞書を結合、順序を揃える
    def cmbi(fnc:str, bb_:str, txt:str, cc_:dict, spn:str)->dict: # combining:結合
        exi = bb_ # 既存:existing
        dic = cc_
        k, v = txt, spn
        inx = list( dic).index( exi)
        rvers = list( dic)
        rvers.reverse() # 元のリスト自体が書き換えられる破壊的処理。返り値はNoneなので注意。
        front = { ky: dic.get(ky) for ky in list( dic)[:inx]}       
        backs = { ky: dic.get(ky) for ky in reversed(rvers[:rvers.index(exi)])}
        if fnc == "front_insert":
            dic = {**front,**{ k : v },**{exi:dic.get(exi)},**backs,**{ k : v }}
        elif fnc == "edit":
            dic = {**front,**{ k : v },**backs}
        elif fnc == "end_insert":
            dic = {**front,**{exi:dic.get(exi)},**{ k : v },**backs,**{ k : v }}
        elif fnc == "delete":
            dic = {**front,**backs}        
        return dic        

    def front_insert(aa_,bb_,cc_,dd_,ee_,sub,fram_,dic):
        fnc = sys._getframe().f_code.co_name
        sVar0 = tk.StringVar(sub)
        sVar0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, sVar0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,sVar0,sVar1,sub).select())
        opt0.pack(side="left")
        sVar1 = tk.StringVar(sub)
        sVar1.set("")
        opt1=tk.OptionMenu(fram_,sVar1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[10],*ls.nw()[17][12:])    
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")                
        iVar = tk.IntVar(sub)
        spn = tk.Spinbox(fram_, textvariable=iVar, width=3, from_=1, to=999, state = 'readonly' )        
        spn.pack(side="left", padx=2 ,pady=2)
        tk.Label(fram_,text='部').pack(side="left")
        tk.Button(fram_,text='次へ',width=4,command=lambda :cmp.jnc(aa_,bb_,cmp.cmbi(fnc, bb_, sVar1.get(), cc_, spn.get()),dd_,ee_) if sVar1.get() != "" else tk.Label(sub,text='未入力の箇所があります' ).pack(),relief="groove",bd=4).pack(side="top",padx=1,pady=1)     

    def edit(aa_,bb_,cc_,dd_,ee_,sub,fram_,dic):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        print(aa_,bb_,cc_,dd_,ee_,sub,fram_,dic)
        fnc = sys._getframe().f_code.co_name
        sVar0 = tk.StringVar(sub)
        sVar0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, sVar0, *ls.mn(), command=lambda event:optionmenu.option(opt0,opt1,sVar0,sVar1,sub).select())
        opt0.pack(side="left")
        sVar1 = tk.StringVar(sub)
        sVar1.set(bb_)
        opt1=tk.OptionMenu(fram_,sVar1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[10],*ls.nw()[17][12:])    
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")                
        iVar = tk.IntVar(sub)
        iVar.set(int(dic.get(bb_)))
        spn = tk.Spinbox(fram_, textvariable=iVar, width=3, from_=0, to=999, state = 'readonly')        
        spn.pack(side="left", padx=2 ,pady=2)      
        tk.Label(fram_,text='部').pack(side="left") 
        tk.Button(fram_,text='次へ',command=lambda :cmp.jnc(aa_,bb_,cmp.cmbi(fnc, bb_, sVar1.get(), cc_, spn.get()),dd_,ee_),relief="groove",bd=4).pack(side="top",padx=1,pady=1)

    def end_insert(aa_,bb_,cc_,dd_,ee_,sub,fram_,dic):
        fnc = sys._getframe().f_code.co_name
        sVar0 = tk.StringVar(sub)
        sVar0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, sVar0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,sVar0,sVar1,sub).select())
        opt0.pack(side="left")
        sVar1 = tk.StringVar(sub)
        sVar1.set("")
        opt1=tk.OptionMenu(fram_,sVar1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[10],*ls.nw()[17][12:])    
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")                
        iVar = tk.IntVar(sub)
        spn = tk.Spinbox(fram_, textvariable=iVar, width=3, from_=1, to=999, state = 'readonly' )        
        spn.pack(side="left", padx=2 ,pady=2)        
        tk.Label(fram_,text='部').pack(side="left") 
        tk.Button(fram_,text='次へ',width=4,command=lambda :cmp.jnc(aa_,bb_,cmp.cmbi(fnc, bb_, sVar1.get(), cc_, spn.get()), dd_,ee_) if sVar1.get() != "" else tk.Label(sub,text='未入力の箇所があります' ).pack(),relief="groove",bd=4).pack(side="top",padx=1,pady=1)     

    def delete(aa_,bb_,cc_,dd_,ee_,sub,frame,dic):
        fnc = sys._getframe().f_code.co_name
        tk.Label( frame, text=bb_).pack(side="left",padx=10)
        tk.Label( frame, text=dic.get(bb_)).pack(side="left")
        tk.Label( frame, text='部').pack(side="left") 
        tk.Button( frame, command=lambda: cmp.jnc(aa_,bb_,cmp.cmbi(fnc, bb_, None, cc_, None),dd_,ee_), text='次へ',relief="groove",bd=4).pack(side="right")       
        
    def jnc(*tpl): # junction: 分別点, 可変長引数
        i, txt, dic, dct, sub = tpl
        
        if dct == None :
            sub.destroy()
            
        elif infi.ix.ky()['ファイル名'] in dct.values(): # 'ファイル名':os.path.basename(__file__)
            infi.infix(i, txt, dic, dct, sub).post() 
            
        elif call.ix.ky()['ファイル名'] in dct.values():
            call.cnsl(i, txt, dic, dct, sub).post() 
            
        else:
            sub.destroy()

class info:           
    # 顧客情報dicに不足してるkeyを検出・追加。      
    def corr(dic)->dict: # correction:補正
        d = {}
        differenc_ = set(ls.kl()) - set(dic.keys()) # 差集合
        for k in ls.kl():
            if k in dic.keys():
                d = {**d , **{ k :dic[ k ]}}
            elif k not in dic.keys():
                d ={**d , **{ k :""}}
        for k in dic.keys():
            if k not in ls.kl():
                d = {**d , **{ k :dic[ k ]}}
        return d 
    
class wdgt: # widget                       
    def forget(root):
        children = root.winfo_children() 
        for child in children:
            child.destroy() 
            
if __name__ == '__main__':   # これがないと外部からインポートされた際に処理が実行されてしまう。              
   
    prfl = { 'ファイル名':os.path.basename(__file__)}
    lst = ls.customer()
    dic =lst[81]
    info.corr(dic)
    
              
    root = tk.Tk() 
    aa_ = 6
    cmp(aa_,ls.kb(),ls.customer()[aa_],None,root).divi()
    root.mainloop()