import pandas as pd
import tkinter as tk
import itertools
from collections import defaultdict
import collections
import os.path
import os
import ls
import sys
import ext
import time
class cum(ls.sp): #Cumulative:総計 
    def __del__(self):
        pass#print("killing me")
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
        sub.option_add( '*font', 'TkDefaultFont'+' '+ ls.ft()[2])##YuGothic
        lst = ls.customer()
        cum.write(lst)
        keylst = ls.kl()
        dic={}
        dc={}        
        for i in range(len(lst)):
            for  ky in lst[i].keys() : 
                if ky not in keylst:
                    dic.setdefault( lst[i][ls.kb()] ,{})
                    dic[ lst[i][ ls.kb()] ].setdefault( ky,0)#( ..)φメモメモ：ネスト構造
                    dc.setdefault(ky,0)
                    dic[ lst[i][ls.kb()]][ky] = int(lst[i][ky]) if ky not in dic[ lst[i][ls.kb()] ].keys() else int(dic[ lst[i][ls.kb()]][ky]) +  int(lst[i][ky])
        
        dict_sorted = cum.fmat(dic)
        if ls.sort()[ ls.cm()[0] ] == ls.cm()[1] :
            table(0,dict_sorted,cum.fm_t(dc),0,ee_).single()
        elif ls.sort()[ ls.cm()[0] ] == ls.cm()[2] :
            table(0,dict_sorted,cum.fm_t(dc),0,ee_).group()
        elif ls.sort()[ ls.cm()[0] ] == ls.cm()[3] :
            table(0,dict_sorted,cum.fm_t(dc),0,ee_).setting()
    def write(lst):#
        dic={}
        for i in range(len(lst)):
            lst[i][ls.kb()]
            dic[lst[i][ls.kb()]]=None
        lst = [ lst[i][ ls.kb()] for i in range( len( lst))] #lst = ['hey','人事院', '弁護士会館','hello', '富国生命', 'プレスセンター', '厚生労働省', '日比谷国際ビル', 'パークフロント']
        lst = list(collections.Counter(lst).keys())##順序を保持、
        grup = list(ls.group().keys())
        fls= [ lst[i] for i, ele in enumerate(lst) if ele not in grup]
        [ ext.group(ele,"1") for ele in fls]
    def fmat(dic):#format 
        key_val={}        
        lis = cum.revers()
        for key in dic.keys() :   
            key_val.setdefault( key ,{})
            for ii in range(len( lis )):                
                for iii in range(len(lis[ii])):
                    if lis[ii][iii] in dic[key].keys():
                        key_val[key].setdefault(  lis[ii][iii]  ,dic[key][lis[ii][iii]])
        return key_val
    def fm_t(dic):#format    
        key_val={}
        lis = cum.revers()
        for ii in range(len( lis )):                
            for iii in range(len(lis[ii])):
                if lis[ii][iii] in dic.keys():
                    key_val.setdefault(  lis[ii][iii]  ,None)
        #print(key_val)
        return key_val
    
    def revers():#format    
        lis = ls.nw()
        zero =list(reversed(ls.nw()[0]))
        lis = [ list(zero)] + (list(lis))[1:]
        return lis        
    
class table(ls.sp): 
    def trace_(*args):
        type(args),args,args[2]
    def store(val, fram, sub):#                 
        dct = ls.sort()  
        dct[ ls.cm()[0] ] = val
        ext.store("sort.txt" ,dct)         
        table.reflexion(sub, fram)
        
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
        cansell = tk.Button(frame, text="戻る" ,command = sub.destroy)
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
        columN = list( cc_.keys())
        df = pd.DataFrame(data= bb_, dtype=object)
        df = pd.DataFrame(data= df.T.reindex(columns=columN), dtype=object)
        rowS = range( len( df.index) )
        columNS = range( len( df.columns) )
        frame = tk.Frame(sub)
        fram_ = tk.Frame(frame)
        fra__= tk.LabelFrame(fram_)###  
        val = tk.IntVar(sub)
        val.trace("w" ,lambda uno,duo,tres:None)#lBL2.configure( text = ext.list_index( enr6_val.get() ,lst) ))                
        fram=tk.Frame(frame)
        vr = tk.IntVar()
        vr.trace("w",table.trace_)
        table.select(vr,fram,sub)
        fram.pack()            
        cvs = table.scrollbar(fram_,ww, wh)

        fra__ = tk.LabelFrame(cvs)  
        for r, c in itertools.product( rowS, columNS):##for分で回すにはイテレータである必要がある  
            tk.Label( fra__, text=ext.gomoji(columN[c]), bg= ext.clr(columN[c])).grid(row= 0, column= c+1)#value[c]
            tk.Label( fra__, text=df.index.values[r], bg="lightgray").grid(row=r+1, column=0,sticky="w")#
            try:
                #val = str(round( df.loc[ df.index[r],columN[c]])).replace('0','')
                val = round( df.loc[ df.index[r],columN[c]])
                #val = round(df.reindex(columns=columN).iloc[r][c])
                tk.Label( fra__, text = val ,bg = None if r % 2 == 0 else None).grid( row = r+1, column = c+1)
            except ValueError:#float NaN to integer :tkinter
                pass
            tk.Label( fra__, text = "総計", relief = "groove" ).grid(row = 1+len(df.index.values), column=0,pady=7)
            try:                
                tk.Label( fra__, text = round(df.cumsum()[columN[c]][df.index[r]]) ).grid(row=1+len(df.index.values), column=c+1)#累積和
            except (IndexError, ValueError):
                pass
            
        fra__.pack(  ipadx=1)  #_forget#
        fram_.pack()  
        fram_ = tk.Frame(frame)
        tin=[]
        sub.bind("<MouseWheel>", lambda event:table.wheel( event,tin) )
        fram_.pack( padx=2)
        frame.pack()
        sub.bind('<2>', lambda event:sub.destroy())    
        elapsed_time = time.time() - start
        print ("{0}".format(elapsed_time) + "[sec]")   
        sub.mainloop()       

    def group(self):        
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
        
        columN = list( cc_.keys())
        df = pd.DataFrame(data= bb_, dtype=object)
        df = pd.DataFrame(data= df.T.reindex(columns=columN), dtype=object)
        columNS = range( len( df.columns) )

        frame = tk.Frame(sub)
        fram_ = tk.Frame(frame)
        fra__= tk.LabelFrame(fram_)###                
        fram=tk.Frame(frame)
        vr = tk.IntVar()
        vr.trace("w",table.trace_)
        table.select(vr,fram,sub)
        fram.pack()            
        cvs = table.scrollbar(fram_,ww, wh)

        fra__ = tk.LabelFrame(cvs)
        dic = ls.group()#   
        tUB =[ dic[i] for i in [ item for item in df.index]]        
        gROUP = sorted( set(tUB))  

        lis= defaultdict(int)
        for idx in df.index:
            lis[dic[idx]] += df.loc[ idx]
            
        df = pd.DataFrame(data= lis, dtype=object)
        df = pd.DataFrame(data= df.T, dtype=object)
        rowS = range( len( df.index))

        for r, c in itertools.product( rowS, columNS):##for分で回すにはイテレータである必要がある  
            tk.Label( fra__, text=ext.gomoji(columN[c]), bg= ext.clr(columN[c])).grid(row= 0, column= c+1)#value[c]
            tk.Label( fra__, text= "グループ"+ gROUP[r], bg="lightgray").grid(row=r+1, column=0,sticky="w")#
            try:
                #val = str(round( df.loc[ df.index[r],columN[c]])).replace('0','')
                val = round( df.loc[ df.index[r],columN[c]])
                #val = round(df.reindex(columns=columN).iloc[r][c])
                tk.Label( fra__, text = val ,bg = None if r % 2 == 0 else None).grid( row = r+1, column = c+1)
            except ValueError:#float NaN to integer :tkinter
                pass
            tk.Label( fra__, text = "総計", relief = "groove" ).grid(row = 1+len(df.index.values), column=0,pady=7)
            try:                
                tk.Label( fra__, text = round(df.cumsum()[columN[c]][df.index[r]]) ).grid(row=1+len(df.index.values), column=c+1)#累積和
            except (IndexError, ValueError):
                pass
        fra__.pack(  ipadx=1)  #_forget#
        fram_.pack()  
        fram_ = tk.Frame(frame)
        fram_.pack( padx=2)
        frame.pack()
        sub.bind('<2>', lambda event:sub.destroy())    
        elapsed_time = time.time() - start
        print("{0}".format(elapsed_time) + "[sec]")   
        sub.mainloop()   

    def setting(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #  
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        sub = ee_
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
        fram.pack()
        cvs = table.scrollbar(fram_,ww, wh)
        fra__= tk.LabelFrame(cvs, text="グループ設定")##      
        for r in rowS:            
            try:
                btn = tk.Button( fra__,text=df.columns.values[r] )
                btn.bind( "<1>", lambda event:table.callback( event, ee_, df))
                btn.grid( row= r, column = 0, ipady=1)
                tk.Label( fra__, text= "グループ" + str(dic[df.columns.values[r]]) ).grid( row=r, column=1, ipadx=2, ipady=2)
            except (IndexError, ValueError):#float NaN to integer :tkinter
                pass           
        fra__.pack(  ipadx=5,ipady=5)###  
        fram_.pack() 
        frame.pack()            
        sub.bind('<2>', lambda event:sub.destroy())       
        sub.mainloop()
        
    def scrollbar(fram_,ww, wh):
        canvas = tk.Canvas(fram_, width=ww, height=wh)
        ybar = tk.Scrollbar(fram_, orient="vertical")
        ybar.pack(side="right", fill="y")
        ybar.config(command=canvas.yview)
        xbar = tk.Scrollbar(fram_, orient="horizontal")
        xbar.pack(side="bottom", fill="x")
        xbar.config(command=canvas.xview)
        canvas.config(yscrollcommand=ybar.set, xscrollcommand=xbar.set) # Canvasのサイズ変更をScrollbarに通知
        canvas.config(scrollregion=(0,0,ww,wh/2)) #スクロール範囲
        canvas.pack( side="top", fill=tk.BOTH, expand=True, padx=5, pady=5)
        cvs = tk.Frame(canvas)
        canvas.create_window((0,0), window=cvs, anchor=tk.NW, width=0, height=0)
        return cvs
    def callback( event, sub, df):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        event.widget["relief"]
        event.widget["activeforeground"]
        info = event.widget.grid_info()
        info['row'], info['column']#-
        
        top = tk.Toplevel()
        val = tk.IntVar( top)
        dic = ls.group()
        key = event.widget["text"]
        inT = dic[key]
        columnS = df.columns.values
        val.set(inT)
        
        fram_ = tk.LabelFrame(top,text='「'+event.widget["text"]+'」'+"\nグループ番号を設定する")
        spn = tk.Spinbox(fram_, textvariable=val, width=3,from_= 1,to= len(columnS), state = 'readonly',command=lambda :ext.group(key,spn.get()) )
        spn.pack(side="left", padx=2 ,pady=2)
        tk.Button( fram_,text="保存",command =lambda:table.reflexion( sub, top) ).pack(side="left", padx=2 ,pady=2)#side="left"
        
        fram_.pack(side="left", padx=2 ,pady=2)
        cansell = tk.Button(top, text="キャンセル" ,command = top.destroy)
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:top.destroy() )
        cansell.pack(side="left", padx=2 ,pady=2)
        key, dic[key], len(columnS), columnS, dic, spn.get()
        
        if event.widget["bg"] == "SystemButtonFace":# ボタンの背景色がデフォルト値だったら赤に変更し、
            event.widget["bg"] = "SystemButtonFace"     
        else:
            event.widget["bg"] = "SystemButtonFace"# 
                
    def exhibition(df):#展示
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'b': 2, 'c': 4, 'd': 5}
        key1 = d1.keys() | d2.keys()##和集合
        key2 = d1.keys() & d2.keys()##共通部分
        sorted(key1), key2
        sorted( df.index.values)
        df.T.values
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
        
    def reflexion(sub,top):#反射,反映
        top.destroy()
        children = sub.winfo_children() 
        for child in children:
            child.destroy()         
        cum(0,0,0,0,sub).post()
        
    def wheel(event,tub):
        if event.delta < 0:
            tub.append(event.delta)
        elif event.delta > 0 and len(tub) > 0:#
            tub.remove(event.delta*-1)
        len(tub)

    
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    cum(0,0,0,0,root).post()
    #table(0,0,0,0,root).post()
    root.mainloop()
    """"""
    lst = ls.customer()
