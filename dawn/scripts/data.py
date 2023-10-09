import tkinter as tk
import os.path
import os
import ls
import sys
import math
import log
import ext
import panda
import time
import prnt

class anlys(): # 数値,analysis:解析,
    def __init__(self, l__):
        self.l__ = l__   #    

    def arr(lst): # array
        return [ i if i == 0 or i != 0 and lst[i-1]['区分'] != dic['区分'] else None for i, dic in enumerate(lst)] # [0, None, None, None, None, 23, None, 

    def tll(lst):
        l1 = [ i if i == 0 or i != 0 and lst[i-1]['区分'] != dic['区分'] else None for i, dic in enumerate(lst)] # [0, None, None, None, None, 23, None, 
        l2 = [ i if i == 0 or i != 0 and lst[i-1]['区間'] != dic['区間'] else None for i, dic in enumerate(lst)] 
        return l1, l2
    
    def num(lst):
        dct, dd, dn, ddd = {}, {}, {}, {}
        for i , dic in enumerate(lst):
            for k , v  in dic.items(): 
                ddd = anlys.section( dic, ls.kl(), k , v, ddd ) # {'人事院': {'': {'ア': 15, 'マ': 13, 'ヨ': 19, 'サ': 31, 
                if k not in ls.kl():
                    dct.setdefault( k , 0)
                    dct[ k ] += int( v )
                    kb = dic.get('区分')
                    dd.setdefault( dic['区分'], {})
                    dd[ kb].setdefault( k , 0) # ネスト構造
                    dd[ kb][ k ] = int( v ) if k not in dd[ kb].keys() else int( dd[ kb][ k ]) +  int( v )
                    dn.setdefault( k , None)
                    
        return dct, D.D_T( dd, log.anlys.nw(), {} ), { i:None for i in log.anlys.nw() if i in dn }, ddd
        # {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, 'A': 15, '農業': 10, 
        # {'人事院': {'ト': 10, '産': 12, 'サ': 31, 'ヨ': 19, 'マ': 13, 'ア': 15, '農業': 1, 'A': 2}, '弁護士会館': {'ト': 7, '産': 
        # {'ト': None, '産': None, 'サ': None, 'ヨ': None, 'マ': None, 'ア': None, '工': None, '日産': None, '流通': None,
        # {'人事院': {'': {'ア': 15, 'マ': 13, 'ヨ': 19, 'サ': 31, '産': 12, 'ト': 10, 'A': 2, '農業': 1}}, '弁護士会館': {'': {'ア': 11,
    
    def section( dic, keylst, k , v , ddd)->dict:
        if k not in keylst or k in '区間':
            kb = dic.get('区分')
            kk = dic.get('区間')
            ddd.setdefault( kb, {})
            if k in '区間':
                ddd[ kb].setdefault( v , {})
                ( ddd[ kb])
            if k not in '区間':
                (ddd[ kb] )
                ddd[ kb][ kk].setdefault( k ,0)
                ddd[ kb][ kk][ k ] = int( v ) if k  not in ddd[ kb][ kk].keys() else int(ddd[ dic[ ls.kb()]][ kk][ k ] ) +  int( v )
        return ddd # {'人事院': {'': {'ア': 15, 'マ': 13, 'ヨ': 19, 'サ': 31, 
    
    def lot(start,lst) :###numerical:lot:区分,品分け
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        arr = anlys.arr(lst)#[ i if i == 0 or i != 0 and lst[i-1][ls.kb()] != lst[i][ls.kb()] else None for i in range(len(lst))]
        anlys.wdgt( start,lst)
        if start in arr:
            print(start, "bingo") 
            if None != None: 
                anlys.table(start,lst)
                
        elif start not in arr :#and 
            sub= anlys.subb()
            sub.winfo_ismapped() == 1
            print(start, "outskirts")
    
    def table( lst, lis, root) :
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        start = time.time()  
        d__= anlys.num(lst)[0]
        two = anlys.num(lst)[1]
        dc  = anlys.num(lst)[2]
        itr = [ i for i in dc.keys() if i in lis]
        #
        anlys.forget(root)
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.title("部数") 
        root.geometry( ls.ge(ww,wh) )
        root.option_add( '*font', [ 'TkDefaultFont', ls.ft()[0] ] )

        frame= tk.Frame( root) #
        frame.pack()      
        fram_= tk.Frame( frame) 
        fram_.pack()      
        east= tk.Frame( frame) 
        east.pack(side='right')      
        fra__= tk.Frame( frame)   
        fra__.pack()     
        cvs = panda.table.scrollbar( fra__, ww, wh)
        lf= tk.Frame(cvs)  
        lf.pack()  
        
        gdgt.butn(fram_, lst, 6, root)
        anlys.cancel( east, root)    
        anlys.loop( lf, d__, two, itr)
        elapsed_time = time.time() - start
        ("{0}".format(elapsed_time) + "[sec]")   
        root.bind("<MouseWheel>", lambda event: root.destroy() if event.delta < 0 else None  )
        root.mainloop()
        
    def loop(lf, d__, two, itr):
        for c, clmn in enumerate( two):
            tk.Label( lf, text= clmn, relief= "groove").grid( row= c + 1, column= 0)
            for r, rw in enumerate( itr) :
                tk.Label( lf, text= ext.gomoji(rw), relief="groove", fg= ext.font_clr(None, rw), bg= ext.clr(rw)).grid( row= 0, column= r + 1)
                tk.Label( lf, text= two[clmn].get(rw), relief="groove", bg= "white").grid( row= c + 1, column= r + 1)  ##,fg=ext.fg(lst[di][rw]), bg= ext.clr(lst[di][rw])
                tk.Label( lf, text =  d__.get(rw), relief="groove", bg="lightgray" ).grid( row= len(two)+1, column= r+1)  ##,fg=ext.fg(lst[di][li]), bg= ext.clr(lst[di][li])
        
    def cancel( frame, sub):
        cancel = tk.Button( frame, text= "×", command= sub.withdraw, font=('TkDefaultFont',ls.ft()[0]))
        cancel.bind('<FocusOut>', lambda event: sub.destroy())
        cancel.bind('<Return>', lambda event: sub.destroy())
        cancel.bind('<Motion>', lambda event: None)
        cancel.pack( padx=2, pady=2)
        cancel.focus_force()  
            
            
    def resize( event, arr):
        if event.delta > 0:
            arr.append(event.delta)
            ("↑", event.x, event.y)            #
        elif event.delta < 0 :#
            if len(arr) > 0 :arr.pop(0) 
            ("↓",event.delta)
        (len(arr))
        
    def wdgt( start, lst, sub) :##widget
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        sub.title("部数") 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        sub.option_add( '*font', [ 'TkDefaultFont', 18 ] )

        frame=tk.Frame(sub)#
        f_ame= tk.LabelFrame(frame, text=ls.kb(), font=('TkDefaultFont',ls.ft()[2]))
        f_ame.pack(anchor=tk.W,padx=6)  
        fr___ = tk.Frame( frame)  
        fr___.pack(anchor=tk.W,padx=2)    
        east= tk.Frame( frame) 
        east.pack(side='right')     
        anlys.cancel(  east, sub)    
        cvs = panda.table.scrollbar( frame, ww, wh)  
        fra__ = tk.LabelFrame( cvs) 
        fra__.pack( )      
        fram_= tk.Frame(frame)    
        fram_.pack( ) 
        frame.pack( padx=2, pady=2)   
        sub.bind("<MouseWheel>", lambda event: sub.destroy() if event.delta < 0 else None  )
        
        divi = lst[ start][ ls.kb()]
        zero, two, uno, trpl = anlys.num(lst)
        two # {'人事院': {'ト': 10, '産': 12, 'サ': 31, 'ヨ': 20, 'マ': 13, 'ア': 15, '農業': 1, 'A': 2}, '弁護士会館': {'ト': 7, '産': 7, 'サ': 16, 'ヨ': 12, 'マ': 12, 'ア': 13, '報知': 1, '日刊スポ': 1, 'スポニチ': 1, 'A': 2, '碁': 1}, 
        uno # {'ト': 10, '産': 12, 'サ': 31, 'ヨ': 20, 'マ': 13, 'ア': 15, '工': None, '日産': None, 
        trpl # triple, {'人事院': {'': {'ア': 15, 'マ': 13, 'ヨ': 20, 'サ': 30, '産': 12, 'ト': 10, 'A': 2, '農業': 1}, 'S': {'サ': 1}}, '弁護士会館': {'': {'ア': 13,
        tk.Label( f_ame, text= divi).pack()#
        anlys.grdd(fra__,divi, uno,trpl) #格子
        (uno)
        sub.mainloop()
        
    def grdd( frame, divi, uno, itr): # grid:格子
        (itr[divi])
        for c, two in enumerate( itr[divi]):
            (c,two)
            tk.Label( frame, text= two , relief= "groove",width=5).grid( row= c + 1, column= 0)
            for r, tex in enumerate( uno) :
                (r, tex)
                if tex in itr[divi][two].keys():
                    tk.Label( frame, text= ext.gomoji( tex), relief="groove", fg= ext.font_clr(None,  tex), bg= ext.clr( tex)).grid( row= 0, column= r + 1)
                    tk.Label( frame, text= itr[divi][two].get( tex), relief="groove", bg= "white").grid( row= c + 1, column= r + 1) 
             
    def forget(root):
        children = root.winfo_children() 
        for child in children:
            child.destroy() 
            
class cfg(): # config, Cumulative:累計
    def kb( aa_:int, dct:dict):
        txt = dct.get('区分')
        txt =  "{:.7}".format(txt) # 7文字まで
        return '' + txt 
    
    def kk( aa_:int, dct:dict):
        txt = dct.get('区間')
        return '' + txt 
        
    def east( aa_:int, i:int, lst:list):
        if aa_ == 0 :
            return ' ' + '◀'
        elif aa_ != 0 and lst[aa_][ls.kb()] != lst[aa_-1][ls.kb()] :
            return ' ' + '◀'
        
    def efg( aa_:int, i:int, lst:list):
        divi = lst[aa_][ls.kb()]
        if aa_ == 0 :
            return "black"
        elif aa_ != 0 and divi != lst[aa_-1][ls.kb()] :
            return ext.divi_clr( lst, divi)
        
    def west( bb_:int, i:int, lst:list):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        if bb_ == len(lst):
            return ' ' + 'close'
        elif lst[bb_-1][ls.kb()] != lst[bb_][ls.kb()]:
            return ' ' + '▶'
        
    def wfg( bb_:int, i:int, lst:list):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()
        if bb_ == len(lst):
            return ls.cl()[0],
        elif  lst[bb_-1][ls.kb()] != lst[bb_][ls.kb()]:
            return ext.divi_clr( lst, lst[bb_-1][ls.kb()])
        
    def txx( frame, aa_:int, i:int, lst:list): #
        l1, l2 = anlys.tll(lst) # [0, None, None, None, None, 5
        if aa_ == i and i in l1 or i in l2:
            lis = [ s for s in reversed( ls.nw()[0])] # ['ト', '産', 'サ', 'ヨ', 'マ', 'ア'], +  [ ls.nw()[1][0]] + [ ls.nw()[1][1]] + [ls.nw()[9][0]] + [ls.nw()[12][0]]
            kb, kk = lst[aa_]['区分'], lst[aa_]['区間']
            dct = anlys.num(lst)[3][kb][kk] # {'ア': 15, 'マ': 13, 'ヨ': 20, 'サ': 31, '産': 12, 'ト': 10, 'A': 2, '農業': 1},新聞ごとの部数、部数、区間、指定なし、
            for s in lis:
                tk.Label( frame, text= str( dct.get(s) if dct.get(s) != None else '　' ), relief="groove", width= 3, font= ( "TkDefaultFont", ls.ft()[0])).pack(side="left")
                tk.Label( frame, text= s , fg=ext.font_clr(None, s) if s in dct.keys() else ext.clr(s),  font= ( "TkDefaultFont", ls.ft()[0])).pack(side="left")
                tk.Label( frame, text= ' ', ).pack(side="left")
            
    def hide(event, wdgt): # 非常時
        wdgt.config( state= "disabled")
        wdgt.config( disabledforeground= "#dfe1ce")
        event.widget
        

class gdgt():
    def clla( txt:str)->list: # collation:照合
        if ls.kt()[0] == txt: # 一般紙
            return ls.nw()[0] 
        elif ls.kt()[1] == txt: # 産業紙
            return ls.nw()[1]
        elif ls.kt()[2] == txt: # 業界紙
            return ls.nw()[3]  + ls.nw()[4] + ls.nw()[5] + ls.nw()[6] + ls.nw()[7]
        elif ls.kt()[3] == txt: # 金融紙
            return ls.nw()[2]
        elif ls.kt()[4] == txt: # スポーツ紙
            return ls.nw()[10] 
        elif ls.kt()[5] == txt: # 海外紙
            return ls.nw()[11] 
        elif ls.kt()[6] == txt: # 国内英字紙
            return ls.nw()[12] 
        elif ls.kt()[7] == txt: # 青少年向き
            return ls.nw()[13] 
        elif ls.kt()[8] == txt: # レジャー・趣味
            return ls.nw()[14] 
        elif ls.kt()[9] == txt: # 一般夕刊紙
            return ls.nw()[15] 
        elif ls.kt()[10] == txt: # 各種の縮刷版・その他
            return ls.nw()[16] + ls.nw()[17]
        elif ls.kt()[11] == txt: # 全て
            return [ ii for i in ls.nw() for ii in i]
        
    def butn( fra__, lst, nm, root):
        num = len( ls.kt())
        nm = nm #横に表示するwidgetの上限数
        ceill= math.ceil(num / nm)# 切り上げ
        for n in range(ceill):  
            frame = tk.Frame(fra__)
            for i, li in enumerate( ls.kt()[n*nm:nm*n+nm]):  
                [n*nm, nm*n+nm]
                btn= tk.Button( frame, text= li, font=('TkDefaultFont', int(ls.ft()[2]) + 2))
                btn.configure#( bg= anlys.bg( ktg,li))
                btn.configure#( fg= anlys.fg( ktg,li))
                btn.pack(side="left")
                btn.bind( '<1>', lambda event: anlys.table( lst, gdgt.clla(event.widget['text']), root)) # 
            frame.pack()
                
class D():
    def D_T( dd:dict, tpl:tuple, hss:dict)-> dict:
        for txt in dd.keys() : # dict_keys(['人事院', '弁護士会館', '富国生命', 'プレスセンター', '厚生労働省', '日比谷国際ビル', 'パークフロント'])
            hss.setdefault( txt, {})
            for i in tpl :
                if i in dd[ txt].keys():
                    hss[ txt].setdefault( i, dd[ txt ][i])
        return hss # {'人事院': {'ト': 10, 'サ': 31}, '弁護士会館': {'ト': 7, '産': 6}}
    # 
    def LD_D( lst:list, dic)->dict: # lst, 人事院, ア 
        for  k, v in  dic.items():
            hss = { i: int(hss.get(k)) for i, hss in enumerate(lst) if k in hss.keys() and v in hss.values()} 
            hss # {0: 3, 1: 1, 2: 1, 4: 1, 9: 2, 11: 1, 13: 1, 16: 1, 18: 1, 19: 1, 21: 2}, {0: 3, 1: 2, 2: 1, 3: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 3, 10: 1, 11: 1, 12: 1, 13: 3, 14: 1, 16: 2, 17: 1, 18: 3, 19: 1, 21: 2, 22: 1}
            (sum(hss.values())) # 15, 31
            
class I():
    # 表示されてる顧客、　以降の残りの部数を、　intを返す。
    def LD_I_S( lst:list, ix:int, txt:str)->int: # 
        ( ix, txt) # 0, 'ア'
        divi, sect = lst[ ix]['区分'], lst[ ix]['区間'] # '人事院','A'  division: 区分, section:区間
        # '区分'
        [ int(dic.get(txt)) for i, dic in enumerate(lst) if ix < i and divi in dic.values() and txt in dic.keys() ] # [1, 1, 1, 2, 1, 1, 1, 1, 1, 2]
        # '区分','区間'
        arr = [ int(dic.get(txt)) for i, dic in enumerate(lst) if ix < i and divi in dic.values() and sect in dic.values() and txt in dic.keys() ] # [1, 1, 1, 2, 1, 1, 1, 1, 1, 2]
        if txt in ls.nw()[0] : # 一般紙はNoneを返し、表示しない。 
            return sum(arr) % 100 # 12
        elif txt not in ls.nw()[0]: return sum(arr) % 100 
        else : pass # None
        
class B():
    # 最初か最期かをブールで返す。　
    def LD_I_S( lst:list, ix:int, txt:str)->bool:
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        kb = lst[ ix].get('区分') # '人事院'
        
        # Lstからtxtと一致するインデックスをリストで返す。
        arr = [ i for i, dic in enumerate(lst) if kb in dic.values() and '' == dic.get('区間') and txt in dic.keys() ] # [0, 1, 2, 3, 8, 10, 13, 16, 18, 19, 21]
        if len(arr) == 0:
            boole = False
        else:
            boole = bool( ix == min(arr) or ix == max(arr) )
        return boole # True

        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。   
    
    lst = ls.customer()
    I = I.LD_I_S( lst, 0, 'ア')
    (I)
    B.LD_I_S( lst, 33, 'サ')
    (anlys.arr(lst)) # [0, None, None, None, None]
    D.LD_D( lst, { 'ア': '人事院', 'サ': '人事院'})
    d0, d1, d2, d3 = anlys.num(lst)
    (d0,d1,d2,d3)
    anlys.wdgt#( ls.start(),lst, tk.Tk())  
    anlys.table( lst, ls.nw()[0], tk.Tk() )
    
    tpl = prnt.LD_DL_LD.get() # {'い': [0, 1, 2, 3,], 'ろ': [23, 24, 25], 'は': [33]
    ld, dl, l = tpl
    lld =[ [{ k : v for k , v in lst[i].items() if k not in ls.kl()} for i in l] for txt, l in dl.items()] # [[{'ア': '2', 'マ': '2', 'ヨ': '2', 'サ': '3', '産': '2', 'ト': '2'}, {'ア': '1', 'サ': '2'}, {'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '1', '産': '1', 'ト': '1'}, {'ア': '1', 'ヨ': '1'}, {'サ': '1'}, {'サ': '1'}, {'サ': '1', 'A': '1'}, {'サ': '1'}, {'ア': '2', 'マ': '1', 'ヨ': '3', 'サ': '3', '産': '1', 'ト': '1'}, {'サ': '1'}, {'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '1', '産': '1', 'A': '1', '農業': '1'}, {'サ': '1'}, {'ヨ': '1', 'サ': '1'}, {'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '3', 'ト': '1'}, {'サ': '1'}, {'ヨ': '1'}, {'ア': '1', 'マ': '1', 'ヨ': '2', 'サ': '2', '産': '1', 'ト': '1'}, {'サ': '1'}, {'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '3', '産': '1', 'ト': '1'}, {'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '1', '産': '1'}, {'産': '1'}, {'ア': '2', 'マ': '2', 'ヨ': '2', 'サ': '2', '産': '2', 'ト': '2'}, {'マ': '1', 'ヨ': '1', 'サ': '1'}], [{'ア': '4', 'マ': '4', 'ヨ': '4', 'サ': '5', '産': '3', 'ト': '4', 'A': '1'}, {'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '1'}, {'サ': '1'}, {'ア': '2', 'マ': '2', 'ヨ': '2', 'サ': '2', '産': '2', 'ト': '2', 'A': '1', '報知': '1', 'スポニチ': '1', '碁': '1'}, {'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '1'}, {'サ': '1'}, {'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '1', '日刊スポ': '1'}, {'ヨ': '1', 'サ': '1'}, {'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '1', '産': '1', 'ト': '1'}], [{'ア': '1', 'マ': '1', 'ヨ': '1', 'サ': '1', '産': '1'}]]
    (lld)
    lll = [[[9, 5, 9], [5, 4, 4, 5, 4], [9, 4, 10], [4, 5, 8, 4], [4, 9, 4], [9, 8, 4], [9, 6]], [[10, 7, 4], [13, 7, 4], [8, 5, 9]], [[8, 5], [13, 5], [9, 4, 7], [9, 4, 4, 5], [5, 9, 4, 4], [4, 5, 4, 4, 5], [4, 4, 5, 4, 4], [6, 4, 4, 5, 4], [4, 4, 4, 4, 4, 4], [4, 10, 4, 5], [4, 6, 4]], [[22], [8, 13], [8, 8, 8], [6, 8, 9], [4, 4, 5, 4, 4], [4, 5, 11, 4], [5, 4, 5, 4], [8, 4, 11], [6, 8, 7], [4, 11, 7]], [[9, 9], [9, 9], [9, 10], [6, 9, 9], [7, 9, 7], [11, 9], [11, 11], [12, 12], [13, 9], [8, 11], [9, 10], [11, 9], [10, 9], [9, 9], [9, 11], [8, 7], [11, 9], [8, 11], [10, 7], [9, 9], [9, 9], [9, 9], [9, 9], [9, 8, 4], [6, 11], [9, 9, 6], [9, 4]], [[4, 5, 6, 4, 4], [4, 5, 5, 5, 4], [11, 4], [10, 4, 6], [11, 5, 4, 4], [4, 4, 6, 9], [4, 4, 9, 4], [4, 6, 5, 4, 4], [5, 4, 4, 5], [10, 4, 4, 4], [4, 4, 5, 4, 4], [4, 9, 4, 4], [4, 6, 4, 5, 5], [5, 4, 4, 4, 6], [4]], [[4, 4, 5, 7, 4], [12, 4, 4], [5, 9, 4, 4], [4, 4]]]
    [ [ [ i for i in  I ] for I in ll ]  for ll in lll ]