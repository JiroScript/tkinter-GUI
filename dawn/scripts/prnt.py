from PIL import Image, ImageDraw, ImageFont
import os
from collections import defaultdict
import tkinter as tk
import sys
from ast import literal_eval
import shutil
import os.path

import ls
import ext
import data
import panda
import sl
import xlsx
"""
A4
標準 125dpi（pixel） 
297×210(mm)
1462×1033px
"""

class gdgt(): # gadget
    def post( root):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.title("宛紙") 
        root.geometry( ls.ge(ww,wh) )
        root.iconphoto(False, tk.PhotoImage(file='キャプチャ.PNG'))
        root.option_add( '*font', 'TkDefaultFont' + ' ' + "11" ) # ls.ft()[2]
        frame = tk.Frame(root) #
        frame .pack(padx=10,pady=5)      
        fram_ = tk.Frame(frame) 
        fram_ .pack()   
        cvs = panda.table.scrollbar(fram_,ww, wh)
        fra__ = tk.Frame(cvs)  
        fra__ .pack()
        north = tk.Frame( fra__) 
        north .pack( padx= 10, pady= 5 )   
        center = tk.Frame(fra__) 
        center.pack( padx= 10, pady= 5 )   
        tk.Button( north , text= "印刷", command = lambda:xlsx.file.active() ,width = 9, borderwidth=3 ,font=("TkDefaultFont",11,'bold'),).pack( side="left", padx= 6)
        gdgt.cancel( north, root)
        gdgt.sngl( fra__, center, root)
        root.mainloop()
        
    #
    def sngl( frame,  center, root):
        ll = sl.LL.LD_L( ls.customer(), [ ls.kb(), ls.kk() ]) # [['人事院', ''], ['人事院', ''], ]
        ll = sl.LL.LL( ll, []) # 統合。# [['人事院', ''], ]
        itr = sl.LD.LL( ll, [ ls.kb(), ls.kk() ], {}, []) # 配列内配列を配列内辞書に変換 
        two = dr.dsti()
        if type( sl.LD.LD_LD_L( itr, two, [ls.kb(), ls.kk()],[]) ) == list : 
            ext.store( "dsti.txt", sl.LD.LD_LD_L( itr, two, [ls.kb(), ls.kk()],[])) 
        lis = sl.D.LD_L( ls.customer(), [ ls.kb()]).keys() # dict_keys(['人事院', '弁護士会館', '富国生命', 'プレスセンター', '厚生労働省', '日比谷国際ビル', 'パークフロント'])

        for i, dic in enumerate( itr): #
            inx, bl = gdgt.coll(dic,two, [ls.kb(), ls.kk()])
            if bl :
                dic = two[inx]
            elif bl == False :
                dic = { **dic, **{ ix.wr() : '印刷しない' }}
                
            fram_ = tk.LabelFrame( frame)
            fram_.pack()
            gdgt.wdgt( fram_, center, i, dic, itr, two, lis, root )
    #
    def wdgt( frame, center, i, dic, itr, two, lis, root ):
        if i ==0:
            gdgt.row( center, itr)
        for k,v in dic.items():
            tk.Label( frame, text = v, width= mx.LD_S( itr, ls.kb()) +5, bg='gainsboro' if v in ls.alphabet() else 'whitesmoke', font=( 'TkDefaultFont',11) , anchor= "w" if v in lis else None,).pack( side="left")
        btn = tk.Button( frame, text = i, bd=4, fg="SystemButtonFace",)
        btn.pack( side="left", padx=2)
        btn.bind( "<1>", lambda event:gdgt.call( event, dic, itr, two, root))
                
    def row( center, itr:list): # '見出し'
        for v in [ ls.kb(), ls.kk(), ix.wr() ]:
            tk.Label( center, text = v ,width= mx.LD_S( itr, ls.kb()) +5, bg="gainsboro" if v == ls.kk() else "whitesmoke", anchor= "w" if v in sl.D.LD_L( ls.customer(), [ls.kb()]).keys() else None,).pack( side="left")
        tk.Button( center, text = 0, relief="flat", fg="SystemButtonFace").pack(side="left",padx=2)

    def extr( two:iter)-> list: # extract:抽出
        return set([ v for I in range(len(two)) for k,v in two[I].items() if k == ls.kb()])
    # ダイアログを呼び出す。
    def call( event, dic, itr, two, sub):
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        top = tk.Toplevel()
        top .option_add( '*font', "TkDefaultFont" +' '+ ls.ft()[1])
        val = tk.IntVar( top)
        i = int( event.widget["text"] )
        
        (sl.L.LD_S_D( itr, 'in', { ls.kb():dic.get(ls.kb())} )) # [2, 3]
        
        lf = tk.LabelFrame(top,text='「 '+ itr[i].get(ls.kb()) + " " +itr[i].get(ls.kk())+' 」'+"の"+ ix.wr() +"を設定する")
        lf .pack(side="left", padx= 2 ,pady= 2)
        value =[dic.get('割当')] + L.I_D_L(i, dic, two)
        spn = tk.Spinbox( lf , values= value, textvariable= val, width = 10, state = 'readonly', font=("TkDefaultFont",ls.ft()[0]) )# len([0][:1])
        spn .pack( side="left", padx= 4, pady= 2)
        tk.Button( lf , text="保存", command = lambda:gdgt.hub( i, itr, two, spn.get(), top, sub),).pack(side="left", padx=2 ,pady=2)#side="left"
                    
    def hub( i:int, itr:iter, two, txt:int, top, sub):
        dr.writ( i, itr, two, txt) # ファイル書き込み
        gdgt.dele( top, sub ) # 削除   
        gdgt.post( sub) # 表示
                
    def dele( top, sub): # delete
        top.destroy()
        children = sub.winfo_children() 
        for child in children:
            child.destroy()   
            
    def cancel( frame, sub):
        cancel = tk.Button( frame, text= "閉じる", command= sub.destroy, width=5)
        cancel.bind('<FocusOut>', lambda event: sub.destroy())
        cancel.pack( padx=4 ,pady=2)
        
    def coll( dic:dict, two:iter, arg:list): # collation:照合
        (dic) # {'区分': '人事院', '区間': ''}
        (two) # [{'区分': '人事院', '区間': '', '割当': '1'}, ]
        arr = []
        for i, hss in enumerate(two):     
            bl = [ dic.get(x) == hss.get(x)  for x in arg ]
            ( i, dic, hss, sum(bl), len(bl), bl)
            arr.append(sum(bl) == len(bl))
            #
            if sum(bl) == len(bl): 
                return i, True 
            elif len(arr) == len(two) and not any(arr) : # すべての要素がFalseか判定:not any()
                return i, False
        (arr, len(arr), not any(arr))
        
class L:
    def I_D_L( i:int, dic:dict, two:list)-> list: # Disposal:取捨
        (dic.get(ls.kb())) # 富国生命  [2, 3]
        # 配列は英語でsequence(順序) とも呼ばれる。
        # pythonにもarrayがあるが異なる型が混在できない
        sequ = sl.L.LD_S_D( two, 'not in', { ls.kb():dic.get(ls.kb())}) # [0, 1, 4, 5, 6, 7, 8]
        (sequ,)
        
        sequ.insert( len(sequ), i) # {'は', 'い', 'へ', 'り', 'ほ', 'ち', 'ろ', 'と'}
        # Curly braces:波括弧
        crly = set([ two[i].get('割当') for i in sequ if two[i].get('割当') != '印刷しない']) # {'は', 'い', 'へ', 'り', 'ほ', 'ち', 'ろ', 'と'}
        arr = ['い','ろ','は','に','ほ','へ','と','ち','り','ぬ','る','を','わ','か','よ','た','れ','そ','つ','ね','な','ら','む']
        try:
            for i in crly :
                arr.remove(i)
        except :
            pass
        
        if dic.get('割当') != '印刷しない' : arr = ['印刷しない'] + arr 
        return arr # ['印刷しない', 'に', 'ぬ', 'る', 'を', 'わ', 'か', 'よ', 'た', 'れ', 'そ', 'つ', 'ね', 'な', 'ら', 'む']
    # 1~10のリストを取得。
    def I(num): # 10
        [ i for i in range( 1, num + 1 )] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return  [ i for i, dic in enumerate( range(num), start=1)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
class mx(): # 最大
    # 配列内辞書の、値の文字列、最大値を返す
    def LD_S( itr:list, ky:str)->int: 
        itr # [{'区分': '人事院', '区間': ''}, {'区分': '弁護士会館', '区間': ''}, 
        arr = [ len(dic.get(ky)) for dic in itr ] # [3, 5, 4, 4, 7, 7, 5, 7, 7] 
        return max(arr) # 7
        
class dr(): # direc
    # dsti.txtの読み込み
    def dsti(): # destination: 宛先
        fnc = sys._getframe().f_code.co_name
        file_ = "../setting/" + fnc + ".txt"
        with open(file_, "r", encoding='utf-8') as f:
            data_list = f.read()        
        text = data_list.replace(" ","")
        lst = literal_eval(str(text))#文字列をリストや辞書に変換
        return lst  
    # ファイルに書き込み
    def writ(i,itr, two, txt):
        (i, itr, txt)
        dct = itr[i]
        dct[ix.wr()] = txt
        (itr[i])
        inx, bl = gdgt.coll(dct,two, [ls.kb(), ls.kk()])
        (bl)
        if bl :
            two[inx][ix.wr()] = txt
        elif bl == False :
            two.insert(-1, dct)
        ext.store( "dsti.txt" ,two)

    def rm( ph): # フォルダごと削除する、フォルダを生成する。
        l = os.listdir( path = ph )
        [ os.remove( ph + '/' + i ) for i in l ] # ファイル削除
        
# ファイルを生成        
class form(): # form:生成, 形成する
    def post():        
        path = '../paper' # ディレクトリパス
        digit = 2       # 数字部分の桁数
        count = 1       # 作る個数
        # 存在チェック
        if os.path.isdir(path) == False:
            os.mkdir(path)
        lst = ls.customer() 
        two = dr.dsti()
        two = [ i for i in two if i.get(ix.wr()) != ix.ng() ] # 割当：'印刷しない'の辞書を除外した配列内辞書を返す。
        kkw = sl.LL.LD_L( two, [ls.kb(),ls.kk(),ix.wr()]) # [['人事院', '', '1'],['人事院', '', '1'],]
        kkw = sl.LL.LL( kkw, []) # 統合。[['人事院', '', '1']]
        kk  = sl.LL.LD_L( lst, [ls.kb(),ls.kk()])# [['人事院', '']]
        # iterable:反復可
        itr = form.coll( kkw, kk, [], {}) # {'1': [0, 1, 2, 3]}
        form.sngl( path, digit, lst, itr,)
        
    def coll( two:iter, itr:iter, duo = [], dic= {})->dict: # Collation:照合
        for li in two:   # ['人事院', '', '1']
            l = li[:2]   # ['人事院', '']
            s = li[2]    # '1'
            arr = []
            for i, u in enumerate(itr):
                if l == u : # ['人事院', ''] == ['人事院', '']
                    arr.append(i) # [0]
            duo.append(arr)
            dic.setdefault( s, [])
            dic[s] += arr
        return dic # {'1': [0, 1] }
    
    def add(lst, arg, hss): # {'人事院': {'ア': [3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2], 'マ': [3, 1, 1, 1, 1, 1, 1, 1, 2, 1], 
        for dic in lst:
            for k,v in dic.items():
                if k in ls.kb():
                    hss.setdefault(v,{})
                    x = dic.get(ls.kb())
                    
                elif k not in ls.kl() : # and k in ls.nw()[0]
                    hss[x].setdefault(k,[])
                    hss[x][k].append( int(v))
        return hss
    
    def sngl( path:str, digit:int, lst:list, itr:iter): #
        (itr)
        width =  1462   # pixel：画像の幅、「プロパティ」で参照可能
        height = 1033   # pixel：画像の高さ、「プロパティ」で参照可能
        size = 16  # フォントサイズ
        spce = size #Line spacing:行間
        ddl = DDL.LD_L( lst, [ ls.kb(), ls.kl()], {}) # {'人事院': {'ア': [3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2], 'マ': [3, 1, 1, 1, 1, 1, 1, 1, 2, 1], 
        dr.rm(path) # フォルダごと削除する、フォルダを生成する。
        # ファイル生成
        for i, ky in enumerate( itr): # {'1': [0, 1, 2, 3]}
            arr = itr[ ky ] # [0, 1, 2, 3, 4, 5]
            ld = sl.LD.LD_L_L( lst, arr, ls.kl()) # [{'ア': '3'}, {'マ': '3'},]
            dct =  sl.D.LD( ld , {} ) # {'ア': 13, 'マ': 12, 'ヨ': 12,}
            #  file_base_name='test_'、digit=3のときは 'test_{:03d}.png' => test_000.png
            fmt = "p_" + '{:0' + str(digit) + 'd}' + '.png'
            file_name = fmt.format( i + 1 )
            im = Image.new( 'RGBA', ( width, height))
            draw = ImageDraw.Draw(im)
            fnt = ImageFont.truetype('meiryo.ttc', size) # meiryo.ttc, yumin.ttf
            
            # テキストのサイズを取得し、中心に文字表示
            text_width, text_height = draw.textsize(file_name, fnt)
            lis = [ lst[ i ] for i in arr ] # [{'区分': '人事院', '区間': '', '名称1': '秘書室①'}]
            (lis)
            inx = itr[ky][0] # "1"
            kb = lst[inx].get(ls.kb()) # '人事院'
            
            form.title(draw, kb, file_name, spce ) # タイトル書き込み
            form.culc(draw, dct, spce, fnt ) # 【総計】
            form.dubl(draw, lis, spce, width, fnt) # 新聞名、部数など文字列を書き込み
            # ファイル生成
            im.save(path + '\\' + file_name) 
            
    def culc( draw:object, dic:iter, spce:int, fnt:object): # 【総計】
        (dic)
        txt = form.string( dic )
        l =[]
        for u,d in dic.items():
            t = str(d) + '：' + u + ' '
            l.append(t)
        arr = [ str(dic[k]) + ' : ' + k for k in dic.keys() if k in ls.nw()[0]][::-1]
        print(l)
        txt = '  '.join(arr) 
        tx_ = '  '.join([ str(dic[k]) + ' : ' + k for k in dic.keys() if k not in ls.nw()[0]][::-1]) 
        draw.text(
            ( spce*2, spce * 6 ), # 座標
            txt + ' ■', # 実際に表示される文字列
            fill = 'black', 
            font = fnt)
        draw.text(
            ( spce*2, spce * 7.5  ), # 座標
            tx_ + ' ■', # 実際に表示される文字列
            fill = 'black', 
            font = fnt)
        
    def dubl( draw:object, lis:iter, spce:int, width:int, fnt:object): # double:二重
        for i, dic in enumerate( lis ):
            textWidth, textHeight = draw.textsize( form.string( dic) ,font=fnt)
            ( form.string( dic), textWidth, textHeight)
            
            draw.text(
                ( width -50 - spce - textWidth, ( spce * 10 ) + (spce * i)), # 座標
                form.string( dic), # 実際に表示される文字列
                fill = 'black', 
                anchor = 'rm', spacing=120, align ="right",
                font = fnt)
            
    def title(draw:object, txt:str, file_name:str, spce:int):
        draw.text(
            ( spce*2, spce*2 ), # 座標 「01」
            "{}".format(file_name[2:4]), # 実際に表示される文字列
            fill = 'black', 
            font = ImageFont.truetype('meiryo.ttc', spce*3))
        
        draw.text(
            ( spce * 6, spce ), # 座標
            txt , # 実際に表示される文字列 「人事院」
            fill = 'black', 
            font = ImageFont.truetype('meiryo.ttc', spce*4))
        
    
    # 印字する文字列  
    def T( u, d):
        (u,d)
        if len(str(d)) > 1 and u in ls.nw()[0]:
            ( u,d, len(str(d)))
            x = " " * (3 - len(str(d)))
        else:
            x = "   "
        if str(d) =='0':
            u = "　" # 全角スペース
            d = "  "
        return u, d, x
    
    def string( dic:dict)->str:  # 文字列
        dic = D.D( dic, {})
        itr = [ kv for kv in dic.items()] 
        arr, ar0, ar1, ar2, ar3, ar4, ar5  = [], [], [], [], [], [], []
        for u, d in itr:  
            if u == ls.mi(): # 名称1
                txt = str(d)  
                txt = form.trim(txt,5)
                ar0.append( txt)
            elif u == ls.gs() : # 号数
                txt = str(d)  
                txt = form.trim(txt,4)
                ar1.append( txt)
            elif u == ls.tr() : # 取扱
                txt = str(d)
                txt = form.trim(txt,2)
                ar2.append( txt)
            elif u not in ls.kl() :
                if u in ls.nw()[0]: # 部数：新聞名 ddl[ dic[ls.kb()]][u] 
                    u, d, x = form.T( u , d )
                    txt = x + str(d) + '：' + u 
                    ar3.append(txt)
                elif u not in ls.nw()[0]:
                    txt = str(d) + '：' + u + ' '
                    ar5.append(txt)
            elif u == ls.mm()[1] : #メモ1
                txt = str(d)
                txt = form.trim(txt,5)
                ar4.append( txt)
                
        [ i.replace("\u3000"," ") for i in arr ] # \u3000:全角スペース
        s = S.L( [ ar0, ar1, ar2, ar3, ar4 , ar5])
        return s # 秘書室①   「1」  税のしるべ:1  ト:3  産:3  サ:3  ヨ:3  マ:3  ア:3
    
    
    # 文字数制限
    def trim( txt:str, num:int)->str:  
        blank  = ( num - len(txt)) * '　' #全角スペース
        txt = txt + blank
        txt = txt[ :num] # 文字数制限
        txt = form.jis(txt) # 全角文字に変換
        ( txt, len(txt))
        return txt 
    
    # 全角文字に変換,JIS関数
    def jis(string): 
        return string.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
    
class D():
    def D( dic, hss): # interrupt:割り込み
        for i in ls.nw()[0]:
            if i in dic.keys():
                hss  = {**hss, **{i:dic[i]}}
            elif i not in dic.keys():
                hss  = {**hss, **{ i: 0}}
        (hss)  
        frnt = { k:y for k,y in dic.items() if k in ls.kl()}
        midd = hss
        back = { k:y for k,y in dic.items() if k not in ls.kl() + ls.nw()[0]}
        return {**frnt, **midd, **back}
    
class DDL():
    def LD_L(lst, arg, hss): # {'人事院': {'ア': [3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2], 'マ': [3, 1, 1, 1, 1, 1, 1, 1, 2, 1], 
        for dic in lst:
            for k,v in dic.items():
                if k in ls.kb():
                    hss.setdefault(v,{})
                    x = dic.get(ls.kb())
                    
                elif k not in ls.kl() : # and k in ls.nw()[0]
                    hss[x].setdefault(k,[])
                    hss[x][k].append( int(v))
        return hss
    
class S():    
    def L( arg:list)->list: 
        ar0, ar1, ar2, ar3, ar4, ar5 = arg
        
        ar_ = ['          '] if ''.join(ar4).count('\u3000') == 5 else ['※' + '          ']
        arr = ar4 + ar_ + ar5[::-1] + ar3[::-1] + ['|'] + ar2 + ['|'] + ar1 + ['|'] + ar0 + ['□'] # rra[::-1]
        return ' '.join(arr) # 秘書室①   「1」  税のしるべ:1  ト:3  産:3  サ:3  ヨ:3  マ:3  ア:3
     
class ix():  # index 
    def wr()-> str:
        return '割当'
    def ng()-> str: # Negative:否定、
        return '印刷しない'
    import sys

if sys.platform == 'win32':
    import win32api
    import win32print

class Printer:
    
    @staticmethod
    def print_default():
        if sys.platform != 'win32':
            print("This function can only be executed on Windows.")
            return
        
        path = "キャプチャ.png"
        printer_name = f'"{win32print.GetDefaultPrinter()}"'
        win32api.ShellExecute(0, 'print', path, printer_name, '.', 0)
        
    @staticmethod
    def generate_image():
        import PIL.Image
        import PIL.ImageDraw
        import PIL.ImageFont
        
        # 使うフォント，サイズ，描くテキストの設定
        ttfontname = "C:\\Windows\\Fonts\\meiryob.ttc"
        fontsize = 36
        text = "暗黙の型\n宣言"
        
        # 画像サイズ，背景色，フォントの色を設定
        canvasSize    = (300, 150)
        backgroundRGB = (255, 255, 255)
        textRGB       = (0, 0, 0)
        
        # 文字を描く画像の作成
        img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
        draw = PIL.ImageDraw.Draw(img)
        
        # 用意した画像に文字列を描く
        font = PIL.ImageFont.truetype(ttfontname, fontsize)
        textWidth, textHeight = draw.textsize(text, font=font)
        textTopLeft = (canvasSize[0]//6, canvasSize[1]//2 - textHeight//2) # 前から1/6，上下中央に配置
        draw.text(textTopLeft, text, fill=textRGB, font=font)
        
        img.save("image.png")

            
class LD_DL_LD(): # 
    def get():        
        path = '../paper' # ディレクトリパス
        # 存在チェック
        if os.path.isdir(path) == False:
            os.mkdir(path)
        lst = ls.customer() 
        two = dr.dsti() # [{'区分': '人事院', '区間': '', '割当': 'い'}, {'区分': '弁護士会館', '区間': '', '割当': 'ろ'}, {'区分': '富国生命', '区間': 'A', '割当': 'は'}, {'区分': '富国生命', '区間': '', '割当': '印刷しない'}, 
        # 割当：'印刷しない'の辞書を除外。 
        ld = [ i for i in two if i.get('割当') != '印刷しない' ] # [{'区分': '人事院', '区間': '', '割当': 'い'}, {'区分': '弁護士会館', '区間': '', '割当': 'ろ'}, {'区分': '富国生命', '区間': 'A', '割当': 'は'}]
        lt = T.LD_L( ld, [ '区分', '区間'] ) #  # [('人事院', ''), ('弁護士会館', ''), ('富国生命', 'A')]
        dl = DL.LD_LT_LD( ld, lt, lst, {}) # # {'い': [0, 1, 2, 3], 'ろ': [23, 24, 25,       
        return ld, dl, lst

class DL():  
    def LD_LT_LD( ld:list, lt:list, lst:list, dct:dict)-> dict:
        for i, d in enumerate(lst):
            tpl = ( d.get('区分'), d.get('区間'))
            ( i, tpl, tpl in lt, )
            if tpl in lt : # ('人事院', '') in [('人事院', ''), ('弁護士会館', ''), ('富国生命', 'A')]
                z = lt.index(tpl) # 0
                txt = ld[z].get('割当') # い
                dct.setdefault( txt, [])
                dct[txt].append(i)
        return dct # {'い': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 'ろ': [23, 24, 25, 26, 27, 28, 29, 30, 31, 32], 'は': [33]}

class T():
    def LD_L( ld :iter, arg :list)-> list: 
        return  [ tuple( dic.get(i) for i in arg ) for dic in ld ] # [('人事院', ''), ('弁護士会館', ''), ('富国生命', 'A')]
    
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。  
    root = tk.Tk()
    gdgt.post( root)
    dr.writ#(1,2)
    L.I(10) # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']