import os.path
import tkinter as tk
import delete
import ext
import ls
import sys
import divi
import temp
import edit
import name
import room
import memo
import infi
import sct

def bind_selected(aa_,listbox,sub):#**kwargs: 複数のキーワード引数を辞書として受け取る
    if len(listbox.curselection()) == 0:
        return
    index = listbox.curselection()[0]
    edit.comp(aa_,listbox.get(index)[0],0,0,sub).post()
    #print(listbox.get(index),listbox.get(index)[0],listbox.get(index)[1],listbox.curselection()[0])
            
class call(ls.sp): 
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #  
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.customer()#文字列をリストや辞書に変換  
        sub = ee_#tk.Toplevel() 
        sub.title(lst[aa_][ls.mi()])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        keylst = ls.wd()
        frame = tk.Frame(sub)
        fram = tk.Frame(frame)
        button = tk.Button(fram, text=ext.tategaki("顧客情報を挿入"),command = lambda:infi.infix(aa_,None,None,None,sub).post(),width=3,heigh=12)
        button.pack()
        fram.pack(side="right",padx=2)
        framm = tk.LabelFrame(frame,text="顧客情報",labelanchor="n")
        fram = tk.Frame(framm)
        for i,ke_ in enumerate(lst[aa_]):
            if ke_ in keylst:
                rightf = tk.Frame(fram)
                button0 = tk.Button(rightf, text=ke_, relief=tk.GROOVE, fg= call.clr( ke_))
                button0.bind("<1>",lambda event:sepa(aa_,event.widget["text"],None,None,sub).post())
                button0.bind('<Return>',lambda event:sepa(aa_,event.widget["text"],None,None,sub).post())
                button0.pack(side="left")
                label0 = tk.Label(rightf,width=14,text= lst[aa_][ke_],fg='red' if ls.ak() == lst[aa_][ls.ak()] and ls.gs() == ke_ else 'black',anchor = 'w' )
                label0.pack()
                rightf.pack(side="top")                
            elif ke_ in [ ls.ic()]:
                rightf = tk.Frame(fram)
                button0 = tk.Button(rightf,text=ke_,relief=tk.GROOVE)
                button0.bind("<1>",lambda event:temp.temp(aa_,event.widget["text"],None,None,sub).post())
                button0.bind('<Return>',lambda event:temp.temp(aa_,event.widget["text"],None,None,sub).post())
                button0.pack(side="left")
                label0= tk.Label(rightf, width=14, text="{0}月{1}日{2}～\n{3}月{4}日{5}迄\n{6}".format(lst[aa_][ ls.tm()[0] ],lst[aa_][ ls.tm()[1] ],lst[aa_][ ls.tm()[2] ],lst[aa_][ ls.tm()[3] ],lst[aa_][ ls.tm()[4] ],lst[aa_][ ls.tm()[5] ],lst[aa_][ ls.tm()[6] ]) if lst[aa_][ ls.tm()[0] ] !="" else '',anchor = 'w' )
                label0.pack()
                rightf.pack(side="top")
        fram.pack(side="right", padx=2)
        fram = tk.Frame(framm)
        fra = tk.Frame(framm)
        tk.Label(fra ,text='顧客番号:').pack( side="left")
        tk.Label(fra ,text=aa_).pack( side="left")
        fra.pack()
        scrollbar = tk.Scrollbar(fram)
        scrollbar.pack(side="right",fill="y")
        var = tk.StringVar()
        listbox = tk.Listbox(fram,listvariable=var,heigh=10)
        listbox.config(yscrollcommand=scrollbar.set)
        
        for i,ke_ in enumerate(lst[aa_]):
            if not ke_ in ls.kl():      
                listbox.insert(tk.END, [ ke_,lst[aa_][ke_ ] ])
        listbox.pack()
        listbox.bind("<<ListboxSelect>>", lambda event:bind_selected(aa_,listbox,sub) )
        scrollbar.config(command=listbox.yview)
        
        fram.pack(side="right",padx=2)
        fram = tk.Frame(framm)
        button = tk.Button(fram, text=ext.tategaki("削除"), command = lambda:delete.delet(aa_,0,0,0,sub).post(), width=3,heigh=10,)
        button.pack()
        fram.pack(side="right",padx=2)
        framm.pack(side="right",padx=2)
                
        lf__ = tk.LabelFrame(frame ,text=ls.pg()[0])
        vR = tk.IntVar() 
        vR.set(lst[aa_][ls.pg()[0]])
        rdo1 = tk.Radiobutton(lf__, value=ls.pg()[1],command=lambda:call.store(aa_ ,ls.pg()[0],rdo1['text']) ,variable=vR ,text= ls.pg()[1])        
        rdo1.pack(side='left')
        rdo2 = tk.Radiobutton(lf__, value=ls.pg()[2],command=lambda:call.store(aa_ ,ls.pg()[0],rdo2['text']) ,variable=vR ,text= ls.pg()[2])
        rdo2.pack(side='left')
        lf__.pack()
        
        fram = tk.Frame(frame)
        if aa_== len(lst)-1:
            button = tk.Button(fram,text=ext.tategaki("顧客情報を末尾に挿入"),command=lambda:infi.infix(aa_ +1,None,None,None,sub).post(),width=3,heigh=12 )
            button.pack(side="right",padx=2)
        cansell = tk.Button(fram, text=ext.tategaki("キャンセル") ,command = sub.destroy ,width=3,heigh=11)
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        fram.pack(side="right",padx=2)        
        frame.pack()
        sub.mainloop()      
        
    def clr(txt):         
        if ls.mm()[2] == txt or ls.mm()[4] == txt :
            return "red"
        else:
            return 'black'

    def trace_(*args):
        print("trace")
        pass
    def store(aa_,key,val):#         
        lst = ls.customer()
        lst[aa_][key] = val
        ext.store("customer.txt" ,lst)        
        
class sepa(ls.sp):#分岐点:separation 
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        if bb_ == ls.kb() :
            divi.cmp(aa_,bb_,0,0,ee_).post()
        elif bb_ == ls.kk(): #'
            sct.cmp(aa_,bb_,0,0,ee_).post()
        elif bb_ == ls.mi(): #'
            name.cmp(aa_,bb_,0,0,ee_).post()
        elif bb_ == ls.gs(): #'号数'
            room.cmp(aa_,bb_,0,0,ee_).post()
        elif bb_ == ls.mm()[1] or bb_ == ls.mm()[2] or bb_ == ls.mm()[3] or bb_ == ls.mm()[4]:  
            memo.cmp(aa_,bb_,0,0,ee_).post()
            
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    call(1,0,0,0,root).post()
    root.mainloop()