import tkinter as tk
import os.path
import time
import datetime
import ext
import ls
import sti
import cum
import panda
import data
import temp
import auxi
import fx
import prnt
import sync
import log
import mgmt

class wid(ls.sp): # window    
    def plus( start, root):
        try: # winfo .TclError回避
            lst = ls.customer()
            winfo = root.winfo_width() # 590 
            widz = [ d[ls.hb()] for d in lst] #
            
            if start < len(lst):
                tub, kb, kk = [], lst[start].get('区分'), lst[start].get('区間')
                
                for i, nn in enumerate( widz[ start:]): # nn (natural number:自然数), 自然数とは「正の整数」を意味する言葉
                    tub.append(nn)
                    num = len(tub) # バケツ
                    if winfo < sum(tub): 
                        end = start + i if i != 0 else ( start +1) # 後切り
                        fx.r.u('winf',i,start,end,num,tub,sum(tub))
                        break
                    elif len(lst) > (start + num) and kb != lst[ start + num ]['区分']: 
                        end = start + num # 前切り 
                        fx.r.u('区分',i,start,end,num,tub,sum(tub))
                        break
                    elif len(lst) > (start + num) and kk != lst[ start + num ]['区間']: 
                        end = start + num # 
                        fx.r.u('区間',i,start,end,num,tub,sum(tub))
                        break
                    elif '有効' == lst[ start + i][ '改ページ'] :
                        end = start + num # 後切り
                        fx.r.u('pg  ',i,start,end,num,tub,sum(tub))
                        break
                    else : # 
                        end = start + num
                        fx.r.u('else',i,start,end,num,tub,sum(tub))
                    
                fx.r.u(start,end)  
                renew = auxi.adju.renw( start, end) # start,endの値、 renewの値と比較、　必要なら変更、
                start = renew[0] 
                end =   renew[1]
                wid( start, end, 0, 0, root).post() 
                ext.save( ls.dl()[3], start)
                ext.save( ls.dl()[4], end) 
                ext.renew( start, False, os.path.basename(__file__))
        except Exception as e:
            pass
            ( str(type(e)) , e.args, str(e))#e.message, 
            
    def minus( root):   
        lst = ls.customer()
        widz = [ d[ls.hb()] for d in lst] #width
        
        if ls.start() > 0 :
            end = ls.start() 
            edge = [i for i in range(end)][-1] # 縁, 端, 配列の末尾   
            winfo = root.winfo_width()
            tub, kb, kk = [], lst[edge]['区分'], lst[edge]['区間'] 
            start = 0
            for i, nn in enumerate( widz[:end][::-1] ):
                tub.append(nn)
                num = len(tub) # バケツ
                try:
                    if winfo < sum(tub):
                        start = end - i # len(tub[:-1])
                        fx.r.d('winf', start, end, num, tub, lst)
                        break
                    
                    elif kb != lst[ end - num]['区分']: 
                        start = end - i # len(tub[:-1])
                        fx.r.d('区分', start, end, num, tub, lst)
                        break               
                    elif kk != lst[ end - num]['区間']: 
                        start = end - i # len(tub[:-1])
                        fx.r.d('区間', start, end, num, tub, lst)
                        break                         
                    elif ls.pg()[1] == lst[ end - num][ ls.pg()[0]] and num > 1 :
                        start = end - i # len(tub[:-1])
                        fx.r.d('pg  ', start, end, num, tub, lst)
                        break    
                    else:
                        start = end - len(tub)
                        start = start if start != end else (start - 1)
                        fx.r.d('else', start, end, num, tub, lst)

                except Exception as e:
                    pass
                    ( str(type(e)) , e.args, e.message, str(e))
            
            wid( start ,end ,0,0 ,root ).post() 
            ext.save( ls.dl()[3] ,start )
            ext.save( ls.dl()[4] ,end   )      
                 
    def forget(root):
        children = root.winfo_children() 
        for child in children:
            child.destroy() 
        
    def post(self):        
        aa_, bb_, cc_, dd_, ee_ = self.a, self.b, self.c, self.d, self.e 
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        root = ee_
        wid.forget(root)
        lst = ls.customer()
        root.title( lst[aa_].get(ls.kb()) + '    ' + str(bb_) + "/" + str(len(lst))) #  
        root.update_idletasks() # 削除禁止：理由不明、削除すると最初 のframeのwidth値が１になる。
        font, fon_ = ( 'TkDefaultFont', ls.ft()[0]), ( 'TkDefaultFont', ls.ft()[1]) # 'メイリオ'    
        #
        now = datetime.datetime.now() # モジュール（module）
        today = now.strftime('%Y-%m-%d') #'2022-01-01'
        day_of_week = ['月', '火', '水', '木', '金', '土', '日'][now.weekday()] # '月'
        
        issue = sti.L.S( ls.week(), sti.sti.ph(), day_of_week) # 発行・出版、 ['日産', '工', '流通', '自動車', 'でんき', '電波', '海事', '通信', '農業']
        disp = ls.setting()['表示'] # '全表示' or '曜日・祝日別'
        #
        src = sync.dr.src() # src・sysフォルダ配下であればTrueを返す

        for i in range( aa_, bb_) if type(cc_) is int else range( aa_, bb_)[::-1]:
            frame = tk.Frame(ee_)
            frame0 = tk.Frame(frame)
            # 
            dic = lst[i]
            wr = ext.lmen( dic.get(ls.mm()[1]), 11, '') # メモ１     
            for item in wr:
                tk.Label( frame0, text= ext.tategaki( item), bg= sti.S.M_S( day_of_week, item), relief= sti.T.M_S( today, item)[0], bd= sti.T.M_S( today, item)[1], font=font ).pack(side='right')
            wr = ext.lmen( dic.get(ls.mm()[2]), 11, '') # メモ2     
            for item in wr:
                tk.Label( frame0, text= ext.tategaki( item), bg= sti.S.M_S( day_of_week, item), relief= sti.T.M_S( today, item)[0], bd= sti.T.M_S( today, item)[1], font=font).pack(side='right')
            # 
            frame0.pack(side='right')            
            frame1 = tk.Frame(frame,bg=ls.cl()[1])
            frame2 = tk.Frame(frame1) # 新聞名
            frame2.pack()
            frame3 = tk.Frame(frame1) # 部数                  
            frame3.pack(pady=1)    
                    
            labelframe = tk.LabelFrame( frame1, bg= temp.cnfg.bg(dic) )
            tk.Label( labelframe, text= dic.get(ls.gs()), font = font, bg=ls.cl()[1],fg=ls.cl()[3] if dic.get( ls.ak()) ==ls.ak() else ls.cl()[0]).pack(padx=0,pady=0,side='top') 
            # 一時止
            tk.Label( labelframe, text= temp.cnfg.tx(dic), font = ('TkDefaultFont', ls.ft()[1]), fg= temp.cnfg.fg(dic), bg= temp.cnfg.bg(dic) ).pack( padx=0, pady=0, side='top') 
            # 名称1              
            lf = tk.Frame(labelframe)                           
            wr = ext.lmen( dic.get(ls.mi()), 5, '')  
            for item in wr:
                btn_ = tk.Label(lf,text= ext.tategaki(item),relief ='flat',bg=ls.cl()[1],font=('TkDefaultFont',ls.ft()[1]) ,height=5)
                btn_.pack(padx=0,pady=0,side='right')##  
            lf.pack()
            labelframe.pack()
            # 呼び出し        
            fmblank = tk.Frame( frame1)
            auxi.button( **{ 'master':fmblank, 'text': i , 'font':('TkDefaultFont',7), 'fg':ext.divi_clr( lst, dic[ ls.kb()]), 'bg':ext.divi_clr( lst, dic[ ls.kb()]), 'side':'top', 'fill':tk.BOTH })
            fmblank.pack(fill = tk.BOTH) 
            frame1.pack(side='right')              
            frame5 = tk.Frame(frame)
            # メモ3             
            wr7 = ext.lmen( dic.get(ls.mm()[3]), 11, '')   
            for item in wr7:
                tk.Label( frame5, text=ext.tategaki( item ), bg= sti.S.M_S( day_of_week, item), relief= sti.T.M_S( today, item)[0], bd= sti.T.M_S( today, item)[1], font=font).pack(side='right')
            # メモ４
            wr8 = ext.lmen( dic.get(ls.mm()[4]), 11, '')
            for item in wr8:
                tk.Label( frame5, text=ext.tategaki( item ), bg= sti.S.M_S( day_of_week, item), relief= sti.T.M_S( today, item)[0], bd= sti.T.M_S( today, item)[1], font=font).pack(side='right')
            # 
            tk.Label(frame5,text='',bd=3).pack(side='right')
            frame5.pack(side='right')
            frame9 = tk.Frame(frame1)
            frame9.pack(pady=1)        
            frame.pack(side='right' if type(cc_) is int else 'left')
            south= tk.Frame(root)
            south.place( relx=0.002, rely=0.919)  
            #                 
            for s in dic.keys():
                ( s ) # ア
                if s not in ls.kl() + ls.tm():
                    # 銘柄
                    auxi.label( **{ 'master':frame2, 'text': s , 'font':font, 'fg':ext.font_clr(dic, s ), 'bg':ext.clr( s ), 'width':2, 'side':'right' }).brand()
                    # 部数
                    auxi.label( **{ 'master':frame3, 'text':dic[ s ], 'font':font, 'relief':sti.S.S_S_L( s , disp, issue), 'fg':ls.cl()[0], 'bg':ls.cl()[1], 'width':2, 'side':'right' }).quantity()
         
                    # frame9 , 残りの部数, 区分・区間          
                    auxi.nine.wdgt( frame9, i, s, disp, issue, font, lst)
                    
            # 部数の表示、区分、最初
            if  aa_ == i : 
                data.cfg.txx( south, aa_, i, lst)
                
            # 幅:
            root.update_idletasks()
            if src == False and dic[ls.hb()] != frame.winfo_width(): # '幅'の保存値と現在値が異なるか、
                 ext.long( i, frame.winfo_width()) # '幅'を保存。
            # 一斉再計測、root.winfo_width()が変更された場合に、            
            auxi.wid.reme(dd_,root)
            
        wid.gdgt( root, fon_, aa_, bb_, i, lst)
        # , 
    def gdgt( root, fon_, aa_, bb_, i, lst ):
        root.focus_set() 
        dct = lst[aa_]
        btn1 = tk.Button(root ,text='＜' ,command=lambda : wid.plus( ls.end() ,root ) ,font= fon_ )#command=lambda : turn()
        btn1.place(relx= 0.005, rely= 0.005)    # このパーツをウィンドウにセット
        tk.Button(root, text='<<', command = lambda:wid.plus( auxi.jump(root).front(), root), font= fon_ ).place(relx=0.07, rely=0.005)
        tk.Button(root, text='St', command = lambda:sti.sti.post( tk.Toplevel()) ,font= fon_ ).place(relx=0.11, rely=0.005) 
        tk.Button(root, text='Tb', command = lambda:cum.gdgt.table( ls.start(), ls.customer(), tk.Toplevel()) ,font= fon_ ).place(relx=0.14, rely=0.005) 
        tk.Button(root, text='Pp', command = lambda:prnt.gdgt.post( tk.Toplevel()) ,font= fon_ ).place(relx=0.18, rely=0.005) 
        tk.Button(root, text='■', command = lambda :wid.plus( 0, root), font= fon_ ).place(relx=0.23, rely=0.005)###零
        status= tk.Label(root)
        status.place(relx=0.29, rely=0.005) 
        root.bind('<Return>', lambda event:wid.go(root, status)) # plus | ダブルクリック禁止
        root.bind('<Return>', lambda event:auxi.wid.SetCursorPos( root.winfo_width()//2, root.winfo_reqheight()//2),"+" ) # カーソル位置中央へ
        root.bind('<MouseWheel>', lambda event:None if event.delta > 0 else None ) #
        root.bind('<2>', lambda event:mgmt.cum.post(tk.Toplevel()) ) # 部数
        root.bind('<3>', lambda event:wid.minus( root) ) 
        root.bind('<FocusIn>', lambda event:wid.fOCUS( root,status))
        root.bind('<FocusOut>', lambda event:status.configure( text= ' ' + 'Focus Out' + ' ', bg= 'red' , fg= 'white') )
        tk.Label(root, text= data.cfg.kb(aa_, dct), font=('TkDefaultFont', ls.ft()[0], 'bold') ).place(relx=0.39, rely=0.005) # 区分を表示
        tk.Label(root, text= data.cfg.kk(aa_, dct), font=('TkDefaultFont', ls.ft()[0], 'bold'), fg= None if data.cfg.kk(aa_, dct) == '' else 'teal', bg= None if data.cfg.kk(aa_, dct) == '' else 'white').place(relx=0.62, rely=0.005)
        tk.Button(root, text='§', width=1, font= fon_, command=lambda:wid.rem(root)).place(relx=0.65, rely=0.005)
        tk.Button(root, text='Sc', command =  lambda :data.anlys.wdgt(ls.start(), lst, tk.Toplevel()) ,font= fon_ ).place (relx=0.69, rely=0.005)
        tk.Button(root, text='Cu', command = lambda:mgmt.cum.post(tk.Toplevel()) ,font= fon_ ).place(relx=0.74, rely=0.005)
        tk.Button(root, text='Rg', command = lambda:log.wdgt.actv(tk.Tk()), font= fon_ ).place(relx=0.79, rely=0.005)
        tk.Button(root, text='Tl', command = lambda:data.anlys.table(lst, ls.nw()[0], tk.Toplevel()) ,font= fon_ ).place(relx=0.84, rely=0.005) 
        tk.Button(root, text='>>', command = lambda:wid.plus( auxi.jump(root).back(), root), font= fon_ ).place(relx=0.88, rely=0.005)
        tk.Button(root, text='＞', command = lambda:wid.minus( root) ,font= fon_ ).place( relx=0.94, rely=0.005) # このパーツをウィンドウにセット 
        tk.Label(root, text= data.cfg.east( aa_, i, lst), font=( 'TkDefaultFont', ls.ft()[0]) ).place(relx=0.96, rely=0.09) # '◀'
        tk.Label(root, text= data.cfg.west( bb_, i, lst), font=( 'TkDefaultFont', ls.ft()[0]) ).place(relx=0.00, rely=0.09) # '▶'
        root.update_idletasks()
        #
        ext.renew( False, False, False) # 画面リロード
        
    def fOCUS( root, status):
        root.lift()
        root.focus_force() # 最前列表示？
        root.update_idletasks()
        renew = ext.reader('renew.txt')

        status.configure( text= ' ' + 'Focus In' + ' ', bg = 'blue', fg='white')      
        status.bind('<Configure>', None)
        if renew['relord'] == True:
            start = ls.start()
            if start >= len(ls.customer()): # 末尾の顧客情報を削除する際のエラー回避。
                wid.minus( root)
            else:
                wid.plus( start, root)
        root.update_idletasks()
            
    def go( root, status):# Enter, 進む、データ更新後、反映。
        # ダブルクリック禁止。
        auxi.duble_click.ban( time.perf_counter()) # 788.3213283
        # 進む
        wid.plus( ls.num()['end'], root) 
        try:
            # ファイルを開く
            if ls.setting()[ '音声' ] == '有':
                os.startfile( r'.\sund.py', operation= 'open') # ♪,システム音を鳴らす。    
                os.startfile( r'.\vox.py',  operation= 'open') # 相対パスで指定するとき、パス区切り文字に「/(スラッシュ)」を使用すると動作しません。
        except :
            pass
            
    def rem( root): # 部分的再計測,remeasurement:再計測
        wid( ls.start(), ls.end(), 0, '再計測', root).post()
        wid.plus( ls.start(), root)
        
class main:
    def post():
        root = tk.Tk()
        root.option_add( '*font', 'Meiryo' +' '+ ls.ft()[2])
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.state( 'zoomed') if ls.zm() == True else root.geometry( ls.ge( ww, wh)) 
        starting = time.time()        
        
        root.lift()
        root.focus_force()
        root.update_idletasks()
        sync.dr.synq#( 'retrieve') # 同期、ファイルを取得  
        lst = ls.customer()
        tk.Button(root, text='回復', command = lambda :wid.plus( 0, root), fg='green', font= ( 'TkDefaultFont' , 20, 'bold') ).place(relx=0.5, rely=0.005)###零

        if root.winfo_width() != ls.winfo()['w'] and 'C:' not in os.getcwd(): # True:一斉再計測。Simultaneous remeasurement
            wid(0, len(lst), 0,'再計測',root).post()
            ext.winfo(root.winfo_width())
        start = ls.start()
        # 進む
        wid.plus( start, root)
        try:
            # ファイルを開く
            if ls.setting()[ '音声' ] == '有':
                os.startfile( r'.\sund.py', operation= 'open')
                os.startfile( r'.\vox.py',  operation= 'open') # 相対パスで指定するとき、パス区切り文字に「/(スラッシュ)」を使用すると動作しません。
        except :
            pass
        #
        root.protocol#("WM_DELETE_WINDOW",lambda: print('hello'))
        score = time.time() - starting
        ( '{0}'.format(score) + '[sec]') 
        root.focus_set() 
        root.mainloop()     
        
if __name__ == '__main__': 
    main.post()