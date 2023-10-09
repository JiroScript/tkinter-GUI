import threading
import tkinter as tk
import pyttsx3
import locale
import time, datetime
import vox, ls

class b():
    def run(n):
        # threading.current_thread().nameはgetName()を呼び出す
        print("task: {} (thread name: {})".format(n, threading.current_thread().name))
        time.sleep(0.5)
        print('2s')
        time.sleep(0.5)
        print('1s')
        
        time.sleep(.5)
        print('0s')
        time.sleep(0.5)
    
    def th():
        now = datetime.datetime.now()
        now
        vox.dates.C
        time.sleep(5)
        t1 = threading.Thread(target= b.run('uno'), args=("t1",)) # vox.dates.C( now)
        t2 = threading.Thread(target= b.run('duo'), args=("t2",), name='Thread T2') # ここではsetName()が呼び出される
        # start()
        t1.start()
        t2.start()
        # join()
        t1.join()
        t2.join()
        # join()を呼び出したため
        # メインスレッドは上記のスレッドが終わるまで待機し
        # 全部終わったらprintする
        (threading.current_thread().name)
    
class Test1():
    def __init__(self):
        self.started = threading.Event()
        self.alive = True
        self.thread = threading.Thread(target=self.func)
        self.thread.start()
        
    def __del__(self):
        self.kill()

    def begin(self):
        print("begin")
        self.started.set()
        
    def end(self):
        self.started.clear()
        print("end")
    
    def kill(self):
        self.started.set()
        self.alive = False
        self.thread.join()
        
    def func(self):
        #test = Test1()
        i = 0
        self.started.wait()
        while self.alive :
            i += 1
            print("{}\n".format(i), end="")
            self.started.wait()
            if i > 9999:
                print("break")
                break
        #test.end()
        print("loop end")
            
class p():
    def C( now, line):
        locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
        engine = pyttsx3.init()
        #参照した言葉
        
        engine.getProperty("rate")
        engine.setProperty("rate",100)
        
        engine.getProperty('volume')
        engine.setProperty('volume',2.0)
        
        #参照した言葉の出力
        (line)
        engine.say(line)
        engine.runAndWait()
        
    def wdgt( now, words, root):
        word = "".join(words)
        word
        for i in words:
            root.title("音声") 
            #root.geometry( ls.ge(ww/3,wh/3) )
            root.option_add( '*font', ['TkDefaultFont', ls.ft()[0]] ) # ls.ft()[2]
            root.option_add( '*background', 'black')
            root.configure( bg="black")
            root.option_add( '*Label*background', 'black')
            root.option_add( '*Label*foreground', 'red')
            frame= tk.Frame( root) #
            frame.pack()      
            tk.Label( frame, text= i ).pack()
            root.bind('<Button>', lambda event: root.destroy())
            root.bind('<MouseWheel>', lambda event: root.destroy())
            root.bind('<Motion>', lambda event: None)
            p.C( now, i)
            print(i)
        btn= tk.Button( frame, text= "削除", command=lambda:root.destroy() )
        btn.pack()
        root.after(3000, root.destroy)
        root.mainloop()
        
    def cancel( frame, sub):
        cancel = tk.Button( frame, text= "閉じる", command= sub.withdraw, width=8)
        cancel.bind('<FocusOut>', lambda event: sub.destroy())
        cancel.bind('<Return>', lambda event: sub.destroy())
        cancel.bind('<Motion>', lambda event: None)
        cancel.pack( padx=2 ,pady=2)
        cancel.focus_force()  
        
if __name__ == "__main__":
    locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

    now=datetime.datetime.now()
    days = now.strftime('%m月%d日')
    times = now.strftime(' %H:%M')
    
    words = [ "本日は", days , ' ', times, "です"][:1]
    p.wdgt#(  now, words, tk.Tk()) #
    """
    """
    test = Test1()
    test.begin()
    time.sleep(2)
    test.end()
    test.begin()
    time.sleep(2)
    test.end()
    test.begin()
    time.sleep(2)
    test.end()
    test.kill()
    b.th#()

     