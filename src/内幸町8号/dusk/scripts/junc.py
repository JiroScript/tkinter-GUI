import os.path
import tkinter as tk #Junction:分岐点
import branch,optionmenu,ls,re,sys
            
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
        sub.title(lst[aa_][ls.wd()[0]])
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
 
        fram_ = tk.LabelFrame(sub, text = '挿入')
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,txt0,txt1,sub).select())
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set("")
        opt1=tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[10],*ls.nw()[11])    
        opt1.config(relief=tk.GROOVE,width=5)
        opt1.pack(side="left")                
        validate = sub.register(validate_input)
        entry_val = tk.StringVar()       
        enr1=tk.Entry(fram_ ,width=3,validate="key", validatecommand=(validate, "%P"), textvariable=entry_val)
        enr1.pack(side="left")         
        tk.Label(fram_,text='部').pack(side="left") 
        
        button1= tk.Button(fram_,text='次へ',width=4,command=lambda :branch.confirm(aa_,bb_,txt1.get(),enr1.get(),ee_).inser_() if txt1.get() != "" and enr1.get() != "" else tk.Label(sub,text='未入力の箇所があります' ).pack(),relief="groove",bd=4)
        button1.pack(side="top",fill="x",padx=1,pady=1)     
        fram_.pack(fill="x",padx=1,pady=1)
              
    
        fram_ = tk.LabelFrame(sub, text = '編集')
        txt4 = tk.StringVar(sub)
        txt4.set('カテゴリ')
        opt4 = tk.OptionMenu(fram_, txt4,*ls.mn(),command=lambda event:optionmenu.option(opt4,opt5,txt4,txt5,sub).select())
        opt4.pack(side="left")
        txt5 = tk.StringVar(sub)
        txt5.set(bb_)
        opt5=tk.OptionMenu(fram_,txt5,*ls.nw()[0],*ls.nw()[1],*ls.nw()[10],*ls.nw()[11])
        opt5.config(relief=tk.GROOVE,width=5)
        opt5.pack(side="left")         
        validate = sub.register(validate_input)
        entry_val = tk.StringVar()       
        enr4=tk.Entry(fram_ ,width=3,validate="key", validatecommand=(validate, "%P"), textvariable=entry_val)
        enr4.insert(0,int(lst[aa_][bb_])) 
        enr4.pack(side="left")         
        tk.Label(fram_,text='部').pack(side="left")        
        
        button2= tk.Button(fram_,text='次へ',command=lambda :branch.confirm(aa_,bb_,txt5.get(),enr4.get(),ee_).compil(),relief="groove",bd=4)
        button2.pack(side="top",fill="x",padx=1,pady=1)
        fram_.pack(fill="x",padx=1,pady=1)
             
   
        fram_ = tk.LabelFrame(sub, text = '削除')
        tk.Label(fram_,text=bb_,width=6).pack(side="left")
        tk.Label(fram_,text=lst[aa_][bb_],width=6).pack(side="left")
        tk.Label(fram_,text='部').pack(side="left") 
        button0= tk.Button(fram_,command=lambda :branch.confirm(aa_,bb_,cc_,0,ee_).delet_(),text='次へ',relief="groove",bd=4)
        button0.pack(side="right")        
        fram_.pack( )         
        button3= tk.Button(sub,command=sub.destroy,text='キャンセル',relief="groove",bd=4)
        button3.pack(side="bottom",fill="x",padx=1,pady=1)
        
    def p_st(self):           
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        sub = tk.Toplevel(ee_) 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
            
        fram_ = tk.LabelFrame(sub, text = '挿入する新しい契約')
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,txt0,txt1,sub).select())
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set('新聞名')
        opt1=tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[10],*ls.nw()[11])
        opt1.config(relief=tk.GROOVE,width=5)
        opt1.pack(side="left")         
        validate = sub.register(validate_input)
        entry_val = tk.StringVar()
        enr1=tk.Entry(fram_ ,width=3,validate="key", validatecommand=(validate, "%P"), textvariable=entry_val)
        enr1.pack(side="left")         
        lbl1= tk.Label(fram_,text='部')
        lbl1.pack(side="left")
        
        lis_=list(range(1,999))
        spn1=tk.Spinbox(fram_, values=lis_,font=120,width=3,justify='center',state='readonly')
        spn1.pack_forget()#,state = 'readonly'
        button1= tk.Button(fram_,text='次へ',command=lambda :branch.confirm(aa_,bb_,txt1.get(),enr1.get(),ee_).i_sert(),relief="groove",bd=4)
        button1.pack(side="top",fill="x",padx=1,pady=1)     
        fram_.pack(fill="x",padx=1,pady=1)
        
def returnlst():
    menu = ['一般日刊紙','産業･金融・流通',"株式・証券・税務","交通・運輸・鉄鋼","建設・住宅・電気","石油・繊維・農林","スポーツ紙","海外紙・国内英字紙","青少年向き・レジャー・趣味","一般夕刊紙","各種の縮刷版・その他"]      
    techniQ = ["工業","日産","農業","自動車","産業","流通","日本証券","みなと","食糧","電波","でんき","海事","住宅","金融","繊研","建通","教育","交通","株式"]
    return  menu,techniQ

def validate_input(val):
    fmt = '^[0-9]{,1}[0-9]{,1}?$'#'^[+-]?[0-9]{1,2}(?:\.[0-9]{,2})?$'
    if val=='' or re.match(fmt, val):
        return True
    return False 

