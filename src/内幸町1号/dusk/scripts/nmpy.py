import tkinter as tk
import pandas as pd
import math
from tkinter import ttk
import numpy as np
import ls
import ext
import cum
from pandas import DataFrame
class app(tk.Tk):
    def post(): 
        lst = ls.customer()
        keylst = ls.wd() + ls.tm()
        dic={}
        dc={}        
        for i in range(len(lst)):
            for n, ke_ in enumerate( lst[i].keys() ): 
                if ke_ not in keylst :
                    dic.setdefault( lst[i][ls.wd()[0]] ,{})
                    dic[ lst[i][ls.wd()[0]] ].setdefault(ke_,0)#( ..)φメモメモ：ネスト構造
                    dc.setdefault(ke_,0)
                    dic[ lst[i][ls.wd()[0]] ][ke_] = int(lst[i][ke_]) if ke_ not in dic[ lst[i][ls.wd()[0]] ].keys() else int(dic[ lst[i][ls.wd()[0]] ][ke_]) +  int(lst[i][ke_])
        
        dict_sorted = app.fmat(dic)
        
        return dict_sorted ,app.fm_t(dc)
    def write(lst):#
        dic={}
        for i in range(len(lst)):
            lst[i][ls.wd()[0]]
            dic[lst[i][ls.wd()[0]]]=None
        lst = [ lst[i][ ls.wd()[0]] for i in range( len( lst))] #lst = ['hey','人事院', '弁護士会館','hello', '富国生命', 'プレスセンター', '厚生労働省', '日比谷国際ビル', 'パークフロント']
        lst = list(collections.Counter(lst).keys())##順序を保持、
        grup = list(ls.group().keys())
        fls= [ lst[i] for i, ele in enumerate(lst) if ele not in grup]
        [ ext.group(ele,"1") for ele in fls]
    def fmat(dic):#format    
        key_val={}
        for i,key in enumerate( dic.keys() ):   
            key_val.setdefault( key ,{})
            for ii in range(len( ls.nw() )):                
                for iii in range(len(ls.nw()[ii])):
                    if ls.nw()[ii][iii] in dic[key].keys():
                        key_val[key].setdefault(  ls.nw()[ii][iii]  ,dic[key][ls.nw()[ii][iii]])
        return key_val
    def fm_t(dic):#format    
        key_val={}
        for ii in range(len( ls.nw() )):                
            for iii in range(len(ls.nw()[ii])):
                if ls.nw()[ii][iii] in dic.keys():
                    key_val.setdefault(  ls.nw()[ii][iii]  ,dic[ls.nw()[ii][iii]])
        return key_val
    def __init__(self):
        super().__init__()
        self.title("Display DataFrame")
        dic=app.post()[0]
        
        
        columN = list( app.post()[1].keys())    
        self.df = pd.DataFrame(data= dic, dtype=object)
        #print( self.df.T.reindex(columns=columN))    
        pd.options.display.precision = 0

        df= pd.DataFrame(data= self.df.T.reindex(columns=columN), dtype=object)
        
        style = ttk.Style()
        style.configure("mystyle.Treeview",width=40,font=("",10))        
        style.configure("mystyle.Treeview.Heading",font=('Ubuntu Light',9))#,"overstrike"
        
        print(pd.options.display.precision)
        print(math.floor(df.iloc[0][0]))
        tree = ttk.Treeview(self,style="mystyle.Treeview")
        tree.place(x=1, y=1)
        #print(df.columns)
        # 列を３列作る
        tree["column"] = df.columns
        tree["show"] = "headings"# ヘッダーテキスト
        tree.column(0, width=120)

        tub=[]
        for item in df.columns:
            tub.append(item)
            tree.heading(len(tub), text=item)#ext.gomoji(item))
            tree.column(len(tub), width=40)
        for i, item in enumerate(df.index):
            val1 = df.index[i] 
            t__ =[round(item) for item in df.T[val1].fillna(0)]  
            val2 = tuple( df.T[val1].fillna(0)  )
            val2 = tuple( t__  )
                
            v___ = (df.index[i], )+val2
            print(val2 )
            #print( t__)
            tree.insert("", "end", values=v___ )

        # データ挿入
        #for i in range(self.df.index):
            #tree.insert("", "end", values=(df['SearchTerm'][i], df['Ranking(Domain)'][i], df['Ranking(URL)'][i]))
        
        # 設置
        tree.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        note = ttk.Notebook( )
        note.pack()
        
        
if __name__ == '__main__':
    app = app()
    app.mainloop()