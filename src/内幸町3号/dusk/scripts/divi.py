import os.path #division:区分 
import tkinter as tk 
import ext
import optionmenu
import notice
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
        txt4 = tk.StringVar(sub)
        txt4.set('カテゴリ')
        opt4 = tk.OptionMenu(fram_, txt4,*ls.pa(),command=lambda event:optionmenu.option(opt4,opt5,txt4,txt5,sub).division())
        opt4.pack(side="left")
        txt5 = tk.StringVar(sub)
        txt5.set(lst[aa_][bb_])
        opt5=tk.OptionMenu(fram_,txt5,*ls.ea()[0],*ls.ea()[1])
        opt5.config(relief=tk.GROOVE)
        opt5.pack(side="left")         
        
        button= tk.Button(fram_,text='次へ',command=lambda :cfm(aa_,bb_,txt5.get(),0 ,ee_).compil() if txt5.get() != bb_ else no_entered(sub) ,relief="groove",bd=4)
        button.pack(side="top",padx=1,pady=1)        
        fram_.pack(padx=1,pady=1)        
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        
class cfm(ls.sp):#confirm:確認
    def compil(self):  #編集 
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #    
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        sub = tk.Toplevel( ee_ ) 
        sub.title( bb_ )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame = tk.LabelFrame(sub,text='下記の内容で保存しますか？')
        tk.Label(frame,text=bb_ + ':').pack(side="left", padx=4)
        tk.Label(frame,text=cc_).pack(side="left", padx=4)
        button0= tk.Button(frame,command=lambda :cfm(aa_,bb_,cc_,dd_,ee_).save(),text='実行',relief="groove",bd=4)
        button0.pack(side="left",anchor="e", padx=4) 
        frame.pack(padx=2,pady=1)
        frame_ = tk.Frame(sub)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()           
        frame_.pack()
        
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
        
        ins = notice.save(None,None,None,None,ee_)
        ins.complete() 
        
        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    cmp(1,"区分",0,0,root).post()
    root.mainloop()