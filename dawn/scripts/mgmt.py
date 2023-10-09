import pandas as pd # management: 管理,
import tkinter as tk
import itertools
import os.path
import functools
import os
import ls
import sys
import ext
import time
import call

class L:
    def news():  
        arr =list(reversed(ls.nw()[0]))
        ll = [ list(arr)] + list(ls.nw())[1:]
        l = [ i for l in ll for i in l ]
        return l # ['ト', '産', 'サ', 'ヨ', 'マ', 'ア', '工', '日産', '流通', 'ヴェリタス', 
    
class DD:
    def LD( lst, hss ):
        for i, dic in enumerate(lst):
            for k in dic.keys() : 
                if k not in ls.kl():
                    hss.setdefault( dic.get('区分'), {}) # 
                    hss[ dic.get('区分') ].setdefault( k , 0) # ネスト構造
                    hss[ dic.get('区分')][ k ] = dic.get( k ) if k  not in hss[ dic.get('区分') ].keys() else hss[ dic.get('区分')].get( k ) +  int(dic.get( k ))
        return hss # {'人事院': {'ア': 14, 'マ': 12, 'ヨ': 18, 'サ': 31, '産': 11, 'ト': 9, 'A': 2, '農業': 1}, '弁護士会館': {'ア': 10, 'マ': 10, 
    # 整列する。ト⇨ア
    def LD_L( lst, l , hss ):
        l = L.news()
        for i, dic in enumerate(lst):
            for k in l : 
                if k in dic.keys():
                    hss.setdefault( dic.get('区分'), {}) # 
                    hss[ dic.get('区分') ].setdefault( k , 0) # ネスト構造
                    hss[ dic.get('区分')][ k ] = dic.get( k ) if k  not in hss[ dic.get('区分') ].keys() else hss[ dic.get('区分')].get( k ) +  int(dic.get( k ))
        return hss # {'人事院': {'ア': 14, 'マ': 12, 'ヨ': 18, 'サ': 31, '産': 11, 'ト': 9, 'A': 2, '農業': 1}, '弁護士会館': {'ア': 10, 'マ': 10, 

class cum(ls.sp): # Cumulative:総計 
    def post( root):      
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        root.title("【部数管理】")
        ww, wh = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry( ls.ge( ww,wh+wh) )
        root.option_add( '*font', [ 'TkDefaultFont', 11 ] ) #16
        lst = ls.customer()        
        hss = DD.LD( lst, {}) # {'人事院': {'ア': 14, 'マ': 12, 'ヨ': 18, 'サ': 31, '産': 11, 'ト': 9, 'A': 2, '農業': 1}, '弁護士会館': {'ア': 10, 'マ': 10, 
        ktvd = Dtd.LD_L(lst, ['区分', '区間'], {}) # {('人事院', ''): {'ア': 14, 'マ': 12, 'ヨ': 18, 'サ': 31, '産': 11, 'ト': 9, 'A': 2, '農業': 1}, ('弁護士会館', ''): {'ア': 10,
        sst = { k for d in lst for k in d.keys() if k not in ls.kl() } # {'Y', '日刊スポ', 'ガイド', '産', '海事', 'A', 
        dct = { k : None for k in L.news() if k in sst } # {'ト': None, '産': None, 'サ': None, 'ヨ': None, 'マ': None, 'ア': None, '工': None, '日産': None,
        cum.sepa( hss, ktvd, dct, root)
        
    def sepa( hss, ktvd, dct, root):
        if ls.sort()['設定'] == '全表示' :
            single.main( hss, dct, root)
        elif ls.sort()['設定'] == 'グループ別表示' :
            group.main( hss, ktvd, dct, root)
        elif ls.sort()['設定'] == 'グループ設定' :
            setting.main( hss, ktvd, root)
            
    #　辞書が足りない、 作成する、 グループ１として、
    def create( lst): # create:作成
        dt = { ( d.get('区分'), d.get('区間')) for d in lst } # {('パークフロント', ''), ('人事院', ''), ('プレスセンター', 'A'), 
        lt = ls.group().keys() # dict_keys([('人事院', ''), ('弁護士会館', ''), ('富国生命', 'A'), ('富国生命', ''), ('プレスセンター', ''), 
        arr = [ i for i in dt if i not in lt ]        
        # グループ１として作成。
        if len(arr) > 0 : 
            [ ext.group( i ,'1') for i in arr ]
            
    def extr(two:list)-> tuple: # extract:抽出
        return tuple( (I,i) for I in range(len(two)) for i in range(len(two[I])) ) # ((0, 0), (0, 1), (0, 2),  (1, 0), (1, 1))
        
class table: 
    def store(val, fram, root): #                 
        dct = ls.sort() # {'設定':'グループ設定'}
        dct[ '設定' ] = val # '設定'
        ext.store("sort.txt", dct)  
        call.wdgt.forget(root)
        cum.post(root)

    def select(vr, frame, root):  
        if ls.sort()[ '設定' ] == '全表示' :
            vr.set(0)
        elif ls.sort()[ '設定' ] == 'グループ別表示' :
            vr.set(1)
        elif ls.sort()[ '設定' ] == 'グループ設定' :
            vr.set(2)   
        fram=tk.Frame(frame)
        lf= tk.LabelFrame(fram) 
        rdo1 = tk.Radiobutton( lf, value=0,command=lambda:table.store(rdo1['text'], fram, root), font=( 'TkDefaultFont', 11 ), variable=vr, text= '全表示')   
        rdo1.pack(side='left')
        rdo2 = tk.Radiobutton( lf, value=1,command=lambda:table.store(rdo2['text'], fram, root), font=( 'TkDefaultFont', 11 ), variable=vr, text= 'グループ別表示')
        rdo2.pack(side='left')
        rdo3 = tk.Radiobutton( lf, value=2,command=lambda:table.store(rdo3['text'], fram, root), font=( 'TkDefaultFont', 11 ), variable=vr, text= 'グループ設定')
        rdo3.pack(side='left')
        lf.pack()  
        fram.pack(side='left')
        tk.Button( frame, text= '印刷' ).pack(side='left',padx=4)
        wdgt.cansell( frame, 'left', root)
      
    def scrollbar(frame, ww, wh):
        canvas = tk.Canvas( frame, width= ww, height= wh )
        ybar = tk.Scrollbar( frame, orient= "vertical" )
        ybar.pack(side="right", fill="y")
        ybar.config(command= canvas.yview)
        xbar = tk.Scrollbar(frame, orient= "horizontal")
        xbar.pack(side="bottom", fill="x")
        xbar.config(command=canvas.xview)
        canvas.config( yscrollcommand=ybar.set, xscrollcommand=xbar.set) # Canvasのサイズ変更をScrollbarに通知
        canvas.config( scrollregion= ( 0, 0, ww, wh)) #スクロール範囲
        canvas.pack( side="top", fill=tk.BOTH, expand=True, padx=5, pady=5)
        cvs = tk.Frame(canvas)
        canvas.create_window((0,0), window=cvs, anchor=tk.NW, width=0, height=0)
        canvas.bind("<MouseWheel>", lambda event:canvas.yview_scroll(int(-1*(event.delta/120)), "units") ) # .bind_allにするとtkinter.TclErrorがでる、
        return cvs
    
    def callback( event, df, root):
        info = event.widget.grid_info()
        event.widget["relief"], event.widget["activeforeground"], info['row'], info['column'] # 0 0
        top = tk.Toplevel()
        top.option_add( '*font', [ 'TkDefaultFont', 16 ])
        dct = ls.group()
        n = info['row']
        tpl = df.T.index[ n ] # ('人事院', '')
        ( df.T.index[ n ], dct.get(tpl))
        inv = tk.IntVar( top)
        inv.set( dct.get(tpl) )
        frame = tk.LabelFrame( top, text= '「' + event.widget["text"] + '」のグループ番号を設定する\n')
        spn= tk.Spinbox( frame, textvariable= inv,  width= 3, from_= 1, to= len(df.T.index), state= 'readonly', font=( 'TkDefaultFont', 24) )
        spn.pack( side="left", padx=100, pady=2)
        tk.Button( frame, text='保存', command=lambda : table.hub( tpl, spn.get(), top, root) ).pack( fill=tk.BOTH, padx=2 ,pady=2)
        frame.pack( side="left", padx=2, pady=2)
        wdgt.cansell( top, 'left', top)
        
    def hub( tpl, txt, top, root):
        ext.group( tpl, txt)
        top.destroy()
        call.wdgt.forget(root)
        cum.post(root)
                        
    def wheel( event, tub):
        if event.delta < 0:
            tub.append(event.delta)
        elif event.delta > 0 and len(tub) > 0: #
            tub.remove(event.delta*-1)
        (len(tub))
                    
    def exhibition(df):#展示
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'b': 2, 'c': 4, 'd': 5}
        key1 = d1.keys() | d2.keys()##和集合
        key2 = d1.keys() & d2.keys()##共通部分
        sorted(key1), key2
        sorted( df.index.values)
        df.T.values
        df.index.values
        df.T.cumsum()     
        df.iloc[0][0]
        df.index.values[0]   
        df.columns.values[0]
        df[ df.columns.values[0]].keys()
        df.index[0]
        ( df.T.iloc[[0, 1], [0, 1, 2]] )
        df.iloc[0][0]
        df.iat[0, 0]
        df.loc[["人事院"]]
        df.T.loc['ト']
        df['ア'].fillna(0) # Name: ア, dtype: int64
                          #  1      18
                          #  5      23
                          #  6     180
                          #  12     48
        df.loc[["人事院","弁護士会館"],["ア"]]
        df.T.loc["ア",df[ df.columns.values[0]].keys() ] 
        df.T.loc[ "ア",df.index.values[0]  ]  
        df['ア'].fillna(0)+df['ア'].fillna(0) 
        df.drop(index=['人事院']) # 省く
        df.filter(items=['ア','マ']) 
        df.filter(like='ア')  # Name: ア, dtype: int64
                              #  1      18
                              #  5      23
                              #  6     180
                              #  12     48
        df.loc[["人事院","弁護士会館","富国生命"]].sum()
        for row in df.itertuples(name=None):
            (row) 
            
class wdgt:
    def grdd( frame, df):
        lr, lc = df.index.values, df.columns.values # ['人事院' '弁護士会館' '富国生命' 'プレスセンター'] ['ト' '産' 'サ' 'ヨ' 'マ' 'ア' '工' 
        itrr, itrc = range(len(lr)), range(len(lc)) # range(0, 8) range(0, 32)
        for r , c in itertools.product( itrr, itrc): # 
            s = lc[ c ] # ト 産 サ
            tk.Label( frame, text = lr[ r ].center(5), relief= 'groove').grid( row= r + 1, column= 0, sticky= 'w') #.center(8):中央揃え
            tk.Label( frame, text = ext.gomoji( s ), font=( 'TkDefaultFont', 12), fg= ext.font_clr( None, s ), bg= ext.clr( s )).grid( row= 0, column= c + 1)
            try:
                val = round( df.loc[ df.index[ r ], s ])
                val = val if val != 0 else ''
                tk.Label( frame, text = val, font=( 'TkDefaultFont', 13), bg= 'white', relief= 'groove').grid( row = r + 1, column = c + 1)
            except ValueError: # float NaN to integer :tkinter
                tk.Label( frame, text = '', relief= 'groove' , bg= 'white').grid( row = r + 1, column = c + 1)
            tk.Label( frame, text = '総計', relief= 'groove' ).grid(row = 1 + len( lr), column= 0, pady= 7)
            try:                
                tk.Label( frame, text = round( df.cumsum()[ s ][ df.index[ r ]]), bg= 'gainsboro' ).grid( row= 1 + len(lr), column= c + 1, padx= 1,) # 累積和
            except ( IndexError, ValueError):
                pass
            
    def frame( root):
        ww, wh = root.winfo_screenwidth(), root.winfo_screenheight()
        frame = tk.Frame(root)
        frame.pack()
        r1__ = tk.Frame(frame)
        r1__.pack()            
        r2__ = tk.Frame(frame)
        r2__.pack()  
        cvs = table.scrollbar( r2__, ww, wh)
        r2__ = tk.LabelFrame( cvs, text='')
        r2__.pack( )  
        return r1__, r2__
    
    def cansell(frame, txt, root):
        btn= tk.Button(frame, text= '✕' ,command= root.destroy)
        btn.focus_set() 
        btn.bind('<Return>',lambda event:root.destroy() )
        btn.pack( side=txt ,padx=2,ipadx=2)   
        
class single:
    def main( hss, dct, root):   
        start = time.time()        
        df = pd.DataFrame( data= hss.values(), index= hss.keys(), columns= dct, dtype= object)
        
        r1__, r2__ = wdgt.frame(root)
        vr = tk.IntVar()
        table.select(vr,r1__,root)
        wdgt.grdd( r2__, df)
        root.bind( "<MouseWheel>", lambda event:table.wheel( event, []) )
        root.bind( '<2>', lambda event:root.destroy())    
        elapsed_time = time.time() - start
        ( "{0}".format(elapsed_time) + "[sec]")   
        root.mainloop()    
        
class LF(tk.LabelFrame):
    def __init__( self, frame, df, dd25, ddi, num, r, c, rs, cs):
        self.cs = cs
        self.frame = frame
        self.name ='lf' + ':r'  + str(r) + 'c' + str(c) + ':'
        super().__init__( master= frame, name= self.name, text= self.cs, labelanchor= 'se', font=( 'TkDefaultFont', 1), relief= 'groove') # 継承した親クラスのメソッドを使えるようになる、
        tk.Label( self, text= num, font=( 'TkDefaultFont', 13, 'bold'), fg= ext.font_clr(None,  cs),).pack( side= 'top')
        tk.Label( self).pack( side= 'left') if df.T.loc[ cs ].sum() < 25 else tk.Label( self, font=( 'Ink Free', 13, 'bold'), text= dd25[ rs ].get(cs), fg='darkorange', bg= 'white', relief= 'ridge' ).pack( side= 'left')
        if  df.T.loc[ cs ].sum() < 25:
            tk.Label( self).pack_forget()
        else:
            tk.Label( self, text = ddi[ rs ].get(cs), font=( 'MV Boli', 13, ), fg='darkgreen', bg= 'white').pack( side='left') 
        self.grid( row = r + 1, column = c + 1)
        self.bind("<Enter>", self.getEventEnter, )
        self.bind("<Leave>", self.getEventLeave, '+')
        
    def getEventEnter( self, event):
        ( self.winfo_name( ), self.grid_info().get('column'))
        for child in self.frame.winfo_children() :
            if child.cget('text')== self.cs :
                child.configure( bg= 'lightgray')
                child.configure( relief= 'ridge')
        for child in self.winfo_children() :
            child.configure( bg= 'white')
        
        # nametowidget()メソッドは、Tkinterのウィジェット名から対応するウィジェットオブジェクトを取得することができる
        widget = self.frame.nametowidget( self.winfo_name())
        ( bool(self.winfo_name() == self.name))        ,( self.frame.nametowidget( self.winfo_name()), widget["text"])
            
    def getEventLeave( self, event):
        for child in self.frame.winfo_children():
            if child.cget('bg') == 'lightgray':
                child.configure( bg= 'SystemButtonFace')
                child.configure( relief= 'groove')
        for child in self.winfo_children() :
            child.configure( bg= 'SystemButtonFace')
        
class group:
    def main( hss, ktvd, dct, root): 
        start = time.time()        
        #
        r1__, r2__ = wdgt.frame(root)
        vr = tk.IntVar()
        table.select(vr, r1__, root)
        ksvd = D.D_D( ls.group(), ktvd, {}) # {'1': {'ア': 24, 'マ': 22, 'ヨ': 29, 'サ': 45, '産': 17, 'ト': 16, 'A': 4,
        ksvd = { int( s if s != '' else 1):ksvd.get(s) for s in ksvd} # keyが''の場合は1に変換、
        ksvd = { str(s):ksvd.get(s) for s in sorted(ksvd)} # ソート
        df = pd.DataFrame( data= ksvd.values(), index= ksvd.keys(), columns= dct, dtype= object)
        df.fillna(0, inplace=True) # NaN対応、　「 ValueError: cannot convert float NaN to integer 」
        
        dd25, ddi = T.dtfm( df) # dataframe
        group.grdd1( r2__, df, dd25, ddi, root)
        group.grdd2( r2__, df, df.index.values, dd25, root)
        root.bind('<2>', lambda event:root.destroy())    
        elapsed_time = time.time() - start
        ("{0}".format(elapsed_time) + "[sec]")   
        root.bind("<MouseWheel>", lambda event: root.destroy() if event.delta < 0 else None  )
        root.mainloop()  

    def grdd1( frame, df, dd25, ddi, root):
        lr, lc = df.index.values, df.columns.values # ['1' '2' '3' '4' '6' '7' '8' '9'] ['ト' '産' 'サ' 'ヨ' 'マ' 'ア' '工' 
        itrr, itrc = range(len(lr)), range(len(lc)) # range(0, 8) range(0, 32)
        #
        dct = ls.group() # {('人事院', ''): '1', ('弁護士会館', ''): '2', ('富国生命', 'A'): '3',
        for r in range(len(lr)): # 
            rs= lr[ r ]  # '1' '2' '3' '4' 
            lt = [ k for k , v in dct.items() if v == rs ] # [('日比谷国際ビル', ''), ('パークフロント', '')]
            lf = tk.LabelFrame( frame)
            lbl = tk.Label( lf, text = lr[ r ], relief= 'groove', font=( 'TkDefaultFont', 14 ))
            lbl.bind('<1>', functools.partial( group.callback1, df, r ) ) 
            lbl.pack(side='left')
            for tpl in lt: #
                (tpl) # ('プレスセンター', 'A')
                f = tk.Frame( lf)
                tk.Label( f, text = tpl[0] ).pack( side='left')
                tk.Label( f, text = tpl[1], bg= None if '' == tpl[1] else 'yellow').pack( side='left') 
                f.pack()
            lf.grid( row= r + 1, column= 0, sticky= 'w' )
            
        for c , r in itertools.product(itrc,  itrr): # 
            rs, cs= lr[ r ] , lc[ c ] # '1' '2' '3' '4' # ト 産 サ
            (rs, cs,  r , c )
            lr = df.index.values # ['1' '2' '3' '4']
            tk.Label( frame, text = ext.gomoji( cs), font=( 'TkDefaultFont', 12), fg= ext.font_clr( None, cs), bg= ext.clr( cs)).grid( row= 0, column= c + 1)
            #
            num = df.loc[ df.index[ r ], cs]
            if num != 0: # 値が0なら非表示、
                LF(frame, df, dd25, ddi, num, r, c, rs, cs)
            else:                
                tk.Label( frame, text = '', relief= 'groove' ).grid( row = r + 1, column = c + 1)

    def grdd1___( frame, df, dd25, ddi, root):
        lr, lc = df.index.values, df.columns.values # ['1' '2' '3' '4' '6' '7' '8' '9'] ['ト' '産' 'サ' 'ヨ' 'マ' 'ア' '工' 
        itrr, itrc = range(len(lr)), range(len(lc)) # range(0, 8) range(0, 32)
        #
        dct = ls.group() # {('人事院', ''): '1', ('弁護士会館', ''): '2', ('富国生命', 'A'): '3',
        for r in range(len(lr)): # 
            rs= lr[ r ]  # '1' '2' '3' '4' 
            lt = [ k for k , v in dct.items() if v == rs ] # [('日比谷国際ビル', ''), ('パークフロント', '')]
            lf = tk.LabelFrame( frame)
            lbl = tk.Label( lf, text = lr[ r ], relief= 'groove', font=( 'TkDefaultFont', 14 ))
            lbl.bind('<1>', functools.partial( group.callback1, df, r ) ) 
            lbl.pack(side='left')
            for tpl in lt: #
                (tpl) # ('プレスセンター', 'A')
                f = tk.Frame( lf)
                tk.Label( f, text = tpl[0] ).pack( side='left')
                tk.Label( f, text = tpl[1], bg= None if '' == tpl[1] else 'yellow').pack( side='left') 
                f.pack()
            lf.grid( row= r + 1, column= 0, sticky= 'w' )
            
        for r , c in itertools.product( itrr, itrc): # 
            rs, cs= lr[ r ] , lc[ c ] # '1' '2' '3' '4' # ト 産 サ
            lr = df.index.values # ['1' '2' '3' '4']
            tk.Label( frame, text = ext.gomoji( cs), font=( 'TkDefaultFont', 12), fg= ext.font_clr( None, cs), bg= ext.clr( cs)).grid( row= 0, column= c + 1)
            #
            num = df.loc[ df.index[ r ], cs]
            if num != 0: # 値が0なら非表示、
                lf = tk.LabelFrame( frame)
                tk.Label( lf, text= num, font=( 'TkDefaultFont', 13, 'bold'), fg= ext.font_clr(None,  cs),).pack( side= 'top')
                tk.Label( lf).pack( side= 'left') if df.T.loc[ cs ].sum() < 25 else tk.Label( lf, font=( 'Ink Free', 13, 'bold'), text= dd25[ rs ].get(cs), fg='darkorange', bg= 'white', relief= 'ridge' ).pack( side= 'left')
                if  df.T.loc[ cs ].sum() < 25:
                    tk.Label( lf).pack_forget()
                else:
                    tk.Label( lf, text = ddi[ rs ].get(cs), font=( 'MV Boli', 13, ), fg='darkgreen', bg= 'white').pack( side='left') 
                lf.grid( row = r + 1, column = c + 1)
            else:                
                tk.Label( frame, text = '', relief= 'groove' ).grid( row = r + 1, column = c + 1)

    def grdd2( frame, df, lr, dd25, root):
        d = ls.difference() # {'サ': 2, 'ヨ': 1, 'マ': 1, 'ア': 1, }
        d = { **{ k : 0 for k in df.columns.values }, **d } # {'ト': 0, 'サ': 2, 'ヨ': 2, 'マ': 1, 'ア': 1, '東スポ': 0, 'NYT': 0, 'ゲンダイ': 0, 'フジ': 0}
        for c , s in enumerate( df.columns.values ):
            s  # ト
            lr # ['1' '4' '5' '12']
            dct = D.DD(dd25, {}) # {'ト': 175, 'サ': 350, 'ヨ': 250, 'マ': 225, 'ア': 250, '東スポ': 0, 'NYT': 0, 'ゲンダイ': 0, 'フジ': 0}
            for i, txt in enumerate(( 'アタマ', '25束', '差分', '計')):
                tk.Label( frame, text = txt, relief= 'sunken', width= 6, font=( 'TkDefaultFont', 13, ) ).grid( row = i + 1 + len( lr), column= 0, ipadx= 2 )
            #
            n = df.T.loc[ s ].sum() # 199 354 267 246 269
            tpl = ( n -dct.get( s ) + d.get(s) , dct.get( s ), d.get(s), n )
            for i, num in enumerate( tpl): #  n % 25, n // 25 * 25, n
                if i == 0 : # 
                    tk.Label( frame, text= num, font=( 'Segoe UI Symbol', 13, 'bold'), fg= 'midnightblue', bg= 'azure', relief= 'sunken' ).grid( row = i + 1 + len( lr), column= c + 1,  ipadx=2 ) if 0 != n // 25 else tk.Label().grid_forget() 
                elif i == 1 :
                    tk.Label( frame, text= num, font=( 'MV Boli', 13, ), fg= 'darkorange', bg='white', relief= 'sunken' ).grid( row = i + 1 + len( lr), column= c + 1, ipadx=2 ) if 0 < n // 25 else tk.Label().grid_forget() 
                elif i == 2 :
                    tk.Button( frame, text= num if 0 != num else '', font=( 'MV Boli', 13, 'bold' ), command= functools.partial( group.callback2,  df, d, s, root), fg= 'gray', relief= 'raised' ).grid( row = i + 1 + len( lr), column= c + 1 )
                elif i == 3 :
                    tk.Label( frame, text= num, bg= 'gainsboro', relief= 'sunken' ).grid( row = i + 1 + len( lr), column= c + 1, ipadx=2 ) 
                
    def callback1( *args ) : 
        dct = ls.group() # {('人事院', ''): '1', ('弁護士会館', ''): '2', ('富国生命', 'A'): '3',
        df, r  = args[0], args[1], 
        lr = df.index.values # ['1' '2' '3' '4']
        s = lr[ r ] # '1' '2' '3' '4'
        lt = [ k for k , v in dct.items() if v == s ] # [('日比谷国際ビル', ''), ('パークフロント', '')]
        top = tk.Toplevel()
        top.geometry('+300+150')
        top.attributes( "-alpha", 0.95) # 透過
        tk.Label( top, text = '【グループ' + s + '】', font=( 'TkDefaultFont', 13, 'bold')).grid( row= 0 , column= 0 )
        for i, tpl in enumerate(lt):
            txt0, txt1 = tpl
            tk.Label( top, text = txt0, font=( 'TkDefaultFont', 14, 'bold')).grid( row= 1 + i, column= 0 )
            tk.Label( top, text = txt1, font=( 'TkDefaultFont', 14, 'bold'),  bg= None if txt1 =='' else 'white').grid( row= 1 + i, column= 1 )
        top.after( 4000, top.withdraw)
        
    def callback2( df, d, s, root ):
        top = tk.Toplevel()
        top.geometry('+300+150')
        top.attributes( "-alpha", 0.95) # 透過
        tk.Label( top, text = '【差分】 ' + s + ' ', font=( 'TkDefaultFont', 15 )).grid( row= 1 , column= 0 )
        val = tk.IntVar() 
        val.set( 0 if d.get(s) == None else d.get( s ))   
        ins = group() # この行でインスタンス化 # TypeError: メソッドの名前 missing 1 required positional argument: 'self'
        tk.Spinbox(top, command= functools.partial( ins.update, root, s , val), textvariable= val, state = 'readonly', from_= -99, to= 99, width= 2).grid( row = 1, column= 1)
        tk.Label( top, text = '部', font=( 'TkDefaultFont', 13)).grid( row= 1 , column= 2 )
        top.after( 4000, top.withdraw)
        
    def update( self, root, s , spn): # self:「通常のメソッドではインスタンス自身が暗黙的に第一引数に渡される」
        dct = ls.difference()
        dct = { **dct, **{ s : int(spn.get())}}
        ext.write( "difference.txt", dct)
        call.wdgt.forget(root)
        cum.post(root) #

class T:
    # 新しい位置または場所に動かす、        
    def D_S_I_D( d1:dict, cs:str, n:int, d2:dict): # 送信元（source）, 送信先(destination)
        l1, l2 = d1[cs], d2[cs]
        d1 = { **d1, **{ cs: l1[n:] }}
        d2 = { **d2, **{ cs: l2 + l1[:n] }}
        return d1, d2    # 束の数、 余りを算出する。
    
    def dtfm( df)->tuple: # Dataframe
        d__ = { s : df.T.loc[ s ].sum() for s in df.columns.values} # {'ト': 199, 'サ': 357, 'ヨ': 267, 'マ': 246, 'ア': 269, '東スポ': 1, 
        (d__)
       
        for k , v in ls.difference().items(): #　差分の部数を加える、 総計に,
            d__[ k ] += v

        #　束の数 × 25, 25束区切り部数、　動的, 
        ksvl = { cs :[ 1 for i in range( d__.get(cs) // 25)] * 25 for cs in df.columns.values } # {'ト': [1, 1, 1, 1, 1, 1, 1, 1, 1, 
        atama = { cs :[ 1 for i in range( d__.get(cs) % 25 )] for cs in df.columns.values } # {'ト': [1, 1, 1, 1, 1, 1, 1, 1, 1]}
        # 用意する束の数, remainder:余り、 残余
        ({ k: len(v) for k, v in ksvl.items() },{ k: len(v) for k, v in atama.items() })
        dd25, ddi= {}, {}
        
        # 可変、動的 y:dynamic:
        ksvy = { cs: [] for cs in df.columns.values } # 
        for rs in df.index.values: # ['1' '5' '6' '12']
            d25 = {}
            for cs in df.columns.values: # ['ト', 'サ', 'ヨ', 'マ', 
                num = df.loc[ rs , cs ] # 16 
                # 用意する束がない・可変に部数がない場合、アタマの数を加える
                if num > len(ksvl.get(cs)) + len(ksvy.get(cs)) or rs == df.index.values[-1] : # or 0 == len(ksvl.get(cs)) and num > len(ksvy.get(cs)) 
                    atama, ksvy = T.D_S_I_D( atama, cs, len(atama[cs]), ksvy) # ⇒
                i = I.I_S_D_D( num, cs, ksvl, ksvy) # 用意する束の数
                d25 = { **d25, **{ cs: 25 * i }}  # 
                # 
                ksvl, ksvy = T.D_S_I_D( ksvl, cs, d25[ cs], ksvy) # ⇒
                # 
                ksvy[ cs] = ksvy[ cs][ num:] # {'ト': [1, 1, 1, 1, 1, 1, 1, 1, 1]}
            dd25 = { **dd25, **{ rs: d25 }}
            ddi[ rs ] = { k: len(v) for k, v in ksvy.items() } #  {'1': {'ト': 9, 'サ': 9, 'ヨ': 7, 'マ': 9, 'ア': 7, '東スポ': 0, 'NYT': 0, 'ゲンダイ': 0,
        return dd25, ddi # {'1': {'ト': 25, 'サ': 25, 'ヨ': 25, 'マ': 25, # {'1': {'ト': 9, 'サ': 9, 'ヨ': 7, 'マ': 9, 
            
class I:
    def I_S_D_D( num:int, cs:str, ksvl:dict, ksvy:dict )-> int :
        
        z = len(ksvy.get(cs))
        l25 = [ 25 for i in range(len(ksvl.get(cs)) // 25) ] # [25, 25, 25, 25, 25, 25, 25]
        # 部数を超えている束の残
        l = [ i+1 for i in range(len(l25)) if num < 25 * (i+1) + z ] # [1, 2, 3, 4, 5, 6, 7]
        if num <= z : # 16 <= 0
            i = 0
        elif bool(len(l)) : # 部数を超えている束の残, 有、
            i = min( l ) # 束の残, 最小,
        elif not bool(len(l)) : # 部数を超えている束の残, 無、
            i = len(l25)
        return i # 用意する束の数を返す
    
# グループ設定'
class setting:              
    def main( hss, ktvd, root): 
        root.option_add( '*font', [ 'TkDefaultFont', 14 ] )
        ww, wh = root.winfo_screenwidth(), root.winfo_screenheight()

        dct = ls.group() # 
        (ktvd) # {('人事院', ''): {'ア': 14, 'マ': 12, 'ヨ': 18, 'サ': 31, '産': 11, 'ト': 9, 'A': 2, '農業': 1}, ('弁護士会館',
        (hss)
        df = pd.DataFrame(data = ktvd, dtype=object)
        frame = tk.Frame(root)
        fram_ = tk.Frame(frame)        
        fram= tk.Frame(frame)
        vr = tk.IntVar()
        table.select( vr, fram, root) 
        if type( D.diff( df.T.index, dct, {}) ) == dict : 
            ext.store( "group.txt", D.diff( df.T.index, dct, {})) # ktvs
         
        fram.pack()
        cvs = table.scrollbar( fram_, ww, wh)
        fra__= tk.LabelFrame( cvs, text= 'グループ設定')
        cum.create( ls.customer()) # group.txtに不足している辞書があれば作成する。
        setting.gdgt( fra__, dct, df, root)
        fra__.pack() #  
        fram_.pack() 
        frame.pack( padx=5, pady=5)            
        root.bind( '<2>', lambda event: root.destroy())       
        root.mainloop()
        
    def gdgt( frame, dct, df, root):    
        (dct) # {'弁護士会館': '1', 'プレスセンター': '1', '富国生命': '1', '人事院': '1', 
        df.T.index # MultiIndex([('人事院', '') ('弁護士会館', '') ('富国生命', 'A')
        ( list(df.columns.values) == list( df.T.index) )    

        for i, tpl in enumerate( df.T.index):      
            (df.columns.values[i]==tpl) # True
            try:
                txt0, txt1 = tpl # ('人事院',  '')
                btn = tk.Button( frame, text= txt0 + ' ' + txt1, 
                                bg= None if txt1 =='' else 'gainsboro')
                btn.bind( "<1>", lambda event:table.callback( event, df, root))
                btn.grid( row= i, column = 0, ipady=1, sticky= tk.W+tk.E)
                tk.Label( frame,
                         text= 'グループ ' + dct.get(tpl) if tpl in dct else '未設定',
                         bg= None if tpl in dct else 'yellow',
                         ).grid( row= i, column=1, padx=4, ipadx=1, ipady=1, sticky= tk.W+tk.E)
            except (IndexError, ValueError): # float NaN to integer :tkinter
                pass           
        
class dr___(): # direc
    # 
    def diff( itr:iter, one:iter, hss): # 差集合：set difference
        ( itr, one)
        for l in itr:
            for k , v in one.items(): 
                if  l ==  k : 
                    hss[k] = v # hss.update({k:v})
        return hss   
    
class DT:
    def LD_L( lst, args):
        dt = { tuple( dic.get(i) for i in args ):None for dic in lst } 
        return dt # {('人事院', ''): None, ('弁護士会館', ''): None, ('富国生命', 'A'): None, 
    
class LT:
    def LD_L( lst, args, tpl):
        [( k , int( v )) for dic in lst if dic.get( args[0])== tpl[0] if dic.get( args[1])== tpl[1] for k , v in dic.items() if k not in ls.kl() ]
        [( k , int( v )) for dic in lst if len(args) == sum([ dic.get( i)== tpl[args.index(i)] for i in args]) for k , v in dic.items() if k not in ls.kl() ]
        lt = [( k , int( v )) for dic in lst if B.D_T_L( dic, tpl, args) for k , v in dic.items() if k not in ls.kl() ]
        return  lt # [('ア', 2), ('マ', 2), ('ヨ', 2), ('サ', 3), ('産', 2), ('ト', 2), ('ア', 1), ('サ', 2),

class B:
    # 任意の数の要素が等しいかboolで返す。
    def D_T_L( dic:dict, tpl:tuple, args:list)->bool:      
        tpl # '人事院', ''
        args # ['区分', '区間']   
        boolean = len(args) is sum([ dic.get(txt)== tpl[i] for i , txt in enumerate(args)])
        return boolean # True
    
class D: 
    def DD( dd , hss):
        for d in dd.values() :
            for k, v in d.items():
                hss.setdefault(k, 0)
                hss[ k ] += v
        return hss
    
    def D_D( dct:dict, ktvd:dict, dd)->dict: # transformation:変換, '二次元辞書＋辞書→二次元辞書'
        (dct) # {'人事院': '1', '弁護士会館': '1', '富国生命': '3', 'プレスセンター': '4', '厚生労働省': '5', '日比谷国際ビル': '6', 'パークフロント': '7'}
        (ktvd) # {('人事院', ''): {'ア': 14, 'マ': 12, 'ヨ': 18, 'サ': 31, '産': 11, 'ト': 9, 'A': 2,
        for txt in ktvd.keys():
            txt # '人事院'
            sn = dct.get( txt ) if txt in dct.keys() else '' # '1'
            dd.setdefault( sn, {}) 
            for s , i in ktvd[txt].items(): 
                # 'ア': 14,
                dd[ sn].setdefault( s , 0) # { i : {k: 0}}
                dd[ sn][  s ] +=  i  # { i : { k: v}}
                ( txt,  sn,  s ,  i )
        return dd # {'1': {'ア': 24, 'マ': 22, 'ヨ': 29, 'サ': 45, '産': 17, 'ト': 16, 'A': 4,
        
    def diff( itr:iter, one:iter, hss): # 差集合：set difference
        for l in itr:
            for k , v in one.items(): 
                if  l ==  k : 
                    hss[k] = v # hss.update({k:v})
        return hss   
    
class Dtd:
    def LD_L( lst, args , d_ ):
        args # ['区分', '区間'] 
        dt = DT.LD_L( lst, args) # {('人事院', ''): None, ('弁護士会館', ''): None, ('富国生命', 'A'): None, 
        for tpl in dt:
            tpl # '人事院', ''
            lt = LT.LD_L( lst, args, tpl) # [('ア', 2), ('マ', 2), ('ヨ', 2), ('サ', 3), ('産', 2), ('ト', 2), ('ア', 1), ('サ', 2),
            d = {}
            for t in lt:
                k , v = t
                d.setdefault( k , 0 )
                d[ k ] += v
            d_= { **d_,**{ tpl : d }}
        return d_ # {('人事院', ''): {'ア': 14, 'マ': 12, 'ヨ': 18, 'サ': 31, '産': 11, 'ト': 9, 'A': 2, '農業': 1}, ('弁護士会館', ''):
    
if __name__ == '__main__':  
    root = tk.Tk() 
    lst = ls.customer()
    cum.post( root)
    root.mainloop()
    cum.create#( lst)
    #
    dic = {'区分':'区分', '区間':'区間'}
    Dtd.LD_L( lst, ['区分', '区間'], {})
    bl = bool( 0 != 1)+bool( 0 != 1)
    bl = [ dic.get(i)==i for i in [ '区分', '区間']]
    ( len(['区分', '区間']) is sum(bl))

    # Ctrl+4	ブロックコメントを追加
    # Ctrl+5	ブロックコメントを削除
    # Ctrl+Shift+U	大文字に変更する
    # Ctrl+Shift+F	ファイル内を探索, 検索
    # Ctrl+Alt+Shift+←	最後に編集した箇所へ移動 
    
    # {} 波括弧:Curly(縮れた) Bracket, variable:可変,
    
    # 論理記号・論理結合子 	使い方 	意味　　　　　　
        # 連言∧	Ｐ∧Ｑ	ＰかつＱ、　かつ
        # 選言∨	Ｐ∨Ｑ	ＰまたはＱ、　または
        # 否定¬	¬Ｐ	Ｐでない、　ひてい
        # 含意→	Ｐ→Ｑ	ＰならばＱ　、ならば
        # 同値↔	Ｐ↔Ｑ	ＰはＱと同値である、　どうち
        