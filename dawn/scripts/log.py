from pathlib import Path
from ast import literal_eval
import tkinter as tk
import numpy as np
import datetime, time, shutil, os, itertools
import ls, fx, sys, ext, data, panda, nmpy, sync

# 検知:Detection

#ディレクトリ関連の操作
class dirc(): # directory:住所氏名録
    def actv(file):      # activation:有効化、活動化
        path = '../setting/' + file
        dirc.mtime( path)  # 更新日時取得
        dirc.copy( file) # # 更新日時をファイル名にしてコピーする。
        dirc.srt()       # ファイル更新日時順にソート   
        dirc.limit()     # ファイル数上限を設定する。  
        
    # 更新日時取得
    def mtime(path): 
        t = os.path.getmtime(path) # 1574851066.421054
        d = datetime.datetime.fromtimestamp(t) # 2019-11-27 19:37:46.421054
        s = d.strftime('%Y%m%d%H%M%S') # 20191127193746
        d.year
        return s
    
    # 更新日時をファイル名にしてコピーする。
    def copy( file:str):
        path = ix.ky()['../setting/'] + file
        new_path = shutil.copyfile( path, ix.ky()['../log/'] + dirc.mtime(path) + '.txt') # 更新日時をファイル名にしてコピーする。
        new_path # '../log/20211004131746.txt'
                
    def review(): # review： 概要　# ファイル毎のメタ情報で辞書を作成する。{'20211008173135.txt': [1633865625.8773737, '20211010203345']}
        ph = ix.ky()['../log/']
        lis = os.listdir(ph)
        dct = {}
        for item in lis:
            (item)
            path = ph + item
            t = os.path.getmtime(path) # 1574851066.421054
            d = datetime.datetime.fromtimestamp(t) # 2019-11-27 19:37:46.421054
            s = d.strftime('%Y%m%d%H%M%S') # 20191127193746
            dct[item]=[ t, s]
        l = [ i for i in dct.values()]
        fx.l.t( dct)        
        fx.l.t( l)
        fx.l.t( l.index(min(l))) # 更新時間が最も古い、ファイルの、リストのインデックスを返す

    # ファイル数上限を設定する。    
    def limit(): 
        threshold = 10 # threshold:しきい値
        while len( os.listdir(ix.ky()['../log/'])) > threshold : #
            lis = dirc.srt()
            path = ix.ky()['../log/'] + lis[0]
            dirc.rmve( path) # ファイルを削除
            fx.l.u( dirc.srt()[0])
    
    def rmve(path): # remove:削除
        try:
            os.remove( path) # ファイルを削除
        except FileNotFoundError as e: # FileNotFoundErrorは例外クラス名
           print("ファイルが見つかりません", e)
        except Exception as e: # Exceptionは、それ以外の例外が発生した場合
           print(e)
           
    # ファイル更新日時順にソート                
    def srt(): # sort　
        # pathlibモジュール:フォルダのパスをオブジェクトとして操作・処理できる。
        paths = list(Path('../log/').glob(r'*.txt')) # パターンにマッチするパス名を取得する
        paths.sort( key=os.path.getmtime, reverse=False) # ファイル更新時間順にソート
        return [ file.name for file in paths]
    
    # Memorandum:忘備録
    def Memorandum(): 
        fx.l.u(datetime.datetime.now(), # 2019-11-27 19:37:46.421054
               datetime.datetime.now().strftime('%Y%m%d%H%M%S'), # 20191127193746
               os.listdir(ix.ky()['../log/']) ) 
        
        fx.l.u(os.path.exists('../setting/'),
                os.path.exists(ix.ky()['../log/']))
        
class ix(): #index
    def ky()-> dict:
        return { '../setting/':'../setting/', 'customer.txt':'customer.txt', '../log/': '../log/', 'ファイル名':os.path.basename(__file__)}

class anlys(): # 数値,analysis:解析,
    def num( lst:list, dct:dict)->dict: # 内包表記にしても処理時間に差はない。
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        for i in range(len(lst)):
            for k, v in lst[i].items(): 
                if k not in ls.kl():
                    dct.setdefault( k, 0)
                    dct[ k] += int( v)
        return dct # dct {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, 'ショッピング': 1, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, '流通': 15, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}
    
    def customer(path):
        file = path #
        with open(file, "r", encoding = 'utf-8') as f:
            data_list = f.read()        
        text = data_list.replace(" ","")
        lst = literal_eval(str(text))#文字列をリストや辞書に変換
        return lst
    
    # 新聞名一覧をタプルで取得。ト➡ア
    def nw()-> tuple:  # news paper
        tpl = ls.nw() # tuple, 二次元
        zero = tuple(reversed(tpl[0]))
        other = tpl[1:] # それ以外
        return zero + anlys.extr(other) # ('ト', '産', 'サ', 'ヨ', 'マ', 'ア', '工', '日産', 
    
    # 二次元配列から要素の抽出
    def extr(two:tuple)-> tuple: # extract:抽出
        return tuple( i for I in range(len(two)) for i in two[I] )
        
class wdgt(): # 
    def actv( root):
        if len(os.listdir('../log/')) >= 2 : # ファイルが二個以上存在しないと履歴を表示しない。
            start = time.time()  
            lis = dirc.srt()
            two = {} # Two dimensions:二次元(辞書)
            ( os.listdir('../log/'), len(os.listdir('../log/')))
            for txt in lis:
                path = '../log/' + txt
                lst = anlys.customer( path)
                two[ txt] = anlys.num(lst,{}) 
            wdgt.table( two, lst, root)
            elapsed_time = time.time() - start
            ("{0}".format(elapsed_time) + "[sec]")   
    
    def table( two, lst, root):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        start = time.time()  
        sub = root
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.title( str(sync.dr.area()) + ' ' + "更新履歴") 
        sub.geometry( ls.ge(ww,wh) )
        sub.option_add( '*font', 'TkDefaultFont' + ' ' +  ls.ft()[0] ) # ls.ft()[2]
        
        sub.bind("<MouseWheel>", lambda event: sub.destroy() if event.delta < 0 else None  )
        
        frame= tk.Frame(sub) #
        frame.pack() 
        fra__= tk.Frame(frame)   
        fra__.pack(side="bottom")       
        fram_= tk.Frame(frame) 
        fram_.pack()   
        cvs = panda.table.scrollbar( fram_, ww, wh)
        lf= tk.Frame(cvs)  
        lf.pack()  
        wdgt.grdd( lf, two )
        gdgt.cancel( fra__, sub)
        elapsed_time = time.time() - start
        print ("{0}".format(elapsed_time) + "[sec]")   
        sub.mainloop()
        
    # gridタイプのwidgetを生成
    def grdd( lf, two):
        (two) # {'20220530173607.txt': {'ア': 271, 'マ': 247, 'ヨ': 270, 'サ': 355, '産': 181, 'ト': 203,
        
        z = list(two.keys())[-1] # 20220610173900.txt
        dct = nmpy.D.DD( two)
        keys =   dct['keys'] # ['20220530173607.txt', '20220530174854.txt', '20220530175017.txt']
        l =      dct['nw'] # ['産', 'マ', 'ア', '工', '鉄鋼']
        ndarr =  dct['nparray'] # array([[ 0,  1,  1,  0,  0], [ 0,  0,  0,  1, -1],])
        iR, iC = dct['np.shape'] # (6, 5)
        
        # 行 
        for r, line in enumerate( keys): # 二次元辞書  
            ( r, line) # '20220530173607.txt'
            txt = "{1}月{2}日{3}時{4}分".format(line[:4],line[4:6],line[6:8],line[8:10],line[10:12],line[12:14])
            tk.Label( lf, text= txt, relief="groove").grid( row= r + 1, column= 0) if r != 0 else tk.Label().grid_forget()  #　行
        # 列    
        for c, txt in enumerate( l ):
            tk.Label( lf, text= ext.gomoji( txt), relief= "groove", fg= ext.font_clr( None, txt), bg= ext.clr( txt)).grid( row= 0, column= c + 1)
            tk.Label( lf, text= two[ z ].get( txt, 0), relief= "groove", bg= 'whitesmoke' ).grid( row= len(two) + 1, column= c + 1 )
        # セル
        for r, c in itertools.product( range(iR), range(iC) ):
            digi = ndarr[ r ][ c ] # digital: 計数型の 数字の
            tk.Label( lf, text= '' if digi == 0 else digi, relief= "groove", fg= "black" if digi >= 0 else "red", bg= "white").grid( row= r + 2, column= c +1) 
        #
        
class gdgt(): # 数値,analysis:解析,
    def actv( root):
        if len(os.listdir('../log/')) >= 2 : # ファイルが二個以上存在しないと履歴を表示しない。
            start = time.time()  
            lis = dirc.srt()
            two = {} # Two dimensions:二次元(辞書)
            ( os.listdir('../log/'), len(os.listdir('../log/')))
            for txt in lis:
                print(txt)
                path = '../log/' + txt
                lst = anlys.customer(path)
                two[ txt] = anlys.num(lst,{}) 
            gdgt.table( two, lst, root)
            elapsed_time = time.time() - start
            ("{0}".format(elapsed_time) + "[sec]")   

    def table( two, lst, root):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        start = time.time()  
        sub = root
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.title("履歴") 
        sub.geometry( ls.ge(ww,wh) )
        sub.option_add( '*font', 'TkDefaultFont' + ' ' + "10" ) # ls.ft()[2]
        sub.bind("<MouseWheel>", lambda event: sub.destroy() if event.delta < 0 else None  )
        
        frame= tk.Frame(sub) #
        frame.pack() 
        fra__= tk.Frame(frame)   
        fra__.pack(side="bottom")       
        fram_= tk.Frame(frame) 
        fram_.pack()   
        cvs = panda.table.scrollbar( fram_, ww, wh)
        lf= tk.Frame(cvs)  
        lf.pack()  
        gdgt.roop( lf, two, {}, lst)
        gdgt.cancel( fra__, sub)
        elapsed_time = time.time() - start
        print ("{0}".format(elapsed_time) + "[sec]")   
        sub.mainloop()
        
    def roop( lf, two:dict, dct:dict, lst):
        two # {'20220530173607.txt': {'ア': 271, 'マ': 247, 'ヨ': 270, 'サ': 355, '産': 181, 'ト': 203,
        nw = anlys.nw()  # ('ト', '産', 'サ', 'ヨ', 'マ', 'ア', '工', '日産',  :news paper
        for r, line in enumerate( two.keys()): # 
            ( r, line) # 0 20220530095706
            dct[ line] = int( line[:14]) # {'20220530095706.txt': 20220530095706,
            i0 =  int( line[:14]) # 20220530095706
            arr = [ v for k,v in dct.items() if i0 > v ] # [20220530095706, 20220530095738, 20220601153918]
            if  len(arr) >= 1:
                iMax = max(arr) 
                txt = "{1}月{2}日{3}時{4}分".format( line[:4], line[4:6], line[6:8], line[8:10], line[10:12],line[12:14]) #.replace(".txt","")
                tk.Label( lf, text= txt, relief= "groove").grid( row= r + 1, column= 0 ,pady=2) if r != 0 else tk.Label().grid_forget()  #　行
                gdgt.calc( lf, two, r, str(i0)+'.txt', str(iMax)+'.txt' ,lst) 
        
    def calc( lf, two:dict, r:int, s0, sMax, lst )-> int:
        two # {'20220530173607.txt': {'ア': 271, 'マ': 247, 'ヨ': 270, 'サ': 355, '産': 181, 'ト': 203,
        r   # 0
        s0  # '20220530173607.txt', 
        sMax  # '20220530174854.txt'
        # 対称差集合,  symmetric:対称的, difference:差分    dfrnc
        st = set( two[ s0].items()) ^ set(two[ sMax].items()) # {('埼玉建設', 1)} {('日本証券', 1)} , set_tpl
        ( two[  s0].items())
        ( set(two[  s0].items()), set(two[  sMax].items()))
        ( st, bool( st ), dict(st).keys(), )
        arr = [ i for I in ls.reverse() for i in I ]
        x = list(two.keys())[-1] # 20220610173900.txt
        for txt in dict(st).keys():
            ( txt, arr.index(txt))
            #
            lis = [ two[ sMax].get( txt, 0), two[ s0].get( txt, 0)]
            li = np.array(lis)
            l = np.diff( lis)
            i0 = two[ s0].get( txt, 0)
            iMax =two[ sMax].get( txt, 0)
            print(-i0 + iMax, i0 - iMax ,l)
            
            #
            c = arr.index(txt)  # 6              
            tk.Label( lf, text= ext.gomoji(txt), relief= "groove", fg= ext.font_clr( None, txt), bg= ext.clr( txt)).grid( row= 0, column= c + 1)
            ( two[ s0].get( txt, 0), two[ sMax].get( txt, 0), two[ s0].get( txt, 0)-two[ sMax].get( txt, 0) )
            ky = two[ s0].get( txt, 0)- two[ sMax].get( txt, 0)
            tk.Label( lf, text= ky, relief= "groove", fg= "black" if str(ky).isdigit() else "red" , bg= "white").grid( row= r + 1, column= c + 1) #if c != 0 else tk.Label().grid_forget()  
            tk.Label( lf, text= two[x].get( txt,0), relief= "groove", bg= 'whitesmoke' ).grid( row= len(two) + 1, column= c + 1 )

    def cancel(frame, sub):
        cancel = tk.Button( frame, text= "閉じる", command= sub.destroy, width=8)
        cancel.bind('<FocusOut>', lambda event: sub.destroy())
        cancel.bind('<Return>', lambda event: sub.destroy())
        cancel.pack( padx=2 ,pady=2)
        cancel.focus_force()  
    
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。    

    anlys.num#(ls.customer())
    wdgt.actv( tk.Tk())   
    gdgt.actv#( tk.Tk())
    
    path = ix.ky()['../setting/'] + ix.ky()['customer.txt'] 
    dirc.actv#('customer.txt')
    dirc.Memorandum
    dirc.srt
    dirc.mtime#( path)
    dirc.copy#(ix.ky()['customer.txt'] )
    dirc.review#()

    d1 ={'ア':2,'サ':4}
    d2 ={'ア':2,'サ':1}
    (set(d1.items()))
    (set(d1.items()) - set(d2.items()))
    (set(d1.items()) ^ set(d2.items())) # 対称差集合
    
    ([ ls.nw()[0][::-1] , *ls.nw()[1:] ]) # [['ト', '産', 'サ', 'ヨ', 'マ', 'ア'], ['工', '日産',

