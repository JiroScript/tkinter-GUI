import os
import sys
import pathlib
import tkinter as tk
import time
import datetime
import math
from ast import literal_eval
sys.path.append(os.path.join('../dawn/', 'scripts'))
import ls
import panda
import ext
import data

di = '../src/'###directory:「住所録」
ct = '/dawn'
ory= '/setting/customer.txt'
ktg = ls.kt()[0]

class anlys():###数値,analysis:解析,
    def post():
        dct= anlys.drctr()
        d__=anlys.total()
        sub = tk.Tk()
        anlys.table(None, dct, d__, sub)
        
    def re(event, dct, d__, sub):
        if stng.ft()[1] in event.widget["font"]:###event.widget["font"]はテキスト情報
            txt= event.widget["text"]
            txt= txt.replace('\n','')
            txt= txt.replace(' ','')
            txt= txt.replace('丨','ー')
            dct= anlys.drctr()
            d__=anlys.total()
            anlys.table(txt, dct, d__, sub)
            
        elif event.widget["text"] in ls.kt():
            dct= anlys.drctr()
            d__= anlys.total()
            #print(dct)
            anlys.table(None, dct, d__, sub)
            
        elif event.widget["text"] in dct.keys():
            txt= event.widget["text"]
            dct= anlys.drctr()
            d__= anlys.total()
            anlys.table(txt, dct, d__, sub)
        
    def drctr():###directory
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        os.path.exists('../src/内幸町8号')#C:\Users\jiro\Documents\WPy64-3741\scripts
        os.path.exists('./lan.py')
        os.listdir(path= './../src/')
        os.path.exists('C:/Users/Public/Videos')#DESKTOP-32KSG98/Videos
        
        os.getcwd()#カレントディレクトリを表示
        ph= '../src/'
        pathlib.Path(ph)
        t = os.path.getmtime(ph)
        d = datetime.datetime.fromtimestamp(t)
        t, d
        [ li for li in os.listdir( path= ph) if os.path.isdir( os.path.join( ph, li))]
        dct= {}
        for re in os.listdir( path= di):
            if os.path.isdir( os.path.join(di, re)) and os.path.exists(di+re+ct+ory):
                dct[re]= data.anlys.num( anlys.customer(di+re+ct+ory))[0]
        dct= { re:data.anlys.num( anlys.customer(di+re+ct+ory))[0] for re in os.listdir(path= di) if os.path.isdir(os.path.join(di, re)) and os.path.exists(di+re+ct+ory)}
        dct
        return dct
    
    def total():
        d__= {}
        for re in os.listdir( path= di):
            if os.path.isdir( os.path.join( di, re)) and os.path.exists(di+re+ct+ory):
                di_ = data.anlys.num( anlys.customer(di+re+ct+ory))[0]
                for tp in di_.items():
                    d__.setdefault( tp[0], 0)
                    d__[ tp[0]] += tp[1]
        panda.cum.fm__(d__)
        return d__
    
    def table( txt, dct, d__, sub):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        start = time.time()  
        sub = sub
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.title("紙分け表") 
        sub.geometry( stng.ge(ww,wh) )
        sub.option_add( '*font', 'TkDefaultFont'+' '+ stng.ft()[2])##YuGothic
        anlys.reflexion( txt, dct, d__, sub)

        frame= tk.Frame(sub)#, bg="teal"
        fra__= tk.Frame(frame)   
        fra__.pack(pady=4)       
        fram_= tk.Frame(frame)  
        cvs = panda.table.scrollbar(frame,ww*3/2, wh)
        lf= tk.Frame(cvs)  
        lf.pack(padx=4) 
        fram_.pack()   
        frame.pack() 
        dc = panda.cum.fm_t(d__) # {'ト': None, '産': None, 'サ': None, 'ヨ': None, 'マ': None, 'ア': None, '工': None, '日産': None, '流通': None, 'ヴェリタス': None, '自動車': None, '海事': None, '建通': None, '電波': None, 'でんき': None, 'ぜんせき': None, 'せんけん': None, '農業': None, '木材': None, 'ガイド': None, '報知': None, '日刊スポ': None, 'スポニチ': None, '東スポ': None, 'デイリー': None, 'F・T': None, 'A': None, 'Y': None, 'US版': None, 'NYT': None, '朝日小学生': None, '碁': None, 'ゲンダイ': None, 'フジ': None}
        # {'内幸町1号': {'ア': 29, 'マ': 26, 'ヨ': 33, 'サ': 47, '産': 20, 'ト': 18, 'A': 4, '農業': 1, '報知': 1, 'スポニチ': 1, '碁': 1, '日刊スポ': 1}, '内幸町3号': {'ア': 50, 'マ': 44, 'ヨ': 51, 'サ': 87, '産': 1, '工': 14, 'ト': 41, '日産': 23, '流通': 8, 'ヴェリタス': 30, 'US版': 7, 'F・T': 7, 'ガイド': 7, '農業': 4, '海事': 5, 'でんき': 9, '建通': 1, 'A': 8, 'Y': 3, '日刊スポ': 8, 'デイリー': 4, '電波': 4, '朝日小学生': 2, '朝中高Ｗ': 2, 'ゲンダイ': 3, '東スポ': 1, 'NYT': 1, 'スポニチ': 2},
        d__= d__ # {'ア': 557, 'マ': 509, 'ヨ': 555, 'サ': 721, '産': 371, 'ト': 416, 'A': 32, '農業': 20, '報知': 2, 'スポニチ': 6, '碁': 4, '日刊スポ': 20, '工': 75, '日産': 133, '流通': 29, 'ヴェリタス': 83, 'US版': 9, 'F・T': 20, 'ガイド': 14, '海事': 24, 'でんき': 149, '建通': 2, 'Y': 12, 'デイリー': 8, '電波': 10, '朝日小学生': 6, '朝中高Ｗ': 4, 'ゲンダイ': 10, '東スポ': 2, 'NYT': 1, 'ぜんせき': 14, 'フジ': 2, 'Bアイ': 1, '自動車': 6, '木材': 1, 'せんけん': 4}
        (txt, lf, dc,  dct, d__,)
        if None != None:
            pass
            #
            anlys.disp( txt, lf, dc,  dct, d__, sub)
        elif txt == None:
            pass
            #
            anlys.itrtn( txt, lf, dc,   dct, d__, sub)
        elif txt in dct.keys():
            anlys.itr__( txt, lf, dc,   dct, d__, sub)
        else:
            anlys.itrtn( txt, lf, dc,   dct, d__, sub)
            
        anlys.bottn( txt, fra__, dc,   dct, d__, sub)
        cansell = tk.Button( fra__, text= "閉じる", command= sub.destroy, width=8)
        cansell.bind( '<FocusOut>', lambda event: sub.destroy())
        cansell.bind( '<Return>', lambda event: sub.destroy())
        cansell.pack( padx=2 ,pady=2, side="right")
        cansell.focus_force()  

        elapsed_time = time.time() - start
        print ("{0}".format(elapsed_time) + "[sec]")   
        sub.mainloop()
        
    def fg_fnt( event, sub):
        if event.widget["fg"]=="SystemButtonText":
            event.widget["fg"]="SystemInfoText"#ツールチップの文字色
            event.widget["font"]="{} 18"
        elif event.widget["fg"]=="SystemInfoText":
            event.widget["fg"]="SystemButtonText"
            event.widget["font"]="{} 16"            
        sub.update_idletasks()
                    
    def itr__(txt, lf, dc, dct, d__, sub):###反復:Iteration
        fnt= 16
        keylst = anlys.colla(ktg)
        btn1= tk.Button( lf, text= txt, relief ="groove", font= ("", fnt))
        btn1.bind("<1>", lambda event: anlys.fg_fnt( event, sub))
        
        btn1.grid( row= 1, column= 0, padx=4)
        for c, li in enumerate( dc.keys()):
            if li in keylst and li in dct[txt].keys() or li in dct[txt].keys():
                #print(di,li)
                btn2= tk.Label( lf, text= ext.gomoji(li), relief ="groove",  bg= ext.clr(li), fg=ext.fg(li), font= ("", fnt))
                btn2.grid( row= 0, column= c+1)
                lbl= tk.Button( lf, text= str( dct[txt][li]), relief="groove", bg=ls.cl()[2] )
                lbl.configure( font= ("", fnt))
                lbl.bind("<1>", lambda event: anlys.fg_fnt( event, sub))
                lbl.grid( row= 1, column= c+1)
                
    def glb(event):#グローバル変数に代入
        global ktg
        txt= event.widget["text"]
        ktg= txt
        return event
    
    def gl_(event):#グローバル変数に代入
        global ktg
        txt= event.widget["text"]
        ktg= txt
        return event
        
    def bottn( txt, fra__, dc,   dct, d__, sub):###
        num= len( ls.kt())
        nm = 4 #横に表示するwidgetの上限数
        ceill= math.ceil(num / nm)# 切り上げ
        for n in range(ceill):  
            fr___= tk.Frame(fra__)
            for i, li in enumerate( ls.kt()[n*nm:nm*n+nm]):  
                [n*nm, nm*n+nm]
                btn= tk.Button( fr___, text= li )
                btn.configure( bg= anlys.bg( ktg,li))
                btn.configure( fg= anlys.fg( ktg,li))
                btn.pack(side="left")
                btn.bind( '<1>', lambda event: anlys.re( anlys.glb(event), dct, d__, sub))#    def re(event, dct, d__, sub):
            fr___.pack()
        
    def colla(mn):###collation:照合
        if ls.kt()[0] == mn:###一般紙
            return ls.nw()[0] 
        elif ls.kt()[1] == mn:###産業紙
            return ls.nw()[1]
        elif ls.kt()[2] == mn:###業界紙
            return ls.nw()[3]  + ls.nw()[4] + ls.nw()[5] + ls.nw()[6] + ls.nw()[7]
        elif ls.kt()[3] == mn:###金融紙
            return ls.nw()[2]
        elif ls.kt()[4] == mn:###スポーツ紙
            return ls.nw()[10] 
        elif ls.kt()[5] == mn:###海外紙
            return ls.nw()[11] 
        elif ls.kt()[6] == mn:###国内英字紙
            return ls.nw()[12] 
        elif ls.kt()[7] == mn:###青少年向き
            return ls.nw()[13] 
        elif ls.kt()[8] == mn:###レジャー・趣味
            return ls.nw()[14] 
        elif ls.kt()[9] == mn:###一般夕刊紙
            return ls.nw()[15] 
        elif ls.kt()[10] == mn:###各種の縮刷版・その他
            return ls.nw()[16] + ls.nw()[17]
        elif ls.kt()[11] == mn:###全て
            return [ ii for i in ls.nw() for ii in i]
        
    def itrtn(txt, lf, dc, dct, d__, sub):###反復:Iteration
        keylst = anlys.colla(ktg)
        for r, di in enumerate( dct):  
            btn1= tk.Button( lf, text= di)
            btn1.grid( row= r+1, column= 0)
            btn1.bind( '<1>', lambda event: anlys.re( event, dct, d__, sub))
           
            for c, li in enumerate( dc.keys()):
                if li in keylst and li in dct[di].keys() :
                    btn2= tk.Button( lf, text= ext.gomoji(li),  bg= ext.clr(li), fg=ext.fg(li))
                    btn2.configure( font= ("",anlys.fn( txt,li)))
                    btn2.grid( row= 0, column= c+1)
                    btn2.bind("<1>", lambda event: print( event.widget.grid_info()['column']))
                    btn2.bind("<1>", lambda event: anlys.re( event, dct, d__, sub))
                    
                    lbl= tk.Label( lf, text= str( dct[di][li]), relief="groove", bg=ls.cl()[2] )
                    lbl.configure( font= ("", anlys.fn( txt,li)))
                    lbl.configure( bg= anlys.bg( txt,li))
                    lbl.configure( fg= anlys.fg( txt,li))

                    lbl.grid( row= r+1, column= c+1)
                    tk.Label( lf, text= str( d__[li]), relief="groove", bg="lightgray", font=("",stng.ft()[1])).grid( row= len(dct)+1, column= c+1)  ##,fg=ext.fg(lst[di][li]), bg= ext.clr(lst[di][li])
                
        list(dc).index(txt) if txt != None else ""

    def fn(txt,li): # if txt==li else ("",12)
        #print( txt, li)
        if txt !=li :
            return stng.ft()[1]
        elif txt == li : 
            return stng.ft()[0]
    def bg(txt,li): 
        if txt !=li :
            return ls.cl()[2]
        elif txt == li : 
            return ls.cl()[0]
    def fg(txt,li): 
        if txt !=li :
            return ls.cl()[0]
        elif txt == li : 
            return ls.cl()[2]
        else:
            return "red"
       
    def trig(txt, dct, d__, sub):
        txt= txt.replace('\n','')
        txt= txt.replace(' ','')
        anlys.reflexion( txt, dct, d__, sub)

    def reflexion(txt, dct, d__, sub):#反射,反映
        children = sub.winfo_children() 
        for child in children:
            child.destroy() 

    def disp( txt, lf, dc,   dct, d__, sub):#lf, dct, dc, d__, sub
        for r, di in enumerate( dct):   
            tk.Label( lf, text= di, relief="groove").grid( row= r+1, column= 0)
            for c, li in enumerate( dc.keys()):
                tk.Label( lf, text= ext.gomoji(li), relief="groove",fg=ext.fg(li), bg= ext.clr(li)).grid( row= 0, column= c+1)
                try:
                    tk.Label( lf, text= str( dct[di][li]), relief="groove", bg="white").grid( row= r+1, column= c+1)  ##,fg=ext.fg(lst[di][li]), bg= ext.clr(lst[di][li])
                    tk.Label( lf, text= str( d__[li]), relief="groove", bg="lightgray").grid( row= len(dct)+1, column= c+1)  ##,fg=ext.fg(lst[di][li]), bg= ext.clr(lst[di][li])
                except KeyError:
                    tk.Label( lf, text= "", relief="groove").grid( row= r+1, column= c+1) 
                    tk.Label( lf, text= "", relief="groove", bg="lightgray" ).grid( row= len(dct)+1, column= c+1)  ##,fg=ext.fg(lst[di][li]), bg= ext.clr(lst[di][li])
            
    def customer(directory): 
        file_ = directory
        with open(file_, "r", encoding='utf-8') as f:
            data_list = f.read()        
        text = data_list.replace(" ","")
        lst = literal_eval(str(text))#文字列をリストや辞書に変換
        return lst
    
    def forget(root):
        children = root.winfo_children() #print(children)     #print(children,len(children),type(children))
        for child in children:
            child.destroy() 
                
class stng():#setting
    def ge(ww,wh):###
        keylst=[]
        if stng.zm() == True:
            keylst = str(int(ww))+"x"+str(int(wh))+"+"+str(0)+"+"+str(0)
        elif stng.zm() == False:
            keylst = str(int(ww/2-50))+"x"+str(int(wh/2))+"+"+str(0)+"+"+str(0)
        return keylst
    
    def zm(): ###最大化
        return False
    
    def ft(): #font
        return ['14','13','9']

if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。       
    anlys.post()