import tkinter as tk
import sys
import ls

class option(ls.sp): 
    def onMenuCommand(cmd):
        ( cmd) # 'ア' 
        
    def select(self):       
        bb_, cc_, dd_  = self.b, self.c, self.d #
        ['一般日刊紙','産業･金融・流通','株式・証券・税務','交通・運輸・鉄鋼','建設・住宅・電気','石油・繊維・農林','スポーツ紙','海外紙・国内英字紙','青少年向き・レジャー・趣味','一般夕刊紙','各種の縮刷版・その他']
        bb_ # <class 'tkinter.OptionMenu'>
        menu = bb_['menu'] # <class 'tkinter.Menu'>
        sVar1 = cc_ # <class 'tkinter.StringVar'>
        sVar2 = dd_ # tk.StringVar(sub)
        d = option.D() # { '一般日刊紙':['ア','マ','ヨ','サ','産','ト']}
        l = d.get( sVar1.get()) # ['ア','マ','ヨ','サ','産','ト']
        menu.delete( 0, tk.END)
        for s in l :
            menu.add_command( label= s , command= tk._setit( sVar2, s, option.onMenuCommand))  # tk._setit、値iをウィジェット変数sVar2に格納。
            
    def D():
        return { ls.mn()[0]:ls.nw()[0],
             ls.mn()[1]:ls.nw()[1],
             ls.mn()[2]:ls.nw()[2],
             ls.mn()[3]:ls.nw()[3] + ls.nw()[4],
             ls.mn()[4]:ls.nw()[5] + ls.nw()[6],
             ls.mn()[5]:ls.nw()[7] + ls.nw()[8] + ls.nw()[9],
             ls.mn()[6]:ls.nw()[10],
             ls.mn()[7]:ls.nw()[11] + ls.nw()[12],
             ls.mn()[8]:ls.nw()[13] + ls.nw()[14],
             ls.mn()[9]:ls.nw()[15],
             ls.mn()[10]:ls.nw()[16] + ls.nw()[17] }

    def division(self): # division:区分
        bb_, cc_, dd_  = self.b, self.c, self.d #
        bb_ # <class 'tkinter.OptionMenu'>
        menu = bb_['menu']
        sVar1 = cc_ # <class 'tkinter.StringVar'>
        sVar2 = dd_ # tk.StringVar(sub)
        d = { ls.pa()[0]: ls.ea()[0], ls.pa()[1]: ls.ea()[1] } # 
        l = d.get( sVar1.get()) # ['ア','マ','ヨ','サ','産','ト']
        menu.delete( 0, tk.END)
        for s in l :
            menu.add_command( label= s , command= tk._setit( sVar2, s, option.onMenuCommand))  # tk._setit、値iをウィジェット変数sVar2に格納。
        
    def human(self): #
        bb_, cc_, dd_  = self.b, self.c, self.d #
        bb_ # <class 'tkinter.OptionMenu'>
        menu = bb_['menu']
        sVar1 = cc_ # <class 'tkinter.StringVar'>
        sVar2 = dd_ # tk.StringVar(sub)
        d = { ls.rw()[0]: ls.hu()[0], ls.rw()[1]: ls.hu()[1] } # 
        l = d.get( sVar1.get()) # ['ア','マ','ヨ','サ','産','ト']
        menu.delete( 0, tk.END)
        for s in l :
            menu.add_command( label= s , command= tk._setit( sVar2, s, option.onMenuCommand))  # tk._setit、値iをウィジェット変数sVar2に格納。
                        
class LF(tk.LabelFrame):
        
    def __init__( self, frame, dic):
        super().__init__( master= frame, text= '編集') # 継承した親クラスのメソッドを使えるようになる、
        self.pack()
        self.bind("<Enter>", self.getEventEnter )
        self.bind("<Leave>", self.getEventLeave, '+')
        self.dic = dic
        self.create_widgets()
        #

    # オブジェクトを定義し,その後のオブジェクト()の記述で、__call__が呼び出される特殊なメソッド
    # __call__にはreturnを記載することが出来る    
    def __call__(self, event=None):
        self.button.configure(bg='yellow')
        return self.sVar2
        
    def btn_(self):
        self.label.configure( bg="yellow")
        self.label.configure( text= self.sVar2.get())
        
    def create_widgets(self):
        #Button
        self.label= tk.Label( self, text= '')
        self.label.pack()
        self.sVar1= tk.StringVar()
        self.sVar1.set('カテゴリ')
        self.sVar2= tk.StringVar()
        self.sVar2.set(str(self.dic.get('区分')))
        self.opm1= tk.OptionMenu(self, self.sVar1, *ls.pa() ,command=lambda event:self.menu_add() )
        self.opm1.pack(side='left')
        (self.sVar1, self.sVar1.get())
        self.opm2= tk.OptionMenu(self, self.sVar2, *ls.ea()[0], *ls.ea()[1])
        self.opm2.config(relief=tk.GROOVE)
        self.opm2.pack(side='left')    
        self.button = tk.Button( self, text='次へ', command= self.btn_)
        self.button.configure( command= self.btn_) # do not forget to add self!
        self.button.pack( side='left')
        
    def menu_add(self):
        d = self.d() # 
        l = d.get( self.sVar1.get()) # 
        self.opm2['menu'].delete( 0, tk.END)
        for s in l : # ['人事院', '弁護士会館', '富国生命', 
            self.opm2['menu'].add_command( label= s , command= tk._setit( self.sVar2, s, None))  # tk._setit、値iをウィジェット変数sVar2に格納。

    def d(self): # {'内幸町': ['人事院', '弁護士会館', '富国生命', 'プレスセンター', '厚生労働省', '日比谷国際ビル', 'パークフロント'], '永田町': ['国会議事堂', '総理大臣官邸', '国会図書館']}
        return { ls.pa()[0]:ls.ea()[0], ls.pa()[1]:ls.ea()[1]}
        
    def getEventEnter( self, event):
        self.configure( relief= 'ridge')
        
    def getEventLeave( self, event):
        self.configure( relief= 'groove')

if __name__ == '__main__': ##これがないと外部からインポートされた際に処理が実行されてしまう。        
    root = tk.Tk()
    ww, wh = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry( ls.ge( ww, wh))
    #
    frame = tk.Frame(root)
    frame.pack()
    lst = ls.customer()
    dic = lst[0]
    
    sVar = tk.StringVar()
    sVar.set('カテゴリ')
    if None:
        pass
    LF( frame, dic)
    #
    root.mainloop()         