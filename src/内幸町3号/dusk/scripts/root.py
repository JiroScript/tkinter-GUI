import os.path
import sys
import tkinter as tk
import time
import call
import ext
import ls
import sti
import cum
import panda
from _tkinter import TclError
import data

class jumpback: 
    def __init__(self, a):
        self.a = a  
    def jump(self,*args):
        type(args)
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()
        lst = ls.customer()
        start = ls.start()
        my = lst[start][ls.kb()]
        num = 0
        for i,item in enumerate(lst[start:]):
            if my != item[ls.kb()]:
                num = i
                break                      
        return num + start         
    
    def back(self,*args):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()
        lst = ls.customer()
        start = ls.start()
        my = lst[start][ls.kb()]
        name = ""
        num = 0
        for i, item in enumerate( lst[start::-1] ):
            #print(item[ls.kb()])
            if my == item[ls.kb()] and name =="":
                num = i         
            elif my != item[ls.kb()] and name != item[ls.kb()] and i > 1 and name == "":
                num = num     
                break
            elif my != item[ls.kb()] and i == 1 and name == "":
                name=item[ls.kb()]
                num = i 
            elif name == item[ls.kb()]:
                num = i         
            elif name != item[ls.kb()] and name !="":
                my =""
                name =""
                break
        return start - num     
class wid(ls.sp):#window     
    def plus(start ,root):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()                 
        lst = ls.customer()
        winfo = root.winfo_width()
        widz = [item[ls.hb()] for item in lst] #width
        end = ls.end()        
        tub = [] 
        tin = 1 ##tin；缶〔英〕
        
        if start < len(lst):
            my = lst[start][ls.kb()]
            for i, long in enumerate( widz[ start:]):
                if type(long) != int :
                    ext.long( i,winfo)
                tub.append(long)
                now = start +len(tub)
                if winfo > sum(tub): 
                    end = now    
                elif winfo <= sum(tub):
                    if len(tub) != 1:
                        break
                    elif len(tub) == 1:
                        end = now
                        break
                
                if my == lst[ i + start][ ls.kb()]:
                    tin = len(tub)
                elif my != lst[ start + i][ ls.kb()] :
                    end   = start + tin
                    break  
                if ls.pg()[1] == lst[ start + i][ ls.pg()[0]]:
                    end   = start + tin                    #print(i,end,start,tin)
                    break  
                #print(lst[ start + i][ ls.pg()[0]])                print( len(lst), len(widz),start,end)
            wid( start, end, 0, 0, root).post() 
            ext.save( ls.dl()[3], start)
            ext.save( ls.dl()[4], end) 
            ext.RElord(False)##relord
    def minus(end,root):   
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()                 
        lst = ls.customer()
        widz = [item[ls.hb()] for item in lst] #width
        
        if ls.start() > 0 :
            end = ls.start()
            len([i for i in range(end)])
            edge= [i for i in range(end)][-1]###縁, 端,            #print(end, [l for l in range(end)], len([l for l in range(end)]))            print(edge)
            winfo = root.winfo_width()
            my = lst[edge][ls.kb()] #            ##print(" ",my,lst[edge][ls.kb())
            tub= []
            tin= []
            receptacle =[]#入れ物, 器物
            for long in reversed(widz[ :end]):#longs
                tub.append(long)
                now = end - len(tub)
                if winfo > sum(tub):
                    start = now
                    
                elif winfo <= sum(tub):
                    if len(tub) != 1 :
                        break
                    elif len(tub) == 1 :
                        start = edge
                        break
                
                if my != lst[ now][ ls.kb()]: 
                    tin.append(lst[ now][ls.mi()])
                    start =  start + len(tin)
                    break
                if ls.pg()[2] == lst[ now][ ls.pg()[0]]:
                    receptacle.append(lst[ now][ ls.pg()[0]])                    
                elif ls.pg()[1] == lst[ now][ ls.pg()[0]] and 0 != len(receptacle):
                    start = end - len(receptacle)
                    break       
                elif ls.pg()[1] == lst[ now][ ls.pg()[0]] and 0 == len(receptacle):
                    pass
                
            wid( start ,end ,0,0 ,root ).post() 
            ext.save( ls.dl()[3] ,start )
            ext.save( ls.dl()[4] ,end   )           
    def forget(root):
        children = root.winfo_children() #print(children)     #print(children,len(children),type(children))
        for child in children:
            child.destroy() 
            
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #
        root = ee_
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        wid.forget(root)
        lst = ls.customer()
        keylst = ls.kl() + ls.tm()
        cate_divi= ext.category(lst)[0]
        tub = []
        length = []        
        font=("メイリオ",ls.ft()[1]) 
        root.update_idletasks()#削除禁止：理由不明、削除すると最初のframeのwidth値が１になる。
        for i in range( aa_, bb_) if type(cc_) is int else range( aa_,bb_ )[::-1]:
            frame = tk.Frame(ee_)
            frame0 = tk.Frame(frame)
            ############################
            wr = ext.cnv_list( lst[i].get(ls.mm()[1]))##メモ１     
            for item in wr:
                tk.Label(frame0,text=ext.tategaki( item),bd=1,bg=ls.cl()[1],font=font).pack(side="right")
            wr = ext.cnv_list( lst[i].get(ls.mm()[2]))##メモ2     
            for item in wr:
                tk.Label(frame0,text=ext.tategaki( item),bd=1,fg=ls.cl()[3],bg=ls.cl()[1],font=font).pack(side="right")
            ############################
            frame0.pack(side="right")            
            frame1 = tk.Frame(frame,bg=ls.cl()[1])
            frame2 = tk.Frame(frame1)##新聞名
            frame2.pack()
            frame3 = tk.Frame(frame1)##部数                  
            frame3.pack(pady=1)    
                    
            labelframe = tk.LabelFrame(frame1,bg=ls.cl()[1])#raised, sunken, groove, ridge
            lab = tk.Label(labelframe,text= lst[i].get(ls.gs()),font = font,bg=ls.cl()[1],fg=ls.cl()[3] if lst[i].get( ls.ak()) ==ls.ak() else ls.cl()[0])
            lab.pack(padx=0,pady=0,side="top") 
            lab = tk.Label(labelframe,text="{0}月{1}日{2}～{3}月{4}日{5}迄　{6}".format(lst[i].get( ls.tm()[0] ),lst[i].get( ls.tm()[1] ),lst[i].get( ls.tm()[2] ),lst[i].get( ls.tm()[3] ),lst[i].get( ls.tm()[4] ),lst[i].get( ls.tm()[5] ),lst[i].get( ls.tm()[6] )) if lst[i].get( ls.tm()[0] ) !="" else ''
                           ,bg=ls.cl()[1],fg='blue' if lst[i].get( ls.tm()[6] ) =="ナシ" else 'black' if lst[i].get( ls.tm()[6] ) !="取置" else 'purple', relief="groove"if lst[i].get( ls.tm()[6] ) =="ナシ" else 'flat' if lst[i].get( ls.tm()[6] ) !="取置" else 'groove')
            lab.pack(padx=0,pady=0,side="top") 
            
            ############################名称1              
            lf = tk.Frame(labelframe)                           
            wr = ext.cnv_name( lst[i].get(ls.mi()))     
            for item in wr:
                btn_ = tk.Label(lf,text= ext.tategaki(item),relief ="flat",bg=ls.cl()[1],font=("",ls.ft()[2]) ,height=5)
                btn_.pack(padx=0,pady=0,side="right")##  
            lf.pack()
            labelframe.pack()
            ############################呼び出し        
            fmblank = tk.Frame(frame1)
            button = tk.Button(fmblank ,font=("",7),text= i ,name=F'lbl{i}',bg=ext.divi_clr(cate_divi, lst[ i][ ls.kb()]), fg=ext.divi_clr(cate_divi, lst[ i][ ls.kb()]))#
            button.bind("<1>",lambda event: call.call(event.widget["text"],2,3,4,tk.Toplevel()).post())##
            button.pack(side="top", fill=tk.BOTH)
            fmblank.pack(fill = tk.BOTH) 
            frame1.pack(side="right")              
            frame5 = tk.Frame(frame)
            ############################            
            wr7 = ext.cnv_list( lst[i].get(ls.mm()[3]))#メモ3     
            for item in wr7:
                tk.Label(frame5,text=ext.tategaki( item ),bd=1,bg=ls.cl()[1],font=font).pack(side="right")
            wr8 = ext.cnv_list( lst[i].get(ls.mm()[4]))##メモ４
            for item in wr8:
                tk.Label(frame5,text=ext.tategaki( item ),bd=1,bg=ls.cl()[1],fg=ls.cl()[3],font=font).pack(side="right")
            ############################
            tk.Label(frame5,text="",bd=3).pack(side="right")
            frame5.pack(side="right")
            frame9 = tk.Frame(frame1)
            frame9.pack(pady=1)        
            frame.pack(side="right" if type(cc_) is int else "left")
            
            #######################                
            for w in lst[i].keys():
                ###################新聞名
                if w not in keylst:
                    tk.Label(frame2 ,width=2 ,text=ext.gomoji(w) ,font=ext.font(w) ,fg=ext.font_clr(lst[i], w) ,bg= ext.clr(w) ) .pack(padx=0,pady=0,side="right")
                ###################部数                     
                if w not in keylst:
                    if not w in sti.sti.wk(): 
                        tk.Label(frame3,width=2, text= ext.ichi(lst[i].get(w)), font = font,relief= ext.relieF(w),fg=ls.cl()[0] ,bg=ls.cl()[1] ).pack(side="right")
                    elif w in sti.sti.wk():
                        tk.Label(frame3,width=2, text= ext.ichi(lst[i].get(w)), font = font,relief=None,fg=ls.cl()[1],bg=ls.cl()[2]).pack(side="right")
                ###################frame9                
                if w not in keylst and None != None:# ##
                    if not w in sti.sti.wk():#ls.cl()[0]
                        mini = data.anlys.minimum( lst, lst[ i][ls.kb()], w)
                        tk.Label(frame9, width=2, text= data.anlys.ext( lst, i, lst[ i][ls.kb()], w, mini), font= font, relief= ext.relieF(w), fg=data.anlys.fg( lst, i, lst[ i][ls.kb()], w, mini), bg=ls.cl()[1] ).pack(side="right")
            #######################       
            btn1 = tk.Button(root ,text="＜" ,command=lambda : wid.plus( ls.end() ,root) ,font=("",ls.ft()[0]) )#command=lambda : turn()
            btn1.place(relx=0.004, rely=0.005)    # このパーツをウィンドウにセット
            root.focus_set() 
            root.bind('<Return>', lambda event:wid.plus( ls.end(),root) ) 
            root.bind('<Return>', lambda event:wid.rETURN(root,status)) # ④
            root.bind('<MouseWheel>', lambda event:data.anlys.wheel(event, ls.start(), lst) ) #
            root.bind('<2>', lambda event:panda.cum(None,None,None,None,tk.Toplevel()).post() ) #部数
            root.bind('<3>', lambda event:wid.minus( ls.start(),root) ) 
            root.bind('<FocusIn>', lambda event:wid.fOCUS(root,status))
            root.bind('<FocusOut>', lambda event:status.configure( text='Focus Out',bg = "red" ,fg='white') )
            tk.Button(root, text="<<", command = lambda:wid.plus( jumpback(root).jump(), root), font=("", ls.ft()[0]) ).place(relx=0.12, rely=0.005)
            tk.Button(root, text="曜日", command = lambda:sti.sti(None,None,None,None,ee_).post() ,font=("",ls.ft()[0]) ).place(relx=0.22, rely=0.005) 
            status= tk.Label(root)
            status.place(relx=0.42, rely=0.005) 
            """            cansell = tk.Button(root ,text="終了" ,relief="groove" ,font=("",ls.ft()[0]) ,bd=5 )            cansell.bind('<Double-1>' ,lambda e:root.destroy())            cansell.place(relx=0.42, rely=0.005)             """
            tk.Button(root, text="■", command =lambda :wid.plus( 0, root), font=( "", ls.ft()[0]) ).place(relx=0.35, rely=0.005)###零
            if None != None:
                tk.Button(root, text="部数", command = lambda:panda.cum(None,None,None,None,tk.Toplevel()).post() ,font=("",ls.ft()[0]) ).place(relx=0.57, rely=0.005)
            tk.Button(root, text="部数", command = lambda:data.anlys.table( ls.start(),lst) ,font=("",ls.ft()[0]) ).place(relx=0.57, rely=0.005)
            tk.Button(root, text="編集", command = lambda:cum.table.post() ,font=("",ls.ft()[0])).place(relx=0.69, rely=0.005) 
            tk.Button(root, text=">>", command = lambda:wid.plus( jumpback(root).back() ,root) ,font=("",ls.ft()[0]) ).place(relx=0.79, rely=0.005)
            btn6 = tk.Button(root, text = "＞", command=lambda :wid.minus( ls.start(),root) ,font=("",ls.ft()[0]) )
            btn6.place( relx=0.90, rely=0.005) # このパーツをウィンドウにセット #rely=0.91
                                          
            root.update_idletasks()
            length.append(frame.winfo_width())
            ############################幅:
            if lst[i][ls.hb()] != frame.winfo_width():
                ext.long(i,frame.winfo_width())
            ############################
            ############################
            if dd_ == ls.vc()[0]: 
                tub.append(frame.winfo_width())
                wid.forget(root)
                frame.destroy()            
            ############################
            elif dd_ != ls.vc()[0]:   
                pass
        
    def fOCUS( root, status):
        root.lift()
        root.focus_force()#最前列表示？
        root.update_idletasks()
        dct = ext.reLORD()[ ls.dl()[5]]#"relord"
        status.configure( text='Focus In', bg = "blue", fg='white')      
        status.bind('<Configure>', None)
        if dct ==True:
            start = ls.start()
            if start == len(ls.customer()):###末尾の顧客情報を削除する際のエラー回避。
                wid.minus( ls.start() ,root)
            else:
                wid.plus( start, root)
            ext.RElord( False)
        root.update_idletasks()
            
    def rETURN( root, status):#③
        timE = time.perf_counter()
        ext.timer( root, timE, status)
        try:
            wid.plus( int( ls.num()[ ls.dl()[4]]), root)
        except TclError:
            pass
        
class main:
    def post():
        root = tk.Tk()
        root.title( "組手roid")#window
        root.option_add( '*font', 'Meiryo' +' '+ ls.ft()[2])##YuGothic
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.state( 'zoomed') if ls.zm() == True else root.geometry( ls.ge( ww, wh)) 
        starting = time.time()        

        root.lift()
        root.focus_force()
        root.update_idletasks()
        ###root.overrideredirect(1)#ウィンドウのタイトルバーを消す             
        lst=ls.customer()
        if root.winfo_width() != ls.winfo()["w"]:
            wid(0,len(lst),0,ls.vc()[0],root).post()#ls.vc()[0]="longs"
            ext.winfo(root.winfo_width())
        start = ls.start()
        wid.plus( start,root)        
        ###root.protocol("WM_DELETE_WINDOW",lambda:print('hello')) 
        elapsed_time = time.time() - starting
        print ("{0}".format(elapsed_time) + "[sec]") 
        root.mainloop()     
        
if __name__ == '__main__': 
    main.post()