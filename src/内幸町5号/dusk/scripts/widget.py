import tkinter as tk
import tkinter.messagebox as tmb

root = tk.Tk()

# Labelframe and Label 1, 2
tk.Label(root, text="1, 2: Labelframe \nand Label").grid(row=0, sticky="e")
labelframe = tk.LabelFrame(root, text="LabelFrame")
labelframe.grid(row=0, column=1, padx=10, pady=10)
tk.Label(labelframe, text="Label").pack() 

# Button 3
tk.Label(root, text="3: Button").grid(row=1, sticky="e")
tk.Button(root, text="Button", command=lambda : tmb.showinfo("メッセージ", "clicked")).\
    grid(row=1, column=1, padx=10, pady=10)

# Entry 4
tk.Label(root, text="4: Entry").grid(row=2, sticky="e")
tk.Entry(root).grid(row=2, column=1, padx=10, pady=10)

# Checkbutton 5
tk.Label(root, text="5: CheckButton").grid(row=3, sticky="e")
tk.Checkbutton(root, text="A").grid(row=3, column=1, padx=10, pady=10)

# radioButton 6
tk.Label(root, text="6: RadioButton").grid(row=4, sticky="e")
frame_for_radio = tk.Frame(root)
frame_for_radio.grid(row=4, column=1, padx=10, pady=10)
iv1 = tk.IntVar()
iv1.set(1)
tk.Radiobutton(frame_for_radio, text="a", value=1, variable=iv1).pack()
tk.Radiobutton(frame_for_radio, text="b", value=2, variable=iv1).pack()
tk.Radiobutton(frame_for_radio, text="c", value=3, variable=iv1).pack()

# OptionMenu 7
tk.Label(root, text="7: OptionMenu").grid(row=5, sticky="e")
sv1 = tk.StringVar()
sv1.set('オプション１')
tk.OptionMenu(root, sv1, 'オプション１', 'オプション２').grid(row=5, column=1, padx=10, pady=10) 

# Listbox 8
tk.Label(root, text="8: Listbox").grid(row=6, sticky="e")
listbox = tk.Listbox(root, height=4)
for line in ["選択肢1", "選択肢2","選択肢3","選択肢4", "選択肢5"]:
    listbox.insert(tk.END, line)
listbox.select_set(1)
listbox.grid(row=6, column=1, padx=10, pady=10)

# Spinbox 9
tk.Label(root, text="9: Spinbox").grid(row=0, column=2, sticky="e")
tk.Spinbox(root, values=(2, 4, 10)).grid(row=0, column=3, padx=10, pady=10)

# Scale 10
tk.Label(root, text="10: Scale").grid(row=1, column=2, sticky="e")
tk.Scale(root, from_=10, to=80, label='Scale', orient=tk.HORIZONTAL).grid(row=1, column=3, padx=10, pady=10) 

# Message 11
tk.Label(root, text="11: Message").grid(row=2, column=2, sticky="e")
tk.Message(root, text="私の名前は中村です").grid(row=2, column=3, padx=10, pady=10)

# Text 12
tk.Label(root, text="12: Text").grid(row=3, column=2, sticky="e")
text = tk.Text(root, width=20, height=6)
text.insert(tk.END, "sample text\n1\n2\n3")
text.grid(row=3, column=3, padx=10, pady=10)

# ScrollBar with Listbox 13
tk.Label(root, text="13: Listbox \n& ScrollBar").grid(row=4, column=2, sticky="e")
scrollbar_frame = tk.Frame(root)
scrollbar_frame.grid(row=4, column=3, padx=10, pady=10)
listbox2 = tk.Listbox(scrollbar_frame)
for i in range(1000):
    listbox2.insert(tk.END, i)
listbox2.pack(side=tk.LEFT)
scroll_bar =tk.Scrollbar(scrollbar_frame, command=listbox2.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
listbox2.config(yscrollcommand=scroll_bar.set)

# Canvas 14
tk.Label(root, text="14: Canvas").grid(row=5, column=2, sticky="e")
canvas = tk.Canvas(root, bg='white', width=200, height=100)
canvas.grid(row=5, column=3, padx=10, pady=10)
canvas.create_oval(25, 15, 180, 60, fill='red')
canvas.create_oval(25, 45, 180, 85, fill='blue')
canvas.create_text(100, 90, text='Canvasウィジェット', fill="green")

# PanedWindow 15
tk.Label(root, text="15: PanedFrame").grid(row=6, column=2, sticky="e")
panedwindow_frame = tk.Frame(root)
panedwindow_frame.grid(row=6, column=3, padx=10, pady=10)
panedwindow1 = tk.PanedWindow(panedwindow_frame)
text1 = tk.Text(panedwindow1, height=6, width=15)
text1.insert(tk.END, "中村拓男")
panedwindow1.add(text1)
panedwindow1.pack(fill=tk.BOTH, expand=2)
panedwindow2 = tk.PanedWindow(panedwindow1)
text2 = tk.Text(panedwindow1, height=6, width=15)
text2.insert(tk.END, "中村香織")
panedwindow2.add(text2)
panedwindow1.add(panedwindow2)


root.title("いろいろなウィジェット")
root.mainloop()