import os.path #section:区間
import tkinter as tk 
import divi
import ls
import sys

def no_entered(sub):
    tk.Label(sub,text='未入力の箇所があります' ).pack()
class cmp(ls.sp):#compilation:編集       
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #    
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        sub = tk.Toplevel( ee_ ) 
        sub.title( bb_ )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        fram_ = tk.LabelFrame(sub, text = '編集')
        tk.Label(fram_,text="区間:").pack(side="left", padx=4, pady=2)
        txt = tk.StringVar()
        txt.set( lst[aa_][bb_])  
        spn = tk.Spinbox(fram_,  value= [ txt.get()] + [""] + ls.alphabet(),  width= 5, state= 'readonly' )  
        spn.pack(side="left", padx=4, pady=2)        
        button= tk.Button(fram_,text='次へ',command=lambda :divi.cfm(aa_,bb_,spn.get(),None ,ee_).compil() if spn.get() != bb_ else no_entered(sub) ,relief="groove",bd=4)
        button.pack(side="top",padx=4, pady=2)        
        fram_.pack(padx=2,pady=2)        
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        
        
        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    cmp(0,ls.kk(),0,0,root).post()
    root.mainloop()