import tkinter as tk
import os.path
import time
import datetime
import ext
import ls
import sti
import cum
import data
import temp
import auxi
import prnt
import sync
import log
import mgmt

class wid(ls.sp): # window    
    def plus( start, root):
        try: # TclError回避
            lst = ls.customer()
            winfo = root.winfo_width() # 590 
            widz = [ d[ls.hb()] for d in lst] #
            
            if start < len(lst):
                tub = []
                
                for i, num in enumerate( widz[ start:]): 
                    tub.append(num)
                    
                    if winfo < sum(tub): 
                        end = start + i if i != 0 else (start + 1) # 後切り
                        break
                    end = start + len(tub) 

                    # 区分、区間、改ページで終点を判定
                    if end == len(lst) :
                        break
                    elif any(
                        lst[start].get(key) != lst[end].get(key) for key in ['区分', '区間']
                    ) or lst[ start + i]['改ページ'] == '有効':
                        break

                start, end  = auxi.adju.renw( start, end) # start, endの値、renewの値と比較、　必要なら変更、
                wid( start, end, 0, 0, root).post() 
                ext.save( ls.dl()[3], start)
                ext.save( ls.dl()[4], end) 
                ext.renew( start, False, os.path.basename(__file__))
        except Exception as e:
            pass
            
    def minus( root):   
        lst = ls.customer()
        widz = [ d[ls.hb()] for d in lst] # width
        
        if ls.start() > 0 :
            end = ls.start() 
            edge = [i for i in range(end)][-1] # 配列の末尾   
            winfo = root.winfo_width()
            tub = []
            for i, num in enumerate( widz[:end][::-1] ):
                tub.append(num)
                try:
                    if any([
                        winfo < sum(tub),
                        lst[edge]['区分'] != lst[end - len(tub)]['区分'],
                        lst[edge]['区間'] != lst[end - len(tub)]['区間'],
                        ls.pg()[1] == lst[end - len(tub)][ls.pg()[0]] and len(tub) > 1
                    ]):
                        start = end - i
                        break
                    else:
                        start = end - len(tub)
                        start = start if start != end else start - 1

                except Exception as e:
                    pass
            
            wid(start, end, 0, 0, root).post() 
            ext.save(ls.dl()[3], start )
            ext.save(ls.dl()[4], end   )      
                 
    def forget(root):
        children = root.winfo_children() 
        for child in children:
            child.destroy() 


    def post(self):        
        # 変数初期化
        root, lst = self.e, ls.customer()
        font, fon_ = ('TkDefaultFont', ls.ft()[0]), ('TkDefaultFont', ls.ft()[1])
        now = datetime.datetime.now()
        today, day_of_week = now.strftime('%Y-%m-%d'), ['月', '火', '水', '木', '金', '土', '日'][now.weekday()]
        issue, disp, src = sti.L.S(ls.week(), sti.sti.ph(), day_of_week), ls.setting()['表示'], sync.dr.src()
        
        # rootの設定
        wid.forget(root)
        root.title(f"{lst[self.a].get(ls.kb())}    {self.b}/{len(lst)}")
        root.update_idletasks()
        src = sync.dr.src() # src・sysフォルダ配下であればTrueを返す

        # メインループ
        for i in range(self.a, self.b) if type(self.c) is int else range(self.a, self.b)[::-1]:
            dic = lst[i]
            frame, frame0, frame2, frame3, lblframe, frame4, frame5, frame9, south = auxi.wid.frames(root, self.c, dic)
            
            wid.side(self, frame0, lblframe, frame5, day_of_week, today, font, dic)
            wid.middle(self, frame2, frame3, frame9, i, disp, issue, lst , font, dic)
            wid.center(self, lblframe, frame5, font, dic)

            # 呼出し      
            auxi.button( **{'master':frame4, 'text': i, 'font':('TkDefaultFont', 7), 'fg':ext.divi_clr(lst, dic[ ls.kb()]), 'bg':ext.divi_clr( lst, dic[ ls.kb()]), 'side':'top', 'fill':tk.BOTH })
                    
            # 部数の表示、区分、最初
            if  self.a == i : 
                data.cfg.txx(south, self.a, i, lst)
                
            # 幅:
            root.update_idletasks()
            if src == False and dic[ls.hb()] != frame.winfo_width(): # '幅'の保存値と現在値が異なるか、
                 ext.long( i, frame.winfo_width()) # '幅'を保存。
            # 一斉再計測、root.winfo_width()が変更された場合に、            
            auxi.wid.reme(self.d,root)
            
        wid.gdgt( root, fon_, self.a, self.b, i, lst)
        # 
    def side(self, frame0, lblframe, frame5, day_of_week, today, font, dic):
        for frame, keys in zip([frame0, frame5], [ls.mm()[1:3], ls.mm()[3:5]]):
            for key in keys:
                lis = ext.lmen(dic.get(key), 11, '')
                for txt in lis:
                    tk.Label(
                        frame,
                        text=ext.tategaki(txt),
                        bg=sti.S.M_S(day_of_week, txt),
                        relief=sti.T.M_S(today, txt)[0],
                        bd=sti.T.M_S(today, txt)[1],
                        font=font
                    ).pack(side='right')
        
    def middle(self, frame2, frame3, frame9, i, disp, issue, lst, font, dic):
            for s in dic.keys():
                if s not in ls.kl() + ls.tm():
                    # 新聞名
                    auxi.label( **{ 'master':frame2, 'text': s , 'font':font, 'fg':ext.font_clr(dic, s ), 'bg':ext.clr( s ), 'width':2, 'side':'right' }).brand()
                    # 部数
                    auxi.label( **{ 'master':frame3, 'text':dic[ s ], 'font':font, 'relief':sti.S.S_S_L( s , disp, issue), 'fg':ls.cl()[0], 'bg':ls.cl()[1], 'width':2, 'side':'right' }).quantity()
                    # frame9, 残りの部数, 区分・区間          
                    auxi.nine.wdgt(frame9, i, s, disp, issue, font, lst)    

    def center(self, lblframe, frame5, font, dic):
        tk.Label(lblframe, text= dic.get('号数'), font = font, bg=ls.cl()[1],fg=ls.cl()[3] if dic.get( ls.ak()) ==ls.ak() else ls.cl()[0]).pack(side='top') 
        # 一時止
        tk.Label(lblframe, text= temp.cnfg.tx(dic), font = ('TkDefaultFont', ls.ft()[1]), fg = temp.cnfg.fg(dic), bg = temp.cnfg.bg(dic) ).pack(side='top') 
        # 名称1                        
        for txt in ext.lmen(dic.get(ls.mi()), 5, ''):
            tk.Label(lblframe, text= ext.tategaki(txt), relief ='flat', bg=ls.cl()[1], font=('TkDefaultFont',ls.ft()[1]), height=5).pack(side='right')  
        tk.Label(frame5, text='',bd=3).pack(side='right')

    def gdgt( root, fon_, aa_, bb_, i, lst ):
        root.focus_set() 
        dct = lst[aa_]

        buttons_info = [
            ('＜',   lambda:wid.plus(ls.end(), root),                                   0.01),
            ('<<',   lambda:wid.plus(auxi.jump(root).front(), root),                    0.07),
            ('設定', lambda:sti.sti.post(tk.Toplevel()),                                0.11),
            ('一覧', lambda:cum.gdgt.table(ls.start(), ls.customer(), tk.Toplevel()),   0.15),
            ('印刷', lambda:prnt.gdgt.post(tk.Toplevel()),                              0.19),
            ('■',    lambda:wid.plus(0, root),                                          0.23),
            ('§',    lambda:wid.rem(root),                                              0.65),
            ('部数', lambda:data.anlys.wdgt(ls.start(), lst, tk.Toplevel()),            0.69),
            ('累計', lambda:mgmt.cum.post(tk.Toplevel()),                               0.74),
            ('総計', lambda:data.anlys.table(lst, ls.nw()[0], tk.Toplevel()),           0.79),
            ('履歴', lambda:log.wdgt.actv(tk.Tk()),                                     0.84),
            ('>>',   lambda:wid.plus(auxi.jump(root).back(), root),                     0.88),
            ('＞',   lambda:wid.minus(root),                                            0.94)
        ]
        for text, command, relx in buttons_info:
            tk.Button(root, text=text, command=command, font=fon_).place(relx=relx, rely=0.005)

        status= tk.Label(root)
        status.place(relx=0.29, rely=0.005) 
        root.bind('<Return>', lambda event:wid.go(root, status)) # plus | ダブルクリック禁止
        root.bind('<Return>', lambda event:auxi.wid.SetCursorPos( root.winfo_width()//2, root.winfo_reqheight()//2),"+" ) # カーソル位置中央へ
        root.bind('<MouseWheel>', lambda event:None if event.delta > 0 else None ) #
        root.bind('<3>', lambda event:wid.minus(root) ) 
        root.bind('<FocusIn>', lambda event:wid.fOCUS(root, status))
        root.bind('<FocusOut>', lambda event:status.configure(text= ' ' + 'Focus Out' + ' ', bg= 'red' , fg= 'white') )
        
        labels_info= [
            {'text':data.cfg.kb(aa_, dct),          'font':('TkDefaultFont', ls.ft()[0], 'bold'),   'relx':0.39, 'rely':0.005},
            {'text':data.cfg.kk(aa_, dct),          'font':('TkDefaultFont', ls.ft()[0], 'bold'),   'fg': None if data.cfg.kk(aa_, dct) == '' else 'teal', 'bg': None if data.cfg.kk(aa_, dct) == '' else 'white', 'relx':0.62, 'rely':0.005},
            {'text':data.cfg.east( aa_, i, lst),    'font':('TkDefaultFont', ls.ft()[0]),           'relx':0.96, 'rely':0.09},
            {'text':data.cfg.west( bb_, i, lst),    'font':('TkDefaultFont', ls.ft()[0]),           'relx':0.00, 'rely':0.09}
        ]
        for d in labels_info:
            tk.Label(root, text=d.get('text'), font=d.get('font'), fg=d.get('fg'), bg=d.get('bg')).place(relx=d.get('relx'), rely=d.get('rely')) 
        
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
            
    def rem(root): # 部分的再計測,remeasurement:再計測
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