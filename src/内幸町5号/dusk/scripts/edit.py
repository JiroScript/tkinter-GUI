import os.path
import tkinter as tk #Junction:分岐点
import cfm
import optionmenu
import ls
import sys
import ext
            
class comp(ls.sp):#compilation:編集        
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #    
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        lst = ls.customer()
        sub = tk.Toplevel(ee_) 
        sub.title(lst[aa_][ls.wd()[1]])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
 
        fram_ = tk.LabelFrame(sub, text = '挿入')
        comp.front_insert(aa_,bb_,ee_,sub,fram_)
        fram_.pack(padx=1,pady=1)              
    
        fram_ = tk.LabelFrame(sub, text = '編集')
        comp.edit(aa_,bb_,ee_,sub,fram_,lst)
        fram_.pack(padx=1,pady=1)
   
        fram_ = tk.LabelFrame(sub, text = '末尾に挿入')
        comp.end_insert(aa_,bb_,ee_,sub,fram_)
        fram_.pack(padx=1,pady=1)
        agrm = { ky : lst[aa_][ky] for ky in lst[aa_]  if ky not in ls.kl()}   #契約:Agreement     

        if len(agrm) > 1 :            
            fram_ = tk.LabelFrame(sub, text = '削除')
            comp.delete(aa_,bb_,cc_,ee_,fram_,lst)
            fram_.pack( )         
        """fram_ = tk.LabelFrame(sub, text = '削除')
        comp.delete(aa_,bb_,cc_,ee_,fram_,lst)
        fram_.pack( ) """        
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack(pady=4)        
        sub.mainloop()
        
    def front_insert(aa_,bb_,ee_,sub,fram_):
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,txt0,txt1,sub).select())
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set("")
        opt1=tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[2],*ls.nw()[3],*ls.nw()[4],*ls.nw()[5],*ls.nw()[12],*ls.nw()[15])    
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")                
        val = tk.IntVar(sub)
        spn = tk.Spinbox(fram_, textvariable=val, width=3, from_=1, to=999, state = 'readonly' )        
        spn.pack(side="left", padx=2 ,pady=2)
        tk.Label(fram_,text='部').pack(side="left")
        tk.Button(fram_,text='次へ',width=4,command=lambda :cfm.confirm(aa_,bb_,txt1.get(),spn.get(),ee_).lead_insert() if txt1.get() != "" else tk.Label(sub,text='未入力の箇所があります' ).pack(),relief="groove",bd=4).pack(side="top",padx=1,pady=1)     

    def edit(aa_,bb_,ee_,sub,fram_, lst):
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,txt0,txt1,sub).select())
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set(bb_)
        opt1=tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[2],*ls.nw()[3],*ls.nw()[4],*ls.nw()[5],*ls.nw()[12],*ls.nw()[15])    
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")                
        val = tk.IntVar(sub)
        val.set(int(lst[aa_][bb_]))
        spn = tk.Spinbox(fram_, textvariable=val, width=3, from_=0, to=999, state = 'readonly')        
        spn.pack(side="left", padx=2 ,pady=2)      
        tk.Label(fram_,text='部').pack(side="left") 
        tk.Button(fram_,text='次へ',command=lambda :cfm.confirm(aa_,bb_,txt1.get(),spn.get(),ee_).compil(),relief="groove",bd=4).pack(side="top",padx=1,pady=1)

    def end_insert(aa_,bb_,ee_,sub,fram_):
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,txt0,txt1,sub).select())
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set("")
        opt1=tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[2],*ls.nw()[3],*ls.nw()[4],*ls.nw()[5],*ls.nw()[12],*ls.nw()[15])    
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")                
        val = tk.IntVar(sub)
        spn = tk.Spinbox(fram_, textvariable=val, width=3, from_=1, to=999, state = 'readonly' )        
        spn.pack(side="left", padx=2 ,pady=2)        
        tk.Label(fram_,text='部').pack(side="left") 
        tk.Button(fram_,text='次へ',width=4,command=lambda :cfm.confirm(aa_,bb_,txt1.get(),spn.get(),ee_).end_insert() if txt1.get() != "" else tk.Label(sub,text='未入力の箇所があります' ).pack(),relief="groove",bd=4).pack(side="top",padx=1,pady=1)     
                 
    def delete(aa_,bb_,cc_,ee_,fram_,lst):
        tk.Label(fram_,text=bb_).pack(side="left",padx=10)
        tk.Label(fram_,text=lst[aa_][bb_]).pack(side="left")
        tk.Label(fram_,text='部').pack(side="left") 
        tk.Button(fram_,command=lambda :cfm.confirm(aa_,bb_,cc_,0,ee_).delete(),text='次へ',relief="groove",bd=4).pack(side="right")       
         
    def p_st(self):           
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        sub = tk.Toplevel(ee_) 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
            
        fram_ = tk.LabelFrame(sub, text = '挿入する新しい契約')
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,txt0,txt1,sub).select())
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set('新聞名')
        opt1=tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[10],*ls.nw()[11])
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")         
        validate = sub.register(ext.validate_input)
        entry_val = tk.StringVar()
        enr1=tk.Entry(fram_ ,width=3,validate="key", validatecommand=(validate, "%P"), textvariable=entry_val)
        enr1.pack(side="left")         
        lbl1= tk.Label(fram_,text='部')
        lbl1.pack(side="left")
        
        lis_=list(range(1,999))
        spn1=tk.Spinbox(fram_, values=lis_,font=120,width=3,justify='center',state='readonly')
        spn1.pack_forget()#,state = 'readonly'
        button1= tk.Button(fram_,text='次へ',command=lambda :cfm.confirm(aa_,bb_,txt1.get(),enr1.get(),ee_).i_sert(),relief="groove",bd=4)
        button1.pack(side="top",padx=1,pady=1)     
        fram_.pack(padx=1,pady=1)

if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。      
    comp(0,"ア",0,0,tk.Tk() ).post() 
    