import os.path
import tkinter as tk
import notice
import ls
import sys
import ext
import auxi
import log

class cfm(ls.sp): # confirm:確認
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
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        dic = lst[aa_]
        frame = tk.LabelFrame(sub,text='下記の契約を削除しますか？')
        fra__= tk.Frame(frame)
        fra__.pack()
        frame.pack(padx=2,pady=2)
        fram_ = tk.Frame(sub)
        fram_.pack(padx=2,pady=2)
        
        auxi.unit.preview( fra__, dic)
        tk.Button( fram_, command= lambda: cfm(aa_,bb_,cc_,dd_,ee_).save(),text='実行',relief="groove",bd=4).pack(side="left",padx=2,pady=2) 
        cansell = tk.Button( fram_, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack(side="left",padx=2,pady=2) 
        
    def save(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        lst = ls.customer()
        lst.pop(aa_)        
        ext.store("customer.txt" ,lst)
        ext.renew( aa_, True, os.path.basename(__file__))
        log.dirc.actv('customer.txt') # ログを作成
        ins = notice.save(None,None,None,None,ee_)
        ins.complete()   

        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    cfm(0,None,None,None,root).post()
    root.mainloop()
        
    
    