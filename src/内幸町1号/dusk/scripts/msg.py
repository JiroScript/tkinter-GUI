import tkinter as tk
from tkinter.messagebox import Message 
from _tkinter import TclError
import ls

def msg():#message 
    TIME_TO_WAIT = 2000 # in milliseconds 
    root = tk.Tk() 
    root.withdraw()
    try:
        root.after(TIME_TO_WAIT, root.destroy) 
        tk.Label(root,text="Hello World").pack()

        Message(title="alart", message="double click", master=root).show()
    except TclError:
        pass
    
def alart():
    TIME_TO_WAIT = 3000 # in milliseconds 
    root = tk.Tk()  
    root.overrideredirect(1)#ウィンドウのタイトルバーを消す
    ww = root.winfo_screenwidth() 
    wh = root.winfo_screenheight()    
    
    root.after(TIME_TO_WAIT, root.destroy)
    label=tk.Label(root, text="Double click",font=("System",ls.ft()[0]), bg = "yellow" ,fg='black')
    label.pack(ipadx=10,ipady=10)
    root.lift()#最前列表示？
    root.focus_force()
    root.update_idletasks()
    root.geometry( str(label.winfo_width())+"x"+str(label.winfo_height())+"+"+str(int(ww/2))+"+"+str(int(wh/2))) 
    
    root.mainloop()

if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    #msg()
    alart()
    