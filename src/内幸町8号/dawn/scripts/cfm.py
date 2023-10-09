import os.path
import tkinter as tk #Branch:分岐
import notice,sys,ls

class confirm(ls.sp):#確認
    def lead_insert(self):# lead:先頭         
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #  
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()        
        lst = ls.customer()       
        sub = tk.Toplevel(ee_) 
        sub.title(lst[aa_][ls.wd()[0]])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        frame = tk.LabelFrame(sub,text='下記の契約を挿入しますか？')
        tk.Label(frame,text=cc_).pack(side="left",padx=10)
        tk.Label(frame,text=dd_).pack(side="left")
        tk.Label(frame,text='部').pack(side="left") 
        tk.Button(frame,command=lambda :notice.save(aa_,bb_,cc_,dd_,ee_).lead_insert(),text='実行',relief="groove",bd=4).pack(side="left",anchor="e",padx=10) 
        frame.pack(padx=2,pady=1)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        
    def compil(self):  #編集 
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #    
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst =ls.customer()
        
        sub = tk.Toplevel(ee_) 
        sub.title(lst[aa_][ls.wd()[0]])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame = tk.LabelFrame(sub,text='下記の内容で保存しますか？')
        tk.Label(frame,text=cc_).pack(side="left",padx=10)
        tk.Label(frame,text=dd_).pack(side="left")
        tk.Label(frame,text='部').pack(side="left")         
        tk.Button(frame,command=lambda :notice.save(aa_,bb_,cc_,dd_,ee_).compil(),text='実行',relief="groove",bd=4).pack(side="left",anchor="e",padx=10) 
        frame.pack(padx=2,pady=1)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()

    def end_insert(self): #end:末尾
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
        frame = tk.LabelFrame(sub,text='下記の契約を挿入しますか？')
        tk.Label(frame,text=cc_).pack(side="left",padx=10)
        tk.Label(frame,text=dd_).pack(side="left")
        tk.Label(frame,text='部').pack(side="left")         
        tk.Button(frame,command=lambda :notice.save(aa_,bb_,cc_,dd_,ee_).end_insert(),text='実行',relief="groove",bd=4).pack(side="left",anchor="e") 
        frame.pack(padx=2,pady=1)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        
    def delete(self):         
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
        frame = tk.LabelFrame(sub,text='下記の契約を削除しますか？')
        tk.Label(frame,text=bb_).pack(side="left",padx=10)
        tk.Label(frame,text=lst[aa_][bb_]).pack(side="left")
        tk.Label(frame,text='部').pack(side="left") 
        tk.Button(frame,command=lambda :notice.save(aa_,bb_,cc_,dd_,ee_).delete(),text='実行',relief="groove").pack(side="left",padx=10) 
        frame.pack(padx=2,pady=1)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
