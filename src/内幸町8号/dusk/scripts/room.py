import os.path
import tkinter as tk #Junction:分岐点
import notice
import ls
import sys
import ext
    
class cmp(ls.sp):#compilation:編集
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #     
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        sub = tk.Toplevel(ee_)  
        sub.title(lst[aa_][ls.wd()[0]])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        fram_ = tk.LabelFrame(sub, text = '編集')
        tk.Label(fram_, text= bb_, width=6).pack(side="left") 
        validate = sub.register(ext.elim)
        entry_val = tk.StringVar()
        enter0= tk.Entry(fram_, validate="key", validatecommand = (validate, "%P"), textvariable= entry_val ,relief="groove",bd=4,width=30)
        enter0.focus_set() 
        enter0.insert('end',lst[aa_][bb_])
        enter0.pack(side="left", fill="x", padx=1, pady=1) 
        txt1 = tk.StringVar(sub)
        txt1.set(lst[aa_][ ls.ak()])
        opt1=tk.OptionMenu(fram_,txt1, *ls.tg()) 
        opt1.pack(side="left")                  
        button0= tk.Button(fram_,command=lambda :cmp(aa_,bb_,enter0.get(),txt1.get(),ee_).cfm(),text='次へ',relief="groove",bd=4)
        button0.bind('<Return>',lambda event:cmp(aa_,bb_,enter0.get(),txt1.get(),ee_).cfm() )
        button0.pack()  
        fram_.pack()
        cansell = tk.Button(sub, text="キャンセル" ,command= sub.destroy, relief="groove", bd=4, anchor="e")
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()         
        
    def cfm(self):  #confirm:確認
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #   
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        
        sub = tk.Toplevel(ee_) 
        sub.title(lst[aa_][ls.wd()[0]])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame = tk.LabelFrame(sub,text='下記の内容で保存しますか？')
        tk.Label(frame,text=bb_).pack(side="left",padx=15)
        tk.Label(frame,text= cc_ ,fg=ls.cl()[3] if ls.tg()[0] in dd_ else ls.cl()[0]).pack(side="left",padx=15)
        button0= tk.Button(frame,command=lambda :cmp(aa_,bb_,cc_,dd_,ee_).save(),text='実行',relief="groove",bd=4)
        button0.focus_set()
        button0.bind('<Return>',lambda event:cmp(aa_,bb_,cc_,dd_,ee_).save() )
        button0.pack(side="left",anchor="e") 
        frame.pack(padx=2,pady=1)
        frame_ = tk.Frame(sub)   
        frame_.pack()
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")         
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
    def save(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e # 
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        
        lst[aa_][bb_] = cc_        
        ext.store("customer.txt" ,lst)
        
        lst[aa_][ls.ak()] = dd_        
        ext.store("customer.txt" ,lst)
        
        ins = notice.save(0,0,0,0,ee_)
        ins.complete()
    
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    cmp(1,ls.gs(),None,None,root).post()
    #table(0,0,0,0,root).post()
    root.mainloop()
    """"""
    lst = ls.customer()
 
   