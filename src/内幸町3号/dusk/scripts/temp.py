import os.path
import tkinter as tk #Junction:分岐点
import ls
import re
import sys
import notice
import ext

class temp(ls.sp): #Temporarily:一時的に
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
        sub.title('一時止'+'編集  '+ lst[aa_][ls.kb()])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame = tk.Frame(sub )  
        fram_ = tk.Frame(frame )  
        val0 = tk.IntVar(sub)
        val0.set(lst[aa_][ ls.tm()[0] ])
        spn0 = tk.Spinbox(fram_, textvariable=val0, width=3, from_=1,  to=12, state = 'readonly')        
        spn0.pack(side="left", padx=4 ,pady=2) 
        tk.Label(fram_,text='月' ).pack(side="left")  
        val1 = tk.IntVar(sub)
        val1.set(lst[aa_][ ls.tm()[1] ])
        spn1 = tk.Spinbox(fram_, textvariable=val1, width=3, from_=1,  to=31, state = 'readonly')        
        spn1.pack(side="left", padx=4 ,pady=2)   
        tk.Label(fram_,text='日' ).pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set(lst[aa_][ ls.tm()[2] ])
        opt1=tk.OptionMenu(fram_,txt1, '朝刊', '夕刊')  
        opt1.pack(side="left")  
        
        tk.Label(fram_,text='～' ).pack(side="left")  
        val2 = tk.IntVar(sub)
        val2.set(lst[aa_][ ls.tm()[3] ])
        spn2 = tk.Spinbox(fram_, textvariable=val2, width=3, from_=1,  to=12, state = 'readonly')        
        spn2.pack(side="left", padx=2 ,pady=2) 
        tk.Label(fram_,text='月' ).pack(side="left") 
        val3 = tk.IntVar(sub)
        val3.set(lst[aa_][ ls.tm()[4] ])
        spn3 = tk.Spinbox(fram_, textvariable=val3, width=3, from_=1,  to=31, state = 'readonly')        
        spn3.pack(side="left", padx=2 ,pady=2)   
        tk.Label(fram_,text='日' ).pack(side="left")
        
        txt3 = tk.StringVar(sub)
        txt3.set(lst[aa_][ ls.tm()[5] ])
        opt3=tk.OptionMenu(fram_,txt3, '朝刊', '夕刊')  
        opt3.pack(side="left")  
        
        txt4 = tk.StringVar(sub)
        txt4.set(lst[aa_][ ls.tm()[6]])
        opt4=tk.OptionMenu(fram_,txt4, 'ナシ', '取置')   
        opt4.pack(side="left")  
        button0= tk.Button(fram_,command=lambda :brnc(aa_,bb_,[ spn0.get(),spn1.get(),txt1.get(),spn2.get(),spn3.get(),txt3.get(),txt4.get() ],0,ee_).cfm() if spn0.get() !="" and spn1.get() !="" and txt1.get() !="" and spn2.get() !="" and spn3.get() !="" and txt3.get() !="" and txt4.get() !="" else tk.Label(sub,text='未入力の箇所があります' ).pack(),text='次へ',relief="groove",bd=4)
        button0.pack(side="left", padx=5)
        fram_.pack(fill="x",padx=4,pady=4)
        tk.Button( frame, text="一時止情報の消去",command =lambda :brnc(aa_,bb_,cc_,dd_,ee_).clear(),relief="groove",bg="lightgray").pack(padx=2)
        tk.Button( frame, text="キャンセル",command = sub.destroy).pack(padx=2,pady=2)
        frame.pack()

def validate_input(val):
    fmt = '^[0-9]{,1}[0-9]{,1}?$'#'^[+-]?[0-9]{1,2}(?:\.[0-9]{,2})?$'
    if val=='' or re.match(fmt, val):
        return True
    return False 


class brnc(ls.sp):#Branch:分岐
    def cfm(self):  #temporary 一時的
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()        
        sub = tk.Toplevel(ee_) 
        sub.title(lst[aa_][ls.kb()])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        
        frame = tk.LabelFrame(sub,text='下記の内容で保存しますか？')
        tk.Label(frame,text= cc_[0]+'月'+cc_[1]+'日'+cc_[2]+'～'+cc_[3]+'月'+cc_[4]+'日'+cc_[5]+'迄　'+cc_[6]).pack(side="left",padx=15)
        button0= tk.Button(frame,command=lambda :brnc(aa_,bb_,cc_,0,ee_).save(),text='実行',relief="groove",bd=4)
        button0.pack(side="left",anchor="e") 
        frame.pack(padx=2,pady=1)
        frame_ = tk.Frame(sub)
        button1= tk.Button(frame_,command=sub.destroy,text='キャンセル',relief="groove",bd=4,anchor="e")
        button1.pack(side="right")           
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
        for i,item in enumerate( ls.tm()[:7] ):
            lst[aa_][ls.tm()[i]] = cc_[i]
        ext.store("customer.txt" ,lst)
        ins = notice.save(0,0,0,0,ee_)
        ins.complete()        
        
    def clear(self):  #temporary 一時的
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()        
        sub = tk.Toplevel(ee_) 
        sub.title(lst[aa_][ls.kb()])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        
        frame = tk.LabelFrame(sub,text='下記の内容を消去しますか？')
        tk.Label(frame,text= lst[aa_][ls.tm()[0]]+'月'+lst[aa_][ls.tm()[1]]+'日'+lst[aa_][ls.tm()[2]]+'～'+lst[aa_][ls.tm()[3]]+'月'+lst[aa_][ls.tm()[4]]+'日'+lst[aa_][ls.tm()[5]]+'迄　'+lst[aa_][ls.tm()[6]]).pack(side="left",padx=15)
        cc_=["","","","","","",""]
        button0= tk.Button(frame,command=lambda :brnc(aa_,bb_,cc_,0,ee_).save(),text='実行',relief="groove",bd=4)
        button0.pack(side="left",anchor="e") 
        frame.pack(padx=2,pady=1)
        frame_ = tk.Frame(sub)
        button1= tk.Button(frame_,command=sub.destroy,text='キャンセル',relief="groove",bd=4,anchor="e")
        button1.pack(side="right")           
        frame_.pack()


if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
         
    root = tk.Tk() 
    temp(0,0,0,0,root).post()

    root.mainloop()