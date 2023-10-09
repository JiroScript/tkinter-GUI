import tkinter as tk

root = tk.Tk()
val = tk.IntVar() 
val.set(3)  
v = ('apple', 'banana', 'cherry', 'grape', 'orange')
s1=tk.Spinbox(root,textvariable=val, from_=0, to=999,command=lambda:print(val.get()) )
s2=tk.Spinbox(root,value = v, from_=0, to=10, state = 'readonly')

for w in (s1, s2):
    w.pack(padx = 5, pady = 5)
root.mainloop()