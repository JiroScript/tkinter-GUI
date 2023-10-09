import tkinter
import tkinter as tk
from tkinter import ttk
import ls
import os.path
import os
import sys

class tree(ls.sp):    
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #  
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        global select_item 
        root = ee_
        root.title("")#window
        style = ttk.Style()
        style.configure('.', font = ('', 14))
        
        # グローバル変数
        buff1 = tk.StringVar()
        buff1.set('')
        buff2 = tk.StringVar()
        buff2.set('')
        select_item = None
        
        fr = ttk.Frame(root)
        f_ = ttk.Frame(fr)
        ttk.Label(f_, textvariable = buff1 ).pack( padx= 0,pady= 1)
        e = ttk.Label(f_, width = 8, font = ('', 9), textvariable = buff2)
        e.pack()
        f_.pack(side = tk.LEFT)
        button = tk.Button(fr,text="選択",command=lambda:print(buff1.get()))
        button.pack(side = tk.LEFT,padx=2)
        fr.pack(padx=6,pady=6)
        
        tview = ttk.Treeview(root, columns = ('notation','name' ))#Notation：表記
        tview.column('#0', width = 60)
        tview.column('notation', anchor = 'e', width = 100)
        tview.column('name', anchor = 'e', width = 100)
        tview.heading('#0', text = "")
        tview.heading('notation', text = "")
        tview.heading('name', text = "")
        id = tview.insert('', 'end', text = 'あ行')
        tview.insert(id, 'end', values = ('ア', '朝日新聞本紙'))
        print(list(tree.nw()[0][0].keys())[0])
        for i, item in enumerate( tree.nw()[0]):
            k = list(item.keys())[0]
            v = list(item.values())[0]
            tview.insert(id, 'end', values = ( k, v))
        
        id = tview.insert('', 'end', text = 'か行')
        for i, item in enumerate( tree.nw()[1]):
            k = list(item.keys())[0]
            v = list(item.values())[0]
            tview.insert(id, 'end', values = ( k, v))
        
        id = tview.insert('', 'end', text = 'さ行')
        for i, item in enumerate( tree.nw()[2]):
            k = list(item.keys())[0]
            v = list(item.values())[0]
            tview.insert(id, 'end', values = ( k, v))
        
        id = tview.insert('', 'end', text = 'た行')
        for i, item in enumerate( tree.nw()[3]):
            k = list(item.keys())[0]
            v = list(item.values())[0]
            tview.insert(id, 'end', values = ( k, v))
        
        sb = ttk.Scrollbar(root, orient = 'v', command = tview.yview)
        tview.configure(yscrollcommand = sb.set)
        
        tview.pack(side = tk.LEFT)
        sb.pack(side = tk.LEFT, fill = tk.Y)
        e.bind('<Return>', lambda event:tree.update_notation(event,tview,buff2))
        tview.bind('<<TreeviewSelect>>', lambda event:tree.select_(event,tview,buff1,buff2))
        
        cansell = tk.Button(fr, text= "戻る" ,command = root.destroy      )
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:root.destroy() )
        cansell.pack(side="left",padx=6)
        root.mainloop()
        
    def select_( event, tview, buff1, buff2):
        global select_item
        x = tview.selection()[0]
        d = tview.set(x)
        if d:
            buff1.set(d['notation'])
            buff2.set(d['name'])
            select_item = x
        else:
            buff1.set('')
            buff2.set('')
            select_item = None
            
    def update_notation( event, tview, buff2):
        if select_item:
            tview.set( select_item, 'notation', buff2.get())
        
    def nw():#news papar
        agy =[{'朝日小学生':''},{'朝日中高生':''},{'朝日・縮刷版':''},{'ヴェリタス':''}]
        kgy =[{'工':'日刊工業新聞'},{'金融':''},{'株式':''},{'海事':''},{'建通':''},{'建産':''},{'建設':''},{'ガイド':''},{'ＫＯＤＯＭＯ':''},{'高校生':''},{'碁':''},{'ゲンダイ':''}]
        sgy =[{'税のしるべ':''},{'自動車':''},{'ショッピング':''},{'埼玉建設':''},{'せんけん':''},{'ぜんせき':''},{'繊維ニュース':''},{'全国農業':''},{'スポニチ':''},{'サンスポ':''},{'デイリー':''},{'少年写真':''},{'将棋':''},{'日刊工業・縮刷版':''}]
        tgy =[{'ト':'東京新聞本紙'},{'鉄鋼':''},{'電波':''},{'でんき':''},{'東スポ':''},{'つりニュース':''},{'東スポ':''},{'電波・縮刷版':''}]
        ngy =[{'サ':'日本経済新聞本紙'},{'産':''},{'日産':''},{'日本証券':''},{'燃料油脂':''},{'農業':'日本農業新聞'},{'日刊スポ':''},{'日経・縮刷版':''},{'日経産業・縮刷版':''},{'日経流通・縮刷版':''}]
        hgy =[{'フジサンケイ・ビジネスアイ':''},{'報知':''},{'へらニュース':''},{'フジ':''}]
        mgy =[{'マ':'毎日新聞本紙'},{'木材':''},{'毎日小学生':''},{'毎日・縮刷版':''}]
        ygy =[{'ヨ':'読売新聞本紙'},{'読売中高生':''},{'読売・縮刷版':''}]
        rgy =[{'流通':''},{'流通・縮刷版':''}]
        wgy =[{'':''}]
        eig =[{'F・T':''},{'WALL・STREET・JOURNAL・ASIA':''},{'A':''},{'Y':''},{'JAPAN-NEWS':''},{'JAPAN-TIMES/NYT':''},{'US版':''},{'NYT':''},{'ニューヨーク・タイムズ・ウィークリー・レビュー':''},{'ジャパンタイムズ 縮刷版':''},{'Newseek・Japan':''},{'ニューヨーク・タイムズ':''},{'ウォールストリート・ジャーナル':''},{'ザ・タイムズ':''}]
        gig =[{'ル・モンド':''},{'F・アルゲマイネ':''}]
        sks =[{'AERA':''},{'文春':''},{'SPA!':''},{'週刊朝日':''},{'ダイアモンド':''},{'新潮':''},{'東洋経済':''}] 
        return agy,kgy,sgy,tgy,ngy,hgy,mgy,ygy,rgy,wgy,eig,gig,sks 

if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    tree(0,0,0,0,tk.Tk()).post()
    
