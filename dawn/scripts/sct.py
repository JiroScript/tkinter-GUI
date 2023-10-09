# section:区間
import tkinter as tk 
import ls
import edit

def no_entered(sub):
    tk.Label(sub,text='未入力の箇所があります' ).pack()
class cmp(ls.sp):#compilation:編集     
    def post(self):     
        aa_, bb_, cc_, dd_, ee_ = self.a, self.b, self.c, self.d, self.e   
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        edit.wdgt.forget( ee_)
        sub = ee_          
        dic = cc_        
        sub.title( ls.kk() )
        ww, wh = sub.winfo_screenwidth(), sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        fram_ = tk.LabelFrame(sub, text = '')
        tk.Label(fram_,text="区間:").pack(side="left", padx=4, pady=2)
        txt = tk.StringVar()
        txt.set( dic[bb_])  
        spn = tk.Spinbox( fram_,  values= [ txt.get()] + [""] + ls.alphabet(),  width= 5, state= 'readonly' )  
        spn.pack(side="left", padx=4, pady=2)        
        button= tk.Button( fram_, text='次へ',command=lambda :edit.cmp.jnc( aa_, bb_, { **cc_,**{ bb_: spn.get()}}, dd_, ee_) if spn.get() != bb_ else no_entered(sub) ,relief="groove",bd=4)
        button.pack(side="top",padx=4, pady=2)        
        fram_.pack(padx=2,pady=2)        
        cansell = tk.Button(sub, text="キャンセル" , command = lambda: edit.cmp.jnc(aa_, bb_, cc_, dd_, ee_), relief="groove", bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:edit.cmp.jnc(aa_, bb_, cc_, dd_, ee_) )
        cansell.pack() 
        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    aa_ = 6
    cmp(aa_,ls.kk(),ls.customer()[aa_],None,root).post()
    root.mainloop()