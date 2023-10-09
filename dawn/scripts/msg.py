import tkinter as tk
from _tkinter import TclError
import ls
from tkinter import messagebox

class sr(): # series:級数
    def a(dct):###alart
        root = tk.Tk() 
        root.attributes('-topmost',True) # 最前面に移動
        #root.overrideredirect(1)#ウィンドウのタイトルバーを消す
        s0, s1, s2 = dct.values()
        root.title(s0) 
        root.withdraw() # root.mainloop不要。
        try:
            root.after( 2500, root.destroy ) 
            messagebox.showinfo( master=root, title = s0, message= s1, detail= s2 )#.show()
            
        except TclError:
            pass
        
    def alr(dct):###alart
        root = tk.Tk() 
        root.title('') 
        root.attributes('-topmost',True) # 最前面に移動
        #root.overrideredirect(1)#ウィンドウのタイトルバーを消す
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()   
        ww,wh
        
        root.option_add( '*font', ['TkDefaultFont', ls.ft()[0]] ) # ls.ft()[2]
        root.option_add( '*Label*background', 'white')
        root.option_add( '*Label*foreground', 'black')
        
        root.configure( bg="white")
        root.attributes("-alpha",0.9)
      
        for s in dct.values():
            tk.Label(root, text=s, font=("TkDefaultFont",ls.ft()[0])).pack(ipadx=4,ipady=4)
        root.after( 1500, root.destroy ) 
        root.mainloop()
        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。  
    dct = {'title':'名称','message':'メモ','detail':'内容'}  
    sr.alr(dct) 