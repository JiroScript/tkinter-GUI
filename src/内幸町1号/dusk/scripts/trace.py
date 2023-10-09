import tkinter as tk

def callback(sv):
    print(sv.get())

root = tk.Tk()
sv = tk.StringVar()
sv.trace("w", lambda name, index, modegg, sv=sv: callback(sv))
e = tk.Entry(root, textvariable=sv)
e.pack()
var= tk.BooleanVar(value=True)
var.trace("w", lambda name, index, modegg, var=var: callback(var))
tk.Button(root,text='閉じる',command =lambda: var.set(False) ).pack()
        
root.mainloop()  