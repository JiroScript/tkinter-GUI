import tkinter as tk
import sys
import os
import time
import re
import ls
import ext
import sl
import data
import panda
import auxi

class table(ls.sp): #部数 
    def post(self):         
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        table.scll( ee_)
        
    def sngl( dd:dict, l:list)->list:
        for k, dic in dd.items():
            l.append( str( k ) + re.sub( "'|{|}", ' ',str( dic )) ,)
        return l
        
    def save( tpl:tuple, sub):  
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        num = tpl[0]
        if type(num) == int:
            ext.renew( num, True, os.path.basename(__file__))
            ext.save( ls.dl()[3] ,num )
            ext.save( ls.dl()[4] ,num + 1   ) 
        sub.destroy() 
        
    def scll( sub): #
        sub.title("呼出")
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame = tk.Frame(sub)        
        fram=tk.Frame(frame)
        fram.pack(padx=3)
        frame.pack(padx=2)
        
        lst = ls.customer()
        keylst = ls.tm()+ls.kl()[4:]
        
        ll = sl.LL.LD_S_L( lst, "not in", keylst ) # [[0, '区分'], [0, '区間'], [0, '名称1'], [0, '号数'], [0, 'ア'], [0, 'マ'], [0, 'ヨ'], [0, 'サ'], [0, '産'], [0, 'ト'], [0, '税のしるべ'],]
        dd = sl.DD.LL_LD(ll,lst,{}) # {0: {'区分': '人事院', '区間': '', '名称1': '秘書室①', '号数': '1', 'ア': '3', 'マ': '3', 'ヨ': '3', 'サ': '3', '産': '3', 'ト': '3', '税のしるべ': '1'},}
        lis = table.sngl( dd, []) # ['0  区分 :  人事院 ,  区間 :   ,  名称1 :  秘書室① ,  号数 :  1 , サ :  3 , ] 
        ( lis )    
        scrollbarx = tk.Scrollbar( fram)
        scrollbarx.pack( side="bottom", fill="x")        
        scrollbary = tk.Scrollbar( fram)
        scrollbary.pack( side="right",fill="y")
                
        var = tk.StringVar(value = lis )
        listbox = tk.Listbox( fram, listvariable= var, width=80, height=16)
        listbox.config( xscrollcommand= scrollbarx.set)
        listbox.config( yscrollcommand= scrollbary.set)
        listbox.pack( fill= "x" )
        listbox.bind( "<<ListboxSelect>>", lambda event:table.save( listbox.curselection(), sub), )      
        scrollbarx.config( orient= tk.HORIZONTAL, command= listbox.xview)      
        scrollbary.config( orient= tk.VERTICAL  , command= listbox.yview)   
        tk.Button( sub, command= sub.destroy, text='戻る', relief="groove", bd=4 ).pack( padx=1, pady=1)
        sub.mainloop() 
    
class gdgt_():
    def table( inx, lst:list,  root) :
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        start = time.time()  
        auxi.wid.forget(root)
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.title("呼出") 
        root.geometry( ls.ge(ww,wh) )
        root.option_add( '*font', 'TkDefaultFont'+' '+ ls.ft()[1] ) # ls.ft()[2]
        
        frame= tk.Frame(root) #
        frame.pack()      
        fram_= tk.LabelFrame(frame, text="プレビュー")
        fram_.pack(side="right")   
        fra__= tk.Frame(frame)   
        fra__.pack(side="right")  
        cvs = panda.table.scrollbar(fra__, ww+1000, wh+20000)
        root.bind("<MouseWheel>", lambda event:cvs.master.yview_scroll(int(-1*(event.delta/120)), "units") )
        #
        lf= tk.Frame(cvs)  
        lf.pack()  
        #
        gdgt_.roop( lf, fram_, inx, lst,root)
        data.anlys.cancel( fra__, root)
        elapsed_time = time.time() - start
        ("{0}".format(elapsed_time) + "[sec]")  
        
        
    def roop( lf, fram_, inx, lst, root):
        lst = lst # [inx:]
        itr = [ ls.kb(), ls.kk(), ls.gs(), ls.mi(), '一時止']
        hss = {}
        for c, dic in enumerate( lst):
            btn = tk.Button( lf, text= c )
            btn.grid( row= c + 1, column= 0)
            
            btn.bind('<FocusIn>', lambda event:auxi.unit.preview( fram_ , lst[ event.widget['text']] ),)
            btn.bind('<Enter>', lambda event:auxi.unit.preview( fram_ , lst[ event.widget['text']] ),)
            btn.bind('<1>', lambda event: table.save( (event.widget['text'],None), root))
            
            for r, rw in enumerate( itr) :
                if rw not in hss.keys(): 
                    lbl = tk.Label( lf, text= rw if rw !='名称1' else '名称', relief="groove", fg= ext.font_clr(None, rw), bg= ext.clr(rw))
                    lbl.grid( row= 0, column= r + 1)
                    
                if  rw !=  '一時止' and  dic.get( rw,'') != '': 
                    lb_ = tk.Label( lf, text= '{:.10}'.format(dic.get(rw,'') ), relief="groove", fg= "#" + str(c).zfill(6) )
                    lb_.grid( row= c + 1, column= r + 1)  
                    
                elif rw == '一時止' and dic.get( '取扱', '') != '': 
                    lb_ = tk.Label( lf, relief="groove", fg= "#" + str(c).zfill(6), text="{0}月{1}日{2}～{3}月{4}日{5}迄　{6}".format(dic[ ls.tm()[0] ], dic[ ls.tm()[1] ], dic[ ls.tm()[2] ], dic[ ls.tm()[3] ], dic[ ls.tm()[4] ],dic[ ls.tm()[5] ],dic[ ls.tm()[6] ]) if dic[ ls.tm()[0] ] !="" else '' )
                    lb_.grid( row= c + 1, column= r + 1)  
                    
                lb_.bind('<Enter>', lambda event:auxi.unit.preview( fram_ , lst[ con.hf(event.widget['fg'])] ),)
                lb_.bind('<1>', lambda event:table.save( (con.hf(event.widget['fg']), None), root),)
                hss = gdgt.add( hss, rw)
                        
    def add( hss, txt):
        hss[txt] = None
        return hss
    
class D():
    def add( lst:list, l:list)->list:
        for i, dic in enumerate(lst):
            dic = { **{ "番号": str(i)}, **dic }
            l.append(dic)
        return l
    
class I():
    def LD_S( lst:list, txt:str, l:list)->int: # Widthの値をintで返す。
        itr = [ dic.get(txt) for dic in lst]
        for i in itr:
            if i == None:
                i = '0'
            l.append( ext.east_asian(i) )
        n = max(l)
        return n if n < 18 else 18

class L():    
    def LL_LL( itr, arr): # ls.nw()[1:], ['サ', 'A', 'ア', 'マ', 'ヨ', '産', 'ト', '農業']
        return [ i for l in itr for i in l if i in arr ] # ['農業', 'A']
        
class gdgt():
    def table( inx, lst:list,  root) :
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = lst#[:4]
        
        start = time.time()  
        auxi.wid.forget(root)
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.title("呼出") 
        root.geometry( ls.ge(ww,wh) )
        root.option_add( '*font', 'TkDefaultFont'+' '+ ls.ft()[1] ) # ls.ft()[2]
        
        frame= tk.Frame(root) #
        frame.pack(side="left", anchor = tk.NW)      
        fram_= tk.LabelFrame(frame, text="プレビュー")
        fram_.pack(side="left")   
        fra__= tk.Frame(frame)   
        fra__.pack(side="left")  
        #
        dic = { i:0 for i in range(len(lst))} #
        tpl = ( inx, inx + 10)
        lst = D.add( lst, [])
        root.bind( "<MouseWheel>", lambda event:gdgt.wheel( event, dic , lf, fram_, tpl, lst, root), "+" )
        lf= tk.Frame(fra__)  
        lf.pack()  
        gdgt.roop( lf, fram_, tpl, lst, root)
        #
        data.anlys.cancel( fra__, root)
        elapsed_time = time.time() - start
        ("{0}".format(elapsed_time) + "[sec]")  
        
    def wheel( event, dic, lf, fram_, tpl, lst, root):
        inx, i1 = tpl
        n = -(sum(dic.values())) + inx
        (inx, n)
        dic = gdgt.brnc( event, dic, inx, n, lst)
        (dic)
        (dic.values())
        (sum(dic.values()))
        inx = -(sum(dic.values())) + inx 
        ( inx, sum(dic.values()))
        gdgt.forget( lf)
        gdgt.roop( lf, fram_, ( inx, inx + 10), lst, root)

    def brnc( event, dic, inx, n, lst): # Conditional branch
        if event.delta > 0 :
            if sum(dic.values()) == 0: 
                if inx > 0 : 
                    dic[n] += 1
            elif sum(dic.values()) < inx:
                    dic[n] += 1
                
        elif event.delta < 0 :
            if n == len(lst) -1:
                pass
            else:
                dic[n] += -1
        return dic   
    
    def row(txt):
        if txt == '名称1':
            txt = '名称'
        elif txt =='番号':
            txt = "  "
        else:
            txt = txt
        return ext.tategaki(txt)  
      
    def roop( lf, fram_, tpl, lst, root):
        i0, i1 = tpl
        ld = lst[ i0 : i1]
        itr = [ '番号', ls.kb(), ls.kk(), ls.gs(), ls.mi(), '一時止']
        hss = {}
        arr = list({ i : None for dic in ld for i in dic if i not in ls.kl() + itr }) # ['サ', 'A', 'ア', 'マ', 'ヨ', '産', 'ト', '農業']
        arr = list(reversed(ls.nw()[0])) + L.LL_LL( ls.nw()[1:], arr) # ['ト', '産', 'サ', 'ヨ', 'マ', 'ア'] + ['農業', 'A']
        for c, dic in enumerate( ld):
            for r, txt in enumerate( itr + arr ):
                # Widthの値を算出、intで返す。
                iw  = I.LD_S( lst, txt, []) # int, width
                if txt not in hss.keys(): #  if txt !='名称1' else '名称'
                    lbl = tk.Label( lf, text= gdgt.row(txt), height=5, width= iw, relief="groove", fg= ext.font_clr(None, txt), bg= ext.clr(txt))
                    lbl.grid( row= 0, column= r + 1, ipadx=3)
                    
                if  txt == '番号': 
                    btn = tk.Button( lf, text= dic.get('番号'), width= iw, relief= 'raised',  fg= "#" + str(c).zfill(6) )
                    btn.bind('<1>', lambda event: gdgt.save( int(event.widget['text']), root))  
                    btn.grid( row= c + 1, column= r + 1) 
                elif  txt !=  '一時止' and  dic.get( txt,'') != '': 
                    lb_ = tk.Label( lf, text= '{:.10}'.format(dic.get(txt,'') ), width= iw, relief="groove", fg= "#" + str(c).zfill(6) )
                    lb_.grid( row= c + 1, column= r + 1)  
                    
                elif txt == '一時止' and dic.get( '取扱', '') != '': # "{0}月{1}日{2}～{3}月{4}日{5}迄　{6}"
                    lb_ = tk.Label( lf, relief="groove", fg= "#" + str(c).zfill(6), width= iw, text="{6}".format(dic[ ls.tm()[0] ], dic[ ls.tm()[1] ], dic[ ls.tm()[2] ], dic[ ls.tm()[3] ], dic[ ls.tm()[4] ],dic[ ls.tm()[5] ],dic[ ls.tm()[6] ]) if dic[ ls.tm()[0] ] !="" else '' )
                    lb_.grid( row= c + 1, column= r + 1)
                    
                hss = gdgt.add( hss, txt)
                             
    def forget(root):
        children = root.winfo_children() 
        for child in children:
            child.destroy() 
                        
    def add( hss, txt):
        hss[txt] = None
        return hss

    def save( num, sub):  
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        if type(num) == int:
            ext.renew( num, True, os.path.basename(__file__))
            ext.save( ls.dl()[3] ,num )
            ext.save( ls.dl()[4] ,num + 1   ) 
        sub.destroy() 
        
class con(): # conversion:変換
    def hf(txt): # Half size:半角, '#000001'
        num = re.sub(r"\D", "", txt) # 半角＆全角の数字を取り出す, '1'
        num = int(num) # 1
        return num
    
if __name__ == '__main__':
    root = tk.Tk() 
    #gdgt_.table(ls.start(), ls.customer(), root)
    gdgt.table(ls.start(), ls.customer(), root)#

    table(None,None,None,None,root)#.post()
    root.mainloop()
