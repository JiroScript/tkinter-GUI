import pandas as pd
import tkinter as tk
import itertools
import os.path
import os
import ls
import sys
import ext
import time

class cum(ls.sp): # Cumulative:総計 
    def __del__(self):
        pass # print("killing me")
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #  
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        sub = ee_
        sub.title("【部数】")
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        sub.option_add( '*font', [ 'TkDefaultFont', 13 ] )
        lst = ls.customer()
        keylst = ls.kl()
        dic,dc = {},{}        
        for i in range(len(lst)):
            for  ky in lst[i].keys() : 
                if ky not in keylst:
                    dic.setdefault( lst[i][ls.kb()] ,{})
                    dic[ lst[i][ ls.kb()] ].setdefault( ky,0)#( ..)φメモメモ：ネスト構造
                    dc.setdefault(ky,0)
                    dic[ lst[i][ls.kb()]][ky] = int(lst[i][ky]) if ky not in dic[ lst[i][ls.kb()] ].keys() else int(dic[ lst[i][ls.kb()]][ky]) +  int(lst[i][ky])
        dict_sorted = cum.fmat(dic)
        cum.sepa(dict_sorted, dc, ee_)
            
    def sepa( dct, dc, ee_):
        if ls.sort()[ ls.cm()[0] ] == ls.cm()[1] :
            table(0, dct, cum.fm_t(dc), None, ee_).single()
        elif ls.sort()[ ls.cm()[0] ] == ls.cm()[2] :
            table(0, dct, cum.fm_t(dc), None, ee_).group()
        elif ls.sort()[ ls.cm()[0] ] == ls.cm()[3] :
            table(0, dct, cum.fm_t(dc), None, ee_).setting()
            
    #　辞書が足りない、作成する、１、グループ
    def cret( lst): # create:作成
        arr = cum.ki( lst, ls.kb())
        grup = ls.group().keys()
        fls= [ i for i in arr if i not in grup]
        if len(fls) > 0 : [ ext.group( i ,"1") for i in fls]
        
    # keyの抽出    
    def ki( lst:iter, ky:str)->iter: # key
        hss = { dic[ ky]: None for dic in lst } # {'人事院': '1', '弁護士会館': '1', '富国生命': '4', 'プレスセンター': '3', '厚生労働省': '5', '日比谷国際ビル': '6', 'パークフロント': '4'}
        return  hss.keys() 
        
    # 整列する。ト⇨ア
    def fmat(dic):
        ky_vl = {}        
        two = cum.revers() # [['ト', '産', 'サ', 'ヨ', 'マ', 'ア'], ['工', '日産', '流通', 'ヴェリタス', 'フジサンケイ・ビジネスアイ']]
        for ky in dic.keys() :   
            ky_vl.setdefault( ky ,{})
            for I, i in cum.extr(two) :
                if two[I][i] in dic[ky].keys():
                    ky_vl[ky].setdefault( two[I][i], dic[ky][two[I][i]])
        return ky_vl # {'人事院': { 'サ': 31}, '弁護士会館': {'ト': 7, '産': 7}}
    
    def fm_t(dic)-> dict:#format     
        # {'ア': 0, 'マ': 0, 'ヨ': 0, 'サ': 0, '産': 0, 'ト': 0 }
        dct = {}
        two = cum.revers() # [['ト', '産', 'サ', 'ヨ', 'マ', 'ア'], ['工', '日産', '流通', 'ヴェリタス', 'フジサンケイ・ビジネスアイ']]
        for I,i in cum.extr(two) :
                if two[I][i] in dic.keys():
                    dct.setdefault(  two[I][i], None)
        return dct # {'ト': None, '産': None, 'サ': None, 'ヨ': None, 'マ': None}
    
    def fm__(dic)-> dict:#format      
        dct = {}
        two = cum.revers() # [['ト', '産', 'サ', 'ヨ', 'マ', 'ア'], ['工', '日産', '流通', 'ヴェリタス', 'フジサンケイ・ビジネスアイ']]
        for I,i in cum.extr(two) :
                if two[I][i] in dic.keys():
                    dct.setdefault(  two[I][i], 0)
                    dct[ two[I][i]] += dic[two[I][i]]
        return dct
    
    def extr(two:list)-> tuple: # extract:抽出
        return tuple( (I,i) for I in range(len(two)) for i in range(len(two[I])) ) # ((0, 0), (0, 1), (0, 2),  (1, 0), (1, 1))
    
    def revers():#format    
        zero =list(reversed(ls.nw()[0]))
        lis = [ list(zero)] + (list(ls.nw()))[1:]
        return lis # [['ト', '産', 'サ', 'ヨ', 'マ', 'ア'], ['工', '日産', '流通', 'ヴェリタス', 'フジサンケイ・ビジネスアイ']]
    
class table(ls.sp): 
    def trace_(*args):
        type(args),args,args[2]
    def store(val, fram, sub):#                 
        dct = ls.sort() # {'設定':'グループ設定'}
        dct[ ls.cm()[0] ] = val # '設定'
        ext.store("sort.txt" ,dct)         
        table.dele(fram, sub)
        cum( None, None, None, None, sub).post()

    def select(vr, frame, sub):  
        if ls.sort()[ ls.cm()[0] ] == ls.cm()[1] :
            vr.set(0)
        elif ls.sort()[ ls.cm()[0] ] == ls.cm()[2] :
            vr.set(1)
        elif ls.sort()[ ls.cm()[0] ] == ls.cm()[3] :
            vr.set(2)   
        fram=tk.Frame(frame)
        lf=tk.LabelFrame(fram) 
        rdo1 = tk.Radiobutton(lf, value=0,command=lambda:table.store(rdo1['text'], fram, sub), variable=vr, text= ls.cm()[1])   
        rdo1.pack(side='left')
        rdo2 = tk.Radiobutton(lf, value=1,command=lambda:table.store(rdo2['text'], fram, sub), variable=vr, text= ls.cm()[2])
        rdo2.pack(side='left')
        rdo3 = tk.Radiobutton(lf, value=2,command=lambda:table.store(rdo3['text'], fram, sub), variable=vr, text= ls.cm()[3])
        rdo3.pack(side='left')
        lf.pack()  
        fram.pack(side='left')
        cansell = tk.Button(frame, text='✕' ,command = sub.destroy)
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack(side='left',padx=2,ipadx=2)
        
    def single(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #     
        start = time.time()        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        sub = ee_
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        column = list( cc_.keys())
        df = pd.DataFrame(data= bb_, dtype=object)
        df = pd.DataFrame(data= df.T.reindex(columns=column), dtype=object)
        
        frame = tk.Frame(sub)
        fram_ = tk.Frame(frame)
        fra__= tk.LabelFrame(fram_)###  
        fra__.pack(  ipadx=1)
        val = tk.IntVar(sub)
        val.trace("w" ,lambda uno,duo,tres:None)#lBL2.configure( text = ext.list_index( enr6_val.get() ,lst) ))                
        fram=tk.Frame(frame)
        vr = tk.IntVar()
        vr.trace("w",table.trace_)
        table.select(vr,fram,sub)
        fram.pack()            
        cvs = table.scrollbar(fram_,ww, wh)
        fra__ = tk.LabelFrame(cvs)  
        fra__.pack(  ipadx=1)  #_forget#
        fram_.pack()  
        fram_ = tk.Frame(frame)
        fram_.pack( padx=2)
        frame.pack()
        
        table.roop( fra__, df)
        
        sub.bind("<MouseWheel>", lambda event:table.wheel( event,[]) )
        sub.bind('<2>', lambda event:sub.destroy())    
        elapsed_time = time.time() - start
        ("{0}".format(elapsed_time) + "[sec]")   
        sub.mainloop()    
        
    def roop(fra__, df):
        rows = range(len(df.index.values))
        columns = range(len(df.columns.values))
        col = df.columns
        for r, c in itertools.product( rows, columns):##for分で回すにはイテレータである必要がある  
            
            tk.Label( fra__, text = ext.gomoji(col[c]), fg= ext.font_clr(None, col[c]), bg= ext.clr(col[c])).grid( row= 0, column= c+1)#value[c]
            tk.Label( fra__, text = df.index.values[r].center(5), relief="groove").grid( row=r+1, column=0, sticky="w") #.center(8):中央揃え
            try:
                val = round( df.loc[ df.index[r],col[c]])
                val = val if val != 0 else ""
                tk.Label( fra__, text = val , bg= "white", relief="groove").grid( row = r+1, column = c+1)
            except ValueError:#float NaN to integer :tkinter
                tk.Label( fra__, text = '', relief="groove" , bg= "white").grid( row = r+1, column = c+1)
            tk.Label( fra__, text = "総計", relief = "groove" ).grid(row = 1+len(df.index.values), column=0,pady=7)
            try:                
                tk.Label( fra__, text = round(df.cumsum()[col[c]][df.index[r]]) ,bg="gainsboro" ).grid(row=1+len(df.index.values), column=c+1)#累積和
            except (IndexError, ValueError):
                pass
            
    def group(self):        
        aa_ = self.a #
        bb_ = self.b # {'人事院': {'ト': 10, '産': 12} '弁護士会館': {'ト': 7, '産': 7}}  
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #     
        start = time.time()        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        sub = ee_
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        
        frame = tk.Frame(sub)
        fram_ = tk.Frame(frame)
        fra__ = tk.LabelFrame(fram_)###                
        fram = tk.Frame(frame)
        vr = tk.IntVar()
        vr.trace("w",table.trace_)
        table.select(vr, fram, sub)
        fram.pack()            
        cvs = table.scrollbar( fram_, ww, wh)
        fra__ = tk.LabelFrame(cvs)
        fra__.pack(  ipadx=1)  #
        fram_.pack()  
        fram_ = tk.Frame(frame)
        fram_.pack( padx=2)
        frame.pack()
        d__= table.trns( ls.group(), bb_) # {'人事院': {'ト': 10, '産': 12} '弁護士会館': {'ト': 7, '産': 7}} ➡ {'1': {'ト': 10, '産': 12} '3': {'ト': 7, '産': 7}} 
        
        column = list( cc_.keys())
        df = pd.DataFrame( data= d__, dtype=object)
        df = pd.DataFrame( data= df.T.reindex(columns=column), dtype=object)
        
        table.roop( fra__, df)
        sub.bind('<2>', lambda event:sub.destroy())    
        elapsed_time = time.time() - start
        ("{0}".format(elapsed_time) + "[sec]")   
        sub.mainloop()  
        
        
    def trns( dic:dict, two:dict)->dict: # transformation:変換, '二次元辞書＋辞書→二次元辞書'
        duo = {} 
        for key in two.keys():
            pare = table.coll( key, dic) # 親
            duo.setdefault( pare, {}) 
            (pare)
            for chld, val in two[key].items(): # 子, 値
                duo[ pare].setdefault( chld, 0) # {val: {k: 0}}
                duo[ pare][ chld] += val # {val: { k: v}}
                ( key,  pare, chld, val)
        return duo # {'1': {'産': 19} }
    
    def coll( key:str, dic:dict)->str: # collation:照合
        if key in dic.keys(): # キーに含まれていれば値を返す。
            return dic.get( key)
      
    def setting(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #  
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        sub = ee_
        sub.option_add( '*font', "TkDefaultFont" +' '+ ls.ft()[1])
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight() 
        dic = ls.group()# 
        df = pd.DataFrame(data = bb_, dtype=object)
        rowS = range( len( df.T.index) )
        frame = tk.Frame(sub)
        fram_ = tk.Frame(frame)        
        fram=tk.Frame(frame)
        vr = tk.IntVar()
        vr.trace("w",table.trace_)
        
        table.select(vr,fram,sub) 
        if type( dr.difr( df.T.index, dic) ) == dict : ext.store( "group.txt", dr.difr( df.T.index, dic))#ext.store( "group.txt", dr.difr( itr, two, ls.kb())) # 差集合を配列内辞書で返す
         
        fram.pack()
        cvs = table.scrollbar(fram_,ww, wh)
        fra__= tk.LabelFrame(cvs, text="グループ設定")##  
        cum.cret( ls.customer()) # group.txtに不足している辞書があれば作成する。
        table.sngl( fra__, rowS, dic, df, ee_)
        fra__.pack( ipadx=5,ipady=5) #  
        fram_.pack() 
        frame.pack()            
        sub.bind('<2>', lambda event:sub.destroy())       
        sub.mainloop()
        
    def sngl( frame, itr:iter, dic, df, sub):    
        for i in itr:            
            try:
                btn = tk.Button( frame,text=df.columns.values[i] )
                btn.bind( "<1>", lambda event:table.callback( event, df, sub))
                btn.grid( row= i, column = 0, ipady=1)
                tk.Label( frame, text= "グループ" + str(dic[df.columns.values[i]]),).grid( row= i, column=1, ipadx=2, ipady=2)
            except (IndexError, ValueError):#float NaN to integer :tkinter
                pass           
        
    def hub( key:str, num:int, top, sub):
        ext.group( key, num)
        table.dele(  top, sub)
        cum( None, None, None, None, sub).post()

    def scrollbar(frame,ww, wh):
        canvas = tk.Canvas(frame, width=ww, height=wh)
        ybar = tk.Scrollbar(frame, orient="vertical")
        ybar.pack(side="right", fill="y")
        ybar.config(command= canvas.yview)
        xbar = tk.Scrollbar(frame, orient="horizontal")
        xbar.pack(side="bottom", fill="x")
        xbar.config(command=canvas.xview)
        canvas.config(yscrollcommand=ybar.set, xscrollcommand=xbar.set) # Canvasのサイズ変更をScrollbarに通知
        canvas.config(scrollregion=(0,0,ww,wh/2)) #スクロール範囲
        canvas.pack( side="top", fill=tk.BOTH, expand=True, padx=5, pady=5)
        cvs = tk.Frame(canvas)
        canvas.create_window((0,0), window=cvs, anchor=tk.NW, width=0, height=0)
        canvas.bind("<MouseWheel>", lambda event:canvas.yview_scroll(int(-1*(event.delta/120)), "units") ) # .bind_allにするとtkinter.TclErrorがでる、
        return cvs
    
    def callback( event, df, sub):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        event.widget["relief"]
        event.widget["activeforeground"]
        info = event.widget.grid_info()
        info['row'], info['column']#-
        
        top = tk.Toplevel()
        top.option_add( '*font', "TkDefaultFont" +' '+ ls.ft()[1])
        val = tk.IntVar( top)
        dic = ls.group()
        key = event.widget["text"]
        inT = dic[key]
        columnS = df.columns.values
        val.set(inT)
        fram_ = tk.LabelFrame(top,text='「'+event.widget["text"]+'」'+"\nのグループ番号を設定する")
        spn = tk.Spinbox( fram_, textvariable= val,  width=3, from_= 1,to= len(columnS), state = 'readonly' , font=("TkDefaultFont",ls.ft()[0]) )
        spn.pack(side="left", padx=4 ,pady=2)
        tk.Button( fram_,text="保存", command=lambda: table.hub( key, spn.get(), top, sub) ).pack(side="left", padx=2 ,pady=2)#side="left"
        fram_.pack(side="left", padx=2 ,pady=2)
        
        cansell = tk.Button(top, text="キャンセル" ,command = top.destroy)
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:top.destroy() )
        cansell.pack_forget()#(side="left", padx=2 ,pady=2)
                
    def dele( top, sub): # delete
        top.destroy()
        children = sub.winfo_children() 
        for child in children:
            child.destroy()         
        
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
        #print( df.T.iloc[[0, 1], [0, 1, 2]] )
        df.iloc[0][0]
        df.iat[0, 0]
        df.loc[["人事院"]]
        df['ア'].fillna(0)
        df.loc[["人事院","弁護士会館"],["ア"]]
        df.T.loc["ア",df[ df.columns.values[0]].keys() ] 
        df.T.loc[ "ア",df.index.values[0]  ]  
        df['ア'].fillna(0)+df['ア'].fillna(0) 
        df.drop(index=['人事院'])
        df.filter(items=['ア','マ']) 
        df.filter(like='ア') 
        df.loc[["人事院","弁護士会館","富国生命"]].sum()
        
class dr(): # direc
    # 辞書同士の差集合を辞書で返す。共通する要素を返す。
    def difr( itr:iter, one:iter, hss= {}): # 差集合：set difference
        ( itr, one)
        for l in itr:
            for k,v in one.items(): 
                if  l ==  k : hss[k] = v#hss.update({k:v})
        return hss   
    
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    #table(0,0,0,0,root).post()
    lst = ls.customer()
    cum.cret( lst)
    cum(None,None,None,None,root).post()
    root.mainloop()
