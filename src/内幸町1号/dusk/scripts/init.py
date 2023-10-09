import tkinter as tk
import tkinter.ttk as ttk

class Main(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        button = tk.Button(self, text='re-do', command=lambda: self.re_set(frame))
        button.pack()
        
        frame = tk.LabelFrame(self, text='test', bg='#fff', fg='Blue', name='frm')
        frame.pack(pady=10, anchor=tk.NW)

        test_label = { 'peach':'pink', 'orange':'orange', 'lemon':'yellow'}
        lisT=list(test_label)
        
        mkbutton = ttk.Button(self,text="make",command = lambda:self.make_child(frame,test_label))
        mkbutton.pack(side="left")
        dbutton = ttk.Button(self,text="destroy",command = lambda:self.destroy_child(frame))
        dbutton.pack(side="left")
        
        for i in test_label:
            a = tk.LabelFrame( frame, text=i, name=F'lbf{i}' )#f文字列と呼ばれるフォーマット済み文字列:format()
            a.bind("<1>",lambda event:print(event.widget["text"]))
            b = tk.Label( a, text=test_label[i], name=F'lbl{i}' )
            [widget.pack(side=tk.LEFT) for widget in (a, b)]
            self.nametowidget(F"frm.lbf"+ i) 
            self.nametowidget(F"frm.lbf" + i+".lbl" + i)['text'] 
            label_widget = self.nametowidget(F'frm.lbf{i}.lbl{i}')
            label_widget.configure(bg = test_label[i])

        print(self.nametowidget(F"frm.lbf"+lisT[0])['text'] ,self.nametowidget(F"frm.lbf"+lisT[1]+".lbl"+lisT[1])['text'])
        
    def destroy_child(self,frame):
        children = frame.winfo_children()
        for child in children:
            child.destroy()

    def make_child(self,frame,test_label):
        for i in test_label:
            a = tk.LabelFrame( frame, text=i, name=F'lbf{i}')#f文字列と呼ばれるフォーマット済み文字列
            b = tk.Label(a, text=test_label[i], name=F'lbl{i}')
            [widget.pack(side=tk.LEFT) for widget in (a, b)]
            label_widget = self.nametowidget(F'frm.lbf{i}.lbl{i}')
            label_widget.configure(bg = test_label[i])
        label0 = ttk.Label(frame,text="Sample0")
        label0.pack()
        label1 = ttk.Label(frame,text="Sample1")
        label1.pack()
        label2 = ttk.Label(frame,text="Sample2")
        label2.pack()

    def re_set(self,frame):   
        children = frame.winfo_children()
        if len(children) >0 :  
            test_label = { 'peach': 'peachpuff', 'orange': 'darkorange', 'lemon': 'lemonchiffon'}
            for i in test_label:
                label_widget = self.nametowidget(F'frm.lbf{i}.lbl{i}')
                label_widget['text'] = test_label[i]
                label_widget["bg"] = test_label[i]
            print( label_widget.configure("text")[4] )

def main():
    root = tk.Tk()
    root.geometry("500x500")
    win = Main(root)
    win.pack()
    root.mainloop()

if __name__ == '__main__':
    main()