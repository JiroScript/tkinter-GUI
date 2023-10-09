import os.path
import tkinter as tk #Junction:分岐点
import ls
import sys
import ext
import infi
import edit

class cmp(ls.sp):#compilation:編集
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #     
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        dic= cc_    
        infi.wdgt.forget( ee_)
        sub = ee_ 
        sub.title(ls.gs())
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        fram_ = tk.LabelFrame(sub, text = '編集')
        tk.Label(fram_, text= bb_, width=6).pack(side="left") 
        validate = sub.register(ext.elim) # 空白の入力禁止。
        entry_val = tk.StringVar()
        etr= tk.Entry(fram_, validate="key", validatecommand = (validate, "%P"), textvariable= entry_val ,relief="groove",bd=4,width=30)
        etr.focus_set() 
        etr.insert( 'end', str(dic.get( bb_)) ) #if dic.get( bb_) != None else ""
        etr.pack(side= "left", fill= "x", padx=1, pady=1) 
        txt = tk.StringVar(sub)
        txt.set( cmp.blnk( str(dic.get( ls.ak()))))
        opt1=tk.OptionMenu(fram_,txt, *ls.tg()) 
        opt1.pack(side="left")                  
        button0= tk.Button( fram_, command=lambda :edit.cmp.jnc(aa_, bb_, {**cc_, bb_: etr.get(), ls.ak():txt.get()}, dd_, ee_) ,text='次へ',relief="groove",bd=4)
        button0.bind('<Return>',lambda event:edit.cmp.jnc(aa_, bb_, {**cc_, bb_: etr.get(), ls.ak():txt.get()}, dd_, ee_) )
        button0.pack()  
        fram_.pack()
        cancel = tk.Button(sub, text="キャンセル" , command= lambda: edit.cmp.jnc(aa_, bb_, cc_, dd_, ee_), relief="groove", bd=4, anchor="e")
        cancel.bind('<Return>', lambda event: edit.cmp.jnc(aa_, bb_, cc_, dd_, ee_) )
        cancel.pack()   
    
    def blnk( txt:str)-> str: # 空白を「黒字」に変換。
        if txt == "" :
            return ls.js()['黒字']
        else:
            return txt
            
class wdgt:#widget   
    def f_g( dic: dict)-> str: # foreground:前景 ,fg=ls.cl()[3] if lst[i].get( ls.ak()) ==ls.ak() else ls.cl()[0]
        
        if dic.get( ls.ak()) == ls.ak(): # 赤字
            return ls.cl()[3]
        else:
            return ls.cl()[0]
        
    
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    aa_ = 1
    dic = ls.customer()[aa_]
    prfl = { 'ファイル名':os.path.basename(__file__)}
    cmp(aa_, ls.gs(), dic, prfl, root).post()
    root.mainloop()
    """"""
    lst = ls.customer()
 
   