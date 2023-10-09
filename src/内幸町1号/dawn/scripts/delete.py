import os.path
import tkinter as tk
import notice
import optionmenu
import ls
import sys
import ext
import divi
import name
import room
import memo

class read_news(ls.sp): #New customer
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.customer()
        sub = tk.Toplevel( ee_ )  
        sub.title( lst[aa_][ls.wd()[1]] )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        frame = tk.LabelFrame(sub,text='顧客情報を入力してください')              
        entries=[]
        
        fram_ = tk.Frame(frame)     
        txt4 = tk.StringVar(sub)
        txt4.set('カテゴリ')
        opt4 = tk.OptionMenu(fram_, txt4,*ls.pa(),command=lambda event:optionmenu.option(opt4,opt5,txt4,txt5,sub).division())
        opt4.pack(side="left")
        txt5 = tk.StringVar(sub)
        txt5.set(ls.wd()[0])
        opt5 = tk.OptionMenu(fram_,txt5,*ls.ea()[0],*ls.ea()[1])
        opt5.config(relief=tk.GROOVE)
        opt5.pack(side="left")         
        
        fram_.pack()  
        fram_ = tk.Frame(frame)
        tk.Label(fram_, text=ls.kl()[1]).pack(side="left")
        validate = sub.register(ext.elim)
        entry_val = tk.StringVar()
        enr5 = tk.Entry(fram_, validate="key", validatecommand = (validate, "%P"), textvariable= entry_val)
        enr5.pack()         
        fram_.pack()
        fram_ = tk.Frame(frame)
        tk.Label(fram_, text=ls.kl()[2]).pack_forget() #.pack(side="left")
        validate = sub.register(ext.elim)
        entry_val = tk.StringVar()
        enr6 = tk.Entry(fram_, validate="key", validatecommand = (validate, "%P"), textvariable= entry_val)
        enr6.pack_forget() 
        fram_.pack()  
        for i,ke_ in enumerate(ls.kl()[3:]):
            entries.append("")           
        frame.pack(padx=2,pady=1)
        
        fram_ = tk.LabelFrame(sub,text='新聞名と部数を入力してください') 
        
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command = lambda event : optionmenu.option(opt0,opt1,txt0,txt1,sub).select() )
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set('')
        opt1 = tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[10],*ls.nw()[11])    
        opt1.config(relief=tk.GROOVE)
        entries.append(txt1.get())          
        opt1.pack(side="left")                
        validate = sub.register(ext.validate_input)
        entry_val = tk.StringVar()       
        enr1 = tk.Entry(fram_ ,width=3,validate="key", validatecommand=(validate, "%P"), textvariable=entry_val)
        enr1.pack_forget#pack(side="left")   
        val = tk.IntVar(sub)        
        spn = tk.Spinbox(fram_, textvariable=val, width=3, from_=1, to=999, state = 'readonly' )        
        spn.pack(side="left", padx=2 ,pady=2)
        entries.append(spn.get())
 
        tk.Label(fram_,text='部').pack(side="left") 
        fram_.pack(padx=2,pady=1)
        btn = tk.Button(sub, command = lambda :read_news(aa_, [ txt5.get() ] + [ enr5.get() ] + [ enr6.get() ] + entries, txt1.get(), spn.get(), ee_).cfm() if txt5.get() != ls.wd()[0] and enr5.get() !="" and txt1.get() !="" and spn.get() !="" else tk.Label(fram_,text='未入力の箇所があります' ).pack(),text='次へ',relief="groove",bd=4)
        btn.pack() #anchor="e"
                
        fram_ = tk.Frame(sub)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()  
        fram_.pack() 
    def cfm(self):  #confirm:確認
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.customer()
        sub = tk.Toplevel(ee_) 
        sub.title( lst[aa_][ls.wd()[1]] )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        frame = tk.LabelFrame(sub,text='下記の契約を挿入しますか？')
        
        tk.Label(frame,text= ls.wd()[0] + '：' + bb_[0]).pack()
        tk.Label(frame,text= ls.wd()[1] + '：' + bb_[1]).pack()
        tk.Label(frame,text= '新聞名：' + cc_ + '  ' + dd_ + "部").pack()
        btn= tk.Button(frame,command=lambda :read_news(aa_,bb_,cc_,dd_,ee_).save(),text='実行',relief="groove",bd=4)
        btn.pack() #anchor="e"
        frame.pack(padx=2,pady=1)
        fram_ = tk.Frame(sub)        
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()          
        fram_.pack()
        
    def save(self):         
        aa_ = self.a #
        bb_ = self.b #entries
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst      = ls.customer()
        dct={}
        for i,item in enumerate( ls.kl() ):
            dct[ls.kl()[i]] = bb_[i]
        dct[cc_]=dd_
        lst.insert(aa_,dct)
        ext.store("customer.txt" ,lst)
        ins = notice.save("","","",0,ee_)
        ins.complete()   
        
class end_news(ls.sp): #New customer
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.customer()
        sub = tk.Toplevel( ee_ )  
        sub.title( lst[aa_][ls.wd()[1]] )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        frame = tk.LabelFrame(sub,text='顧客情報を入力してください')              
        entries=[]
        
        fram_ = tk.Frame(frame)     
        txt4 = tk.StringVar(sub)
        txt4.set('カテゴリ')
        opt4 = tk.OptionMenu(fram_, txt4,*ls.pa(),command = lambda event:optionmenu.option(opt4,opt5,txt4,txt5,sub).division())
        opt4.pack(side="left")
        txt5 = tk.StringVar(sub)
        txt5.set(ls.wd()[0])
        opt5=tk.OptionMenu(fram_,txt5,*ls.ea()[0],*ls.ea()[1])
        opt5.config(relief=tk.GROOVE)
        opt5.pack(side="left")         
        
        fram_.pack()  
        fram_ = tk.Frame(frame)
        
        tk.Label(fram_, text=ls.kl()[1]).pack(side="left")
        validate = sub.register(ext.elim)
        entry_val = tk.StringVar()
        enr5 =tk.Entry(fram_, validate="key", validatecommand = (validate, "%P"), textvariable= entry_val)
        enr5.pack()         
        fram_.pack()
        fram_ = tk.Frame(frame)
        tk.Label(fram_, text=ls.kl()[2]).pack_forget() #.pack(side="left")
        validate = sub.register(ext.elim)
        entry_val = tk.StringVar()
        enr6 =tk.Entry(fram_, validate="key", validatecommand = (validate, "%P"), textvariable= entry_val)
        enr6.pack_forget() 
        fram_.pack()  
        for i,ke_ in enumerate(ls.kl()[3:]):
            entries.append("")           
        frame.pack(padx=2,pady=1)
        fram_ = tk.LabelFrame(sub,text='新聞名と部数を入力してください') 
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command = lambda event : optionmenu.option(opt0,opt1,txt0,txt1,sub).select() )
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set('')
        opt1 = tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[10],*ls.nw()[11])    
        opt1.config(relief=tk.GROOVE)
        entries.append(txt1.get())          
        opt1.pack(side="left")   
        val = tk.IntVar(sub)        
        spn = tk.Spinbox(fram_, textvariable=val, width=3, from_=1, to=999, state = 'readonly' )        
        spn.pack(side="left", padx=2 ,pady=2)
        entries.append(spn.get())
        tk.Label(fram_,text='部').pack(side="left") 
        fram_.pack(padx=2,pady=1)
        btn= tk.Button(sub, command = lambda :end_news(aa_, [ txt5.get() ] + [ enr5.get() ] + [ enr6.get() ] + entries, txt1.get(), spn.get(), ee_).cfm() if txt5.get() != ls.wd()[0] and enr5.get() !="" and txt1.get() !="" and spn.get() !="" else tk.Label(fram_,text='未入力の箇所があります' ).pack(),text='次へ',relief="groove",bd=4)
        btn.pack() #anchor="e"
                
        fram_ = tk.Frame(sub)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        fram_.pack() 
        
    def cfm(self):  #confirm:確認
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.customer()
        sub = tk.Toplevel(ee_) 
        sub.title( lst[aa_][ls.wd()[1]] )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        frame = tk.LabelFrame(sub,text='下記の契約を挿入しますか？')
        tk.Label(frame,text= ls.wd()[0] + '：' + bb_[0]).pack()
        tk.Label(frame,text= ls.wd()[1] + '：' + bb_[1]).pack()
        tk.Label(frame,text= '新聞名：' + cc_ + '  ' + dd_ + "部").pack()
        btn= tk.Button(frame,command=lambda :end_news(aa_,bb_,cc_,dd_,ee_).save(),text='実行',relief="groove",bd=4)
        btn.pack() #anchor="e"
        frame.pack(padx=2,pady=1)
        fram_ = tk.Frame(sub)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack() 
        fram_.pack()
        
    def save(self):         
        aa_ = self.a #
        bb_ = self.b #entries
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        lst = ls.customer()
        dct = {}
        for i,item in enumerate( ls.kl() ):
            dct[ls.kl()[i]] = bb_[i]
        dct[cc_]=dd_
        lst.insert(aa_ +1 ,dct)
        ext.store("customer.txt" ,lst)
        ins = notice.save("","","",0,ee_)
        ins.complete()   

    
class delet(ls.sp): 
    def post(self):         
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.customer()
        sub = tk.Toplevel(ee_)  
        sub.title( lst[aa_][ls.wd()[1]] )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        frame = tk.LabelFrame(sub,text='下記の契約を削除しますか？')
        label0= tk.Label(frame,text=lst[aa_][ls.wd()[1]] +' '+ lst[aa_][ls.wd()[2]])
        label0.pack(side="left")
        btn= tk.Button(frame,command=lambda :delet(aa_,bb_,cc_,dd_,ee_).delet(),text='実行',relief="groove",bd=4)
        btn.pack(anchor="e") 
        frame.pack(padx=2,pady=1)
        fram_ = tk.Frame(sub)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack() 
        fram_.pack()
        
    def delet(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        lst      = ls.customer()
        
        lst.pop(aa_)        
        ext.store("customer.txt" ,lst)
        
        ins = notice.save(0,0,0,0,ee_)
        ins.complete()   

class sepa(ls.sp):#分岐点:separation 
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        if bb_ == ls.kl()[0] :
            divi.cmp(aa_,bb_,0,0,ee_).post()
        elif bb_ == ls.kl()[1] or bb_ == ls.kl()[2]: #'
            name.cmp(aa_,bb_,0,0,ee_).post()
        elif bb_ == ls.kl()[3]: #'号数'
            room.cmp(aa_,bb_,0,0,ee_).post()
        elif bb_ == ls.mm()[1] or bb_ == ls.mm()[2] or bb_ == ls.mm()[3] or bb_ == ls.mm()[4]:  
            memo.cmp(aa_,bb_,0,0,ee_).post()
        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    read_news(0,0,0,0,root).post()
    root.mainloop()
    