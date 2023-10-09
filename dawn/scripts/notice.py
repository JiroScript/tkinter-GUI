import os.path
import tkinter as tk
import sys
from time import sleep

import ls
import ext
class sp():
    def __init__(self, a,b,c,d,e):
        self.a = a  
        self.b = b 
        self.c = c
        self.d = d
        self.e = e
    def pasS(self):     
        #print(__class__.__name__,sys._getframe().f_code.co_name)
        pass
class save(sp):#
    def complete(self):  #complete:完了  
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()   
        sub = tk.Toplevel(ee_)  
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )    
        frame = tk.Frame(sub)
        frame.pack()
        tk.Label(frame,text="完了しました").pack(side="top",padx=2,pady=5)
        button0= tk.Button(frame,text='閉じる',command = lambda: ee_.destroy())#
        button0.focus_set() 
        button0.bind('<Return>',lambda event:ee_.destroy() )
        button0.pack(side="top",padx=2,pady=1) 
        sleep(0.5)
        ee_.destroy()
        ext.renew( ext.reader('renew.txt')['number'], True, os.path.basename(__file__))
        
    def lead_insert(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        li=[ item for item in lst[aa_] ]
        dct={}
        idx = li.index(bb_)
        for item in li[idx:]:
            num = lst[aa_].pop(item) 
            dct[item] = num
        lst[aa_].update({cc_: dd_})
        lst[aa_].update(dct)  
        lst[aa_].update({cc_: dd_})
        ext.store("customer.txt" ,lst)
        
        ins = save(None,None,None,None,ee_)
        ins.complete()

    def compil(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        li=[ item for item in lst[aa_] ]
        dct={}
        idx =  len( [ i for i in  li[ :li.index(bb_)] ] + [ li[ li.index(bb_)] ] )
        for item in li[idx:]:
            num = lst[aa_].pop(item) 
            dct[item] = num
        lst[aa_].pop(bb_)
        lst[aa_].update({cc_: dd_})
        lst[aa_].update(dct)
        ext.store("customer.txt" ,lst)        
        ins = save(None,None,None,None,ee_)
        ins.complete()
        
    def delete(self):          
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        lst[aa_].pop(bb_)  
        ext.store("customer.txt" ,lst)       
        ins = save(None,None,None,None,ee_)
        ins.complete()
        
    def end_insert(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        li=[ item for item in lst[aa_] ]
        dct={}
        idx = len( [ i for i in  li[ :li.index(bb_)] ] + [ li[ li.index(bb_)] ] ) #li.index(bb_)+1        
        #print( len(list(enumerate(li))))        #print(idx,len(li[:li.index(bb_)]),li.index(bb_),len(li),[i for i in  li[:li.index(bb_)] ] + [i for i in  li[li.index(bb_)] ] )
        for item in li[idx:]:
            num = lst[aa_].pop(item) 
            dct[item] = num
        lst[aa_].update({cc_: dd_})
        lst[aa_].update(dct)
        lst[aa_].update({cc_: dd_})
        ext.store("customer.txt", lst)        
        ins = save(None,None,None,None,ee_)
        ins.complete()        
   

if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    #root = tk.Tk() 
    sub = tk.Toplevel() 
    save(0,'ア','サ',4,sub).end_insert()
    #save(0,'ア',0,0,sub).delete()
    #root.mainloop()