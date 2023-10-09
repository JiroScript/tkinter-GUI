import tkinter as tk
import os.path
import os
import ls
import sys
import ext
import panda
import time

class anlys():###数値,analysis:解析,
    def __init__(self, l__):
        self.l__ = l__   #    

    def minimum( lst, divi, paper):###extract:抽出する  
        dic = { i:int(lst[i][paper]) for i in range(len(lst)) if lst[i][ls.kb()] == divi and paper in lst[i].keys() }
        num = min(list(dic.keys()))
        return num    
    
    def ext( lst, num, divi, paper, mini):###extract:抽出する  
        arr = [ int(lst[i][paper]) for i in range(len(lst)) if num <= i and lst[i][ls.kb()] == divi and paper in lst[i].keys() ]
        #print(num,arr)        #print(sum(arr),
        minimum = mini       #print(dic,minimum)
        if paper in ls.nw()[0] :
            if num == minimum:
                return sum(arr) % 100
            pass
        elif paper not in ls.nw()[0]:
            return sum(arr) % 100
        
    def fg( lst, num, divi, paper, mini):
        minimum = mini
        if paper in ls.nw()[0]:
            pass
        
        elif paper not in ls.nw()[0]:
            if num == minimum:
                return None
            return "gray"
        
    def arr(lst):#array
        return [ i if i == 0 or i != 0 and lst[i-1][ls.kb()] != lst[i][ls.kb()] else None for i in range(len(lst))]
    
    def num(lst):###  
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        keylst = ls.kl()
        d__= {}
        dic= {}
        dc = {}       
        di_= {}
        for i in range(len(lst)):
            for  tp in lst[i].items(): 
                ky= tp[0]
                vl= tp[1]
                #
                if ky not in keylst:
                    d__.setdefault( ky, 0)
                    d__[ky] += int( vl) #if ky not in dic[ lst[i][ls.kb()] ].keys() else int(dic[ lst[i][ls.kb()]][ky]) +  int(vl)
                    
                    dic.setdefault( lst[i][ls.kb()] ,{})
                    dic[ lst[i][ ls.kb()] ].setdefault( ky,0)#( ..)φメモメモ：ネスト構造
                    dic[ lst[i][ ls.kb()]][ky] = int(vl) if ky not in dic[ lst[i][ls.kb()] ].keys() else int(dic[ lst[i][ls.kb()]][ky]) +  int(vl)
                    dc.setdefault(ky,None)
                di_= anlys.section( lst, di_, keylst, i, ky, vl)
                
        dict = panda.cum.fmat(dic)
        list(dict.keys())[0]
        dict["人事院"]['マ']
        return d__, panda.cum.fmat(dic), panda.cum.fm_t(dc), di_
    
    def section( lst, di_, keylst, i, ky, vl):
        if ky not in keylst or ky in ls.kk():
            di_.setdefault( lst[i][ls.kb()], {})
            if ky in ls.kk():
                di_[ lst[i][ ls.kb()]].setdefault( vl, {})
                #print( di_[ lst[i][ ls.kb()]])
            if ky not in ls.kk():
                #print(di_[ lst[i][ ls.kb()]] )
                di_[ lst[i][ ls.kb()]][ lst[i][ ls.kk()]].setdefault( ky,0)
                di_[ lst[i][ ls.kb()]][ lst[i][ ls.kk()]][ky] = int(vl) if ky not in di_[ lst[i][ ls.kb()]][ lst[i][ ls.kk()]].keys() else int(di_[ lst[i][ ls.kb()]][ lst[i][ ls.kk()]][ky] ) +  int(vl)
        return di_
    
    def lot(start,lst) :###numerical:lot:区分,品分け
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        arr = anlys.arr(lst)#[ i if i == 0 or i != 0 and lst[i-1][ls.kb()] != lst[i][ls.kb()] else None for i in range(len(lst))]
        anlys.wdgt( start,lst)
        
        if start in arr:
            print(start, "bingo") 
            
            if None != None: 
                pass
                anlys.table(start,lst)
        elif start not in arr :#and 
            sub=anlys.subb()
            sub.winfo_ismapped() == 1
            print(start, "outskirts")
            
    def subb() :## 
        root = tk.Tk()
        root.withdraw()
        root.deiconify()
        return root
    
    def table( start, lst) :##widget
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        start = time.time()  
        d__= anlys.num(lst)[0]
        dict = anlys.num(lst)[1]
        dc   = anlys.num(lst)[2]
        sub = anlys.subb()
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.title("部数") 
        sub.geometry( ls.ge(ww,wh) )
        sub.option_add( '*font', 'TkDefaultFont'+' '+ ls.ft()[2])##YuGothic
        
        frame= tk.Frame(sub)#, bg="teal"
        fra__= tk.Frame(frame)   
        fra__.pack()       
        fram_= tk.Frame(frame)  
        cvs = panda.table.scrollbar(fram_,ww, wh)
        lf= tk.Frame(cvs)  
        lf.pack() 
        fram_.pack()   
        frame.pack() 
        
        for d, di in enumerate( dict):   
            tk.Label( lf, text= di, relief="groove").grid( row= d+1, column= 0)
            for l, li in enumerate( dc.keys()):
                tk.Label( lf, text= ext.gomoji(li), relief="groove",fg=ext.fg(li), bg= ext.clr(li)).grid( row= 0, column= l+1)
                try:
                    tk.Label( lf, text= str( dict[di][li]), relief="groove",bg="white").grid( row= d+1, column= l+1)  ##,fg=ext.fg(lst[di][li]), bg= ext.clr(lst[di][li])
                except KeyError:
                    tk.Label( lf, text="", relief="groove").grid( row= d+1, column= l+1) 
                    pass
                tk.Label( lf, text= str( d__[li]), relief="groove", bg="lightgray" ).grid( row= len(dict)+1, column= l+1)  ##,fg=ext.fg(lst[di][li]), bg= ext.clr(lst[di][li])
         
        cansell = tk.Button( fra__, text= "閉じる", command= sub.destroy, width=8)
        cansell.bind('<FocusOut>', lambda event: sub.destroy())
        cansell.bind('<Return>', lambda event: sub.destroy())
        cansell.pack( padx=2 ,pady=2)
        cansell.focus_force()  

        elapsed_time = time.time() - start
        print ("{0}".format(elapsed_time) + "[sec]")   
        sub.mainloop()
            
    def wheel(event, start, lst):
        if event.delta > 0:
            anlys.wdgt( ls.start(),lst)
            "↑"            #
        elif event.delta < 0 :#
            pass
            "↓"
            
    def wdgt( start, lst) :##widget
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        divi = lst[ start][ ls.kb()]
        dict = anlys.num(lst)[1]
        di_  = anlys.num(lst)[3]
        sub = anlys.subb()
        sub.title("部数") 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        sub.option_add('*font', 'TkDefaultFont'+' '+ ls.ft()[1])
        if None != None:
            sub.bind("<MouseWheel>", lambda event:anlys.wheel( event) )
        sub.bind("<MouseWheel>", lambda event: sub.destroy() if event.delta < 0 else None  )
        
        frame=tk.Frame(sub)#
        f_ame= tk.Frame(frame)
        f_ame.pack()  
        fram_= tk.Frame(frame)
        fra_e = tk.Frame(fram_) 
        fra_e.pack(side="left")   
        fra__ = tk.Frame(fram_) 
        fra__.pack(side="left")     
        fram_.pack(side="top") 
        fr___ = tk.Frame(frame)  
        fr___.pack()           
        frame.pack(padx=3, pady=2) 
        
        tk.Label( f_ame, text=divi).pack()#
        tk.Label( fra_e, text=ext.gomoji("")).pack()
        for kk in di_[ divi]:
            lf= tk.Frame(fra_e)
            tk.Label( lf,text= kk, bg="snow").pack()
            lf.pack( side='top') 
        tk.Label( fra_e, text="").pack()
        print(di_[divi],len(di_[divi]))
        for tpl in dict[ divi].items():
            lf= tk.LabelFrame( fra__)
            tk.Label( lf,text= ext.gomoji(tpl[0]),fg= ext.fg( tpl[0]), bg= ext.clr(tpl[0])).pack(side='top')
            for d in list(di_[divi]):
                try:
                    tk.Label( lf, text= di_[divi][d][tpl[0]] ).pack( side='top') if len(di_[divi]) > 1 else None
                except KeyError:
                    tk.Label( lf, text= "" ).pack( side='top')
            tk.Label( lf, text= str(tpl[1]), bg="lightgray" ).pack()
            lf.pack( side='left') 
        
        sub.update_idletasks()
        cansell = tk.Button( fr___, text= "閉じる", command= sub.destroy)
        cansell.bind( '<Return>', lambda event: sub.destroy())
        cansell.bind( '<Motion>', lambda event: None)
        cansell.bind( '<FocusOut>', lambda event: sub.destroy())
        cansell.pack( padx=2, pady=2)
        cansell.focus_force()         
        sub.mainloop()       
             
    def forget(root):
        children = root.winfo_children() #print(children)     #print(children,len(children),type(children))
        for child in children:
            child.destroy() 
                                
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。       
    lst = ls.customer()
    #anlys.lot(5,lst)
    anlys.wdgt( ls.start(),lst)
    #anlys.table( ls.start(),lst)
    #anlys.num(lst)[1]
    
