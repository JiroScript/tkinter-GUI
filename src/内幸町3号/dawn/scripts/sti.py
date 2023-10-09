import tkinter as tk
import datetime
import os.path
import locale
import sys
import re
import notice
import ls
import optionmenu
import ext
locale.setlocale(locale.LC_ALL, '')#locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
now=datetime.datetime.now()

class sti(ls.sp): #setting
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #  
        notice.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()                 
        lst = ls.week()
    
        root = tk.Toplevel() 
        root.title("【設定】")
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.geometry( ls.ge(ww,wh) )
        frame = tk.Frame(root)
        
        fram=tk.Frame(frame)
        tk.Label(fram,text= now.strftime('%Y年%m月%d日')  + '(' +  ls.dp()[ now.weekday() ] + ')' + ('祝日' if sti.ph() else '') ).pack()
        vr = tk.IntVar()
        vr.trace("w",sti.trace_)
        if ls.setting()[ ls.dl()[0] ] == ls.dl()[1] :
            vr.set(0)
        elif ls.setting()[ ls.dl()[0] ] == ls.dl()[2] :
            vr.set(1)
        lf=tk.LabelFrame(fram)    
        rdo1 = tk.Radiobutton(lf, value=0,command=lambda:sti.store(rdo1['text']), variable=vr, text= ls.dl()[1])        
        rdo1.pack(side='left')
        rdo2 = tk.Radiobutton(lf, value=1,command=lambda:sti.store(rdo2['text']), variable=vr, text= ls.dl()[2])
        rdo2.pack(side='left')
        lf.pack()
        
        fram.pack(side='right')
        fram=tk.Frame(frame)
        multi =[] #multidimensional:多次元
        keY =[]
        valuE=[]
        for i,ke_ in enumerate( lst.keys()  ):
            keY.append( ke_  )
            valuE.append( lst[ke_] )
            multi.append( ke_ + ' ' + ' : ' + ' ' + lst[ke_]  )
        
        scrollbar = tk.Scrollbar(fram)
        scrollbar.pack(side="right",fill="y")
        
        ###var = tk.StringVar(value = multi)
        var = tk.StringVar(value = multi)
        listbox = tk.Listbox(fram ,listvariable = var ,heigh=10 ,width=25)
        listbox.config(yscrollcommand=scrollbar.set)
        listbox.pack()
        
        listbox.bind("<<ListboxSelect>>", lambda event:cmp(0,keY[ listbox.curselection()[0] ],valuE[ listbox.curselection()[0] ],0,root).post() )
                
        scrollbar.config(command=listbox.yview)        
        fram.pack(side='right',padx=3)
        frame.pack(padx=2)
        #tk.Button(root, text="戻る",command = root.destroy,width=7).pack(padx=3,pady=3)
        cansell = tk.Button(root, text="キャンセル" ,command = root.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:root.destroy() )
        cansell.pack()
        root.mainloop() 
    
    def ph():#祝日か否かを返す
        lst = ls.date()
        now = datetime.datetime.now()   
        return now.strftime('%Y-%m-%d') in lst
    
    def tb():#休刊日前日か否かを返す
        lst = ls.the_day_before()
        now = datetime.datetime.now() 
        timedelta = now + datetime.timedelta(days = 1)#delta:差（分）,datetimeオブジェクトとtimedeltaオブジェクトを加算し翌日のtimedaltaオブジェクトを取得
        return timedelta.strftime('%Y-%m-%d') in lst 
     
    def wk():#曜日・祝日別に
        lst = ls.week()
        now = datetime.datetime.now()
        
        keylst=[]
        lstkey =list(lst.keys()) ##'dict_keys'classをリスト型のコンストラクタの引数に指定することでキーの一覧をリストとして取得する
        if ls.dl()[2] in ls.setting()[ls.dl()[0]] and sti.tb() == False:##'曜日・祝日別' in {'表示':'曜日・祝日別'} and '休刊日前' == False
            if sti.ph() == True:##祝日
                for i,ke_ in enumerate( lst.keys() ):
                    if ls.dp()[ 7 ] not in lst[ ke_ ]: ##'祝' not in　 {'でんき':'月火水木金㊡'}　#week[now.weekday()]
                        keylst.append(ke_) #表示しない新聞をリストに加える
            elif sti.ph() == False:##祝日ではない
                for i,ke_ in enumerate( lst.keys() ):
                    #print('lst',ls.dp()[now.weekday() ],ke_,lst[ke_] )
                    if ls.dp()[ now.weekday() ] not in lst[ ke_ ]: #曜日 not in {'でんき':'月火水木金㊡'}
                        keylst.append(ke_) #表示しない新聞をリストに加える        
        return keylst     
    
    def trace_(*args):
        pass
    def store(val):#         
        dct = ls.setting()  
        dct[ ls.dl()[0] ] = val
        ext.store("setting.txt" ,dct)
        
        
class cmp(ls.sp): #compilation:編集
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #  
        notice.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        sub = tk.Toplevel(ee_) 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        
        frame=tk.LabelFrame(sub, text ='「' + bb_ + '」' + "を配達する曜日にチェックを付けて下さい")
        tk.Label(frame,text='').pack()
        var=[]
        for i ,ke_ in enumerate(ls.dp()):
            var.append(tk.IntVar())#Widget変数（別名：制御変数）,StringVarなど4種、-textvariableや-variableオプションに指定することのできる変数。get()で値の取得、set()で値の設定ができる。
            if ls.dp()[i] in cc_:
                var[i].set(1)
            tk.Checkbutton(frame,variable=var[i],text=ke_,relief="groove").pack(side='left',padx=1)
                      
        frame.pack(padx=2,pady=2)
        tk.Button(sub,command =lambda :cmp(0,bb_,var,0,ee_).cnf(), text="次へ").pack(padx=2,pady=2)        
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy())
        cansell.pack()
        sub.mainloop()#これがないとチェックが付かない。
        
    def cnf(self):       #confirmation 確認        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #  
        notice.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        sub = tk.Toplevel(ee_) 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        row = ""
        var = cc_
        for i in range(len(var)):
            if var[i].get() == 1:
                row += ls.dp()[i]
        
        frame=tk.LabelFrame(sub,text="下記の内容で保存しますか？")
        tk.Label(frame,text = row).pack()
                
        frame.pack(padx=2,pady=2)
        tk.Button(sub,command =lambda :cmp(0,bb_,row,0,ee_).store(), text="保存").pack(padx=2,pady=2)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        
    def store(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #
        notice.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        dct = ls.week()  
        dct[ bb_] = cc_
        ext.store("week.txt" ,dct)
        ins = notice.save(0,0,0,0,ee_)
        ins.complete()

     
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    sti(0,0,0,0,0).post()