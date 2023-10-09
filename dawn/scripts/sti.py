import tkinter as tk
import datetime
import os.path
import locale
import sys
import re
from time import sleep
import functools
import notice
import ls
import optionmenu
import ext

locale.setlocale( locale.LC_ALL, '') # locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
    
class sti(): #setting
    def post(  root):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.title('設定') 
        root.geometry( ls.ge(ww,wh) )
        root.option_add( '*font', [ 'TkDefaultFont', 13 ] )
        
        frame = tk.Frame( root)
        frame.pack()      
        r1__, r2__, r3__, r4__, r5__ = tk.LabelFrame( frame, borderwidth= 0 ), tk.LabelFrame(frame), tk.LabelFrame(frame), tk.LabelFrame(frame), tk.LabelFrame(frame)  
        for i in [ r1__, r2__, r3__, r4__, r5__ ]:
            i.pack( fill=tk.X, padx=3, pady=3)
        ( r1__.keys() ) # ['bd', 'borderwidth', 'class', 'fg', 'font', 'foreground',
        r5__.configure( background = 'lightgray' )
        r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3, r4c1, r4c2, r4c3, r5c1, r5c2, r5c3 = tk.Frame(r1__), tk.Frame(r1__), tk.Frame(r1__), tk.Frame(r2__), tk.Frame(r2__), tk.Frame(r2__), tk.Frame(r3__), tk.Frame(r3__), tk.Frame(r3__), tk.Frame(r4__), tk.Frame(r4__), tk.Frame(r4__), tk.Frame(r5__), tk.Frame(r5__), tk.Frame(r5__)    
        for i in [ r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3, r4c1, r4c2, r4c3, r5c1, r5c2, r5c3 ]:
            i.pack( side='left', padx=3, pady=3)
        
        lis = ls.week()
        now = datetime.datetime.now()
        # 日付
        tk.Label(r1c1,text= now.strftime('%Y年%m月%d日')  + '(' +  ls.dp()[ now.weekday() ] + ')' + ('祝日' if sti.ph() else '') ).pack(side='top')
        # 表示
        wv0 = tk.IntVar() # ウィジェット変数は、「ウィジェットと連動する変数」です。別名で「制御変数（Control Variable）」とも呼ばれます。
        uni.rdiobtn( r2__, r2c1, wv0, ( '表示', '全表示', '曜日・祝日別' ), root)
        # リストボックス
        var = tk.StringVar()
        uni.lstbx( r2__, r2c2, var, lis , [], [], [], root )
        # 音声
        wv1, = tk.IntVar(),
        uni.rdiobtn( r3__, r3c1, wv1, ( '音声', '有', '無' ), root)
        
        # この行でインスタンス化 # TypeError: メソッドの名前 missing 1 required positional argument: 'self'

        # テスト, partial：部分的
        ins = sti() 
        for i in range(5):
            tk.Button( r4__, text= i, command= functools.partial( sti.on_click, i )).pack(side='left') # lambda使えない 
            val = tk.IntVar()
            tk.Spinbox( r4__, command= functools.partial( ins.spn_click, i, val), textvariable= val, state = 'readonly', from_= -99, to= 99, width= 2).pack(side='left')

        # 
        uni.cansell( root, 2, 2)
        root.mainloop() 
            
    def spn_click(self, i, val) :
        print( i, val.get())
        
    def on_click(num) :
        print(num)
        
    def ph(): # 祝日か否かを返す, Public Holiday:祝日
        lis = ls.date()
        now = datetime.datetime.now()   
        return now.strftime('%Y-%m-%d') in lis
    
    def tb():#休刊日前日か否かを返す
        lis = ls.the_day_before()
        now = datetime.datetime.now() 
        timedelta = now + datetime.timedelta(days = 1)#delta:差（分）,datetimeオブジェクトとtimedeltaオブジェクトを加算し翌日のtimedaltaオブジェクトを取得
        return timedelta.strftime('%Y-%m-%d') in lis 
     
    def wk():#曜日・祝日別に
        lis = ls.week()
        now = datetime.datetime.now()
        
        keylst=[]
        lstkey =list(lis.keys()) ##'dict_keys'classをリスト型のコンストラクタの引数に指定することでキーの一覧をリストとして取得する
        if '曜日・祝日別' in ls.setting()['表示'] and sti.tb() == False: # '曜日・祝日別' in {'表示':'曜日・祝日別'} and '休刊日前' == False
            if sti.ph() == True:##祝日
                for i,ke_ in enumerate( lis.keys() ):
                    if ls.dp()[ 7 ] not in lis[ ke_ ]: ##'祝' not in　 {'でんき':'月火水木金㊡'}　#week[now.weekday()]
                        keylst.append(ke_) #表示しない新聞をリストに加える
            elif sti.ph() == False:##祝日ではない
                for i,ke_ in enumerate( lis.keys() ):
                    if ls.dp()[ now.weekday() ] not in lis[ ke_ ]: #曜日 not in {'でんき':'月火水木金㊡'}
                        keylst.append(ke_) #表示しない新聞をリストに加える        
        return keylst     
    
    def store( ky, vl):#  
        dct = ls.setting()  
        dct[ ky ] = vl
        (dct[ ky ])
        ext.store( "setting.txt", dct)
        
class uni():
    def lstbx( r2__:any, r2c2:any, var, lis:list, arr0:list, arr1:list, arr2:list, root ):
        
        for i in lis.keys():
            ( i ) # ア マ ヨ サ 産 ト
            arr0.append( i + ' ' + ' ： ' + ' ' + lis[ i ] )
            arr1.append( i )
            arr2.append( lis[ i ] )
        
        scrollbar = tk.Scrollbar( r2c2)
        scrollbar.pack( side="right",fill="y")
        var.set( arr0)
        listbox = tk.Listbox( r2c2, listvariable = var, heigh=10, width=25)
        listbox.config( yscrollcommand=scrollbar.set)
        listbox.pack()
        listbox.bind( "<<ListboxSelect>>", lambda event:cmp( 0, arr1[ listbox.curselection()[0] ], arr2[ listbox.curselection()[0] ], 0, root).post() )
        scrollbar.config( command=listbox.yview ) 

    # 音、　声 # vox（ラテン語）:声
    def rdiobtn( lf:any, frame:any, wv:int, tpl:tuple, root ): # ウィジェット変数は、「ウィジェットと連動する変数」です。別名で「制御変数（Control Variable）」とも呼ばれます。
        txt0, txt1, txt2 = tpl
        lf.configure( text = txt0 )

        if ls.setting()[ txt0 ] == txt1 :
            wv.set(0)
        elif ls.setting()[ txt0  ] == txt2 :
            wv.set(1)       
        rdo1 = tk.Radiobutton(frame, variable=wv, value=0, command=lambda:sti.store( txt0, rdo1['text']), text= txt1 )        
        rdo1.pack(side='left')
        rdo2 = tk.Radiobutton(frame, variable=wv, value=1, command=lambda:sti.store( txt0, rdo2['text']), text= txt2 )
        rdo2.pack(side='left')
        
    def cansell( root, x, y ):
        cansell = tk.Button( root, font=( "TkDefaultFont", ls.ft()[1]), text='☓', command= root.destroy, bd=4, )
        cansell.focus_set() #
        cansell.bind('<Visibility>', lambda event:None)
        cansell.bind('<Return>', lambda event:root.destroy() )
        cansell.pack( padx= x, pady= y)

class S():
    # 「部数」のreliefのオプションを返す　
    def S_S_L( txt, txx, arr): 
        txt # ア          
        txx # 曜日・祝日別
        arr # ['工', '日産', '自動車', '海事', '建通', '電波', 'でんき', 'せんけん', '農業', 'ガイド', '報知', '日刊スポ', 'スポニチ', 'サンスポ', 'デイリー', 'F・T', 'A', 'Y', 'JAPAN-TIMES/NYT', '朝日小学生', '毎日小学生', 'ア', 'マ', 'ヨ', 'サ', '産', 'ト']
        char = "groove"
        if txx == '全表示' :
            if txt not in ls.nw()[0]:
                char = "raised"
        elif txx == '曜日・祝日別' :
            if txt in arr and txt not in ls.nw()[0]:
                char = "raised" #'raised', 'sunken', 'flat', 'groove', 'ridge'
        return char
    
    def T_L( tpl, arr): 
        txt, txx = tpl # ア,  曜日・祝日別        
        arr # ['工', '日産', '自動車', '海事', '建通', '電波', 'でんき', 'せんけん', '農業', 'ガイド', '報知', '日刊スポ', 'スポニチ', 'サンスポ', 'デイリー', 'F・T', 'A', 'Y', 'JAPAN-TIMES/NYT', '朝日小学生', '毎日小学生', 'ア', 'マ', 'ヨ', 'サ', '産', 'ト']
        (txt, txx, arr)
        char = 'flat'
        if txx == '全表示' :
            if txt not in ls.nw()[0]:
                char = "raised"
        elif txx == '曜日・祝日別' :
            if txt in arr and txt not in ls.nw()[0]:
                char = "raised" #'raised', 'sunken', 'flat', 'groove', 'ridge'
        return char

    # 「メモ」のbgのオプションを返す。    
    def M_S( day_of_week, txt:str)->str: # datetime.datetime.now()「モジュール（module）」
        dic = { '㊊':'#ffea00', '㊋':'crimson', '㊌':'lightblue', '㊍':'lightgreen', '㊎':'gold', '㊏':'khaki','㊐':'#b7282e' }
        Mon, Tue, Wed, Thu, Fri, Sat, Sun = list(dic)
        
        char = "white" # character:文字
        if Mon in txt and '月' == day_of_week:
            char = dic[Mon]
        elif Tue in txt and '火' == day_of_week:
            char = dic[Tue]
        elif Wed in txt and '水' == day_of_week:
            char = dic[Wed]
        elif Thu in txt and '木' == day_of_week:
            char = dic[Thu]
        elif Fri in txt and '金' == day_of_week:
            char = dic[Fri]
        elif Sat in txt and '土' == day_of_week:
            char = dic[Sat]
        elif Sun in txt and '日' == day_of_week:
            char = dic[Sun]
        return char
    
class T():
    # 「メモ」、㊗ ㊟、reliefのオプション、bd（ボーダーの幅）の値を返す　
    def M_S( today, txt:str)->tuple: # （reliefのオプション, Int）をタプルで返す 
        tpl = ('flat', 1)
        if '㊗' in txt:
            lis = ls.date() # ['2022-01-01', '2022-01-10', '2022-02-11', 
            lis.append # (today) test
            if today in lis:
                tpl = ('sunken', 3 ) #'raised', 'sunken', 'flat', 'groove', 'ridge'
        elif '㊟' in txt:
            tpl = ('raised', 3 )
        return tpl
        
class L():
    def S( lis, bol, day_of_week:str)->list: # Issue:発行
        lis # {'工': '月火水木金祝', '日産': '月火水木金',
        bol # 祝日か否かを返す :boolean
        day_of_week # '月'
        if bol:
            arr = [ k for k,v in lis.items() if '祝' in v if day_of_week in v]
        elif bol == False:
            arr = [ k for k,v in lis.items() if day_of_week in v]
        return arr # ['日産', '工', '流通', '自動車', 'でんき', '電波', '海事', '通信', '農業']
        
class cmp(ls.sp): #compilation:編集
    def post(self):        
        aa_, bb_, cc_, dd_, ee_ = self.a, self.b, self.c, self.d, self.e   
        notice.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        sub = tk.Toplevel(ee_) 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame=tk.LabelFrame(sub,text='「' + bb_ + '」' + "を配達する曜日にチェックを付けて下さい")
        tk.Label(frame,text='').pack()
        var = []
        for i ,ke_ in enumerate(ls.dp()):
            var.append(tk.IntVar())#Widget変数（別名：制御変数）,StringVarなど4種、-textvariableや-variableオプションに指定することのできる変数。get()で値の取得、set()で値の設定ができる。
            if ls.dp()[i] in cc_:
                var[i].set(1)
            tk.Checkbutton(frame,variable=var[i],text=ke_,relief="groove").pack(side='left',padx=1)
                      
        frame.pack(padx=2,pady=2)
        tk.Button(sub,command =lambda :cmp(0,bb_,var,0,ee_).cnf(), text="次へ").pack(padx=2,pady=2)     
        
        cansell = tk.Button( sub, text="キャンセル", command = sub.destroy, relief="groove", bd=4, anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        sub.mainloop()#これがないとチェックが付かない。
        
    def cnf(self): # confirmation 確認    
        aa_, bb_, cc_, dd_, ee_ = self.a, self.b, self.c, self.d, self.e   
        notice.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        sub = tk.Toplevel(ee_) 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge( ww, wh) )
        row = ""
        var = cc_
        for i in range(len(var)):
            if var[i].get() == 1:
                row += ls.dp()[i]
        
        frame = tk.LabelFrame( sub, text= "下記の内容で保存しますか？")
        tk.Label(frame,text = row).pack()
                
        frame.pack(padx=2,pady=2)
        tk.Button(sub,command =lambda :cmp( None, bb_, row, None, ee_).store(), text="保存").pack(padx=2,pady=2)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        
    def store(self):        
        aa_, bb_, cc_, dd_, ee_ = self.a, self.b, self.c, self.d, self.e   
        notice.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        dct = ls.week()  
        dct[ bb_] = cc_
        ext.store("week.txt" ,dct)
        ins = notice.save( None, None, None, None, ee_)
        ins.complete()

if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。        
    root = tk.Tk()
    sti.post( root)
    sti.ph()