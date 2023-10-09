from ast import literal_eval
import sys

class sp():
    def __init__(self, a, b, c, d, e):
        self.a = a  
        self.b = b 
        self.c = c
        self.d = d
        self.e = e
        
    def pasS(self): 
        pass

class nm():
    def __init__(self, a,b,c):
        self.a = a  
        self.b = b 
        self.c = c    
    def class_def(self):#       
        file__ = self.a #
        class_ = self.b #   
        def___ = self.c #
        nm.smb(file__,class_,def___)
        (file__,class_,def___)
        
    def smb(file__,class_,def___):
        pass
    
def customer(): # 読み出し
    file = "../setting/customer.txt"
    with open(file, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    lst = literal_eval(str(text))#文字列をリストや辞書に変換
    return lst

def setting():
    file_ = "../setting/setting.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    return dct

def sort():
    file_ = "../setting/sort.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    return dct

def week():
    file_ = "../setting/week.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    lst = literal_eval(str(text))#文字列をリストや辞書に変換
    return lst

def date():
    file_ = "../setting/date.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    lst = literal_eval(str(text))#文字列をリストや辞書に変換
    return lst

def the_day_before():#休刊日前日
    file_ = "../setting/the_day_before.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    lst = literal_eval(str(text))#文字列をリストや辞書に変換
    return lst

def num():
    file_ = "num.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    return dct

def start():
    dct = num()
    lst = customer()    
    return dct["start"]

def end():
    dct = num()
    lst = customer()    
    if dct["end"] <= len(lst):
        return dct["end"]
    elif dct["end"] > len(lst):
        return len(lst)
def winfo():
    file_ = "winfo.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    return dct

def difference():
    file = "../setting/difference.txt"
    with open(file, "r", encoding='utf-8') as f:
        data = f.read()        
    text = data.replace(" ","")
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    return dct

def relord():
    file_ = "relord.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    lst = literal_eval(str(text))#文字列をリストや辞書に変換
    return lst[ dl()[5]]

def group():
    file_ = "../setting/group.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    d = literal_eval(str(text))#文字列をリストや辞書に変換
    return d

def sheet():
    file_ = "../setting/sheet.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    lst = literal_eval(str(text))#文字列をリストや辞書に変換
    return lst

def store( file_name ,lst ):
    lst = str(lst).replace(" ","")
    lst = lst.replace( "}," ,"},\n" )
    sys._getframe().f_code.co_name
    with open( '../setting/' + file_name, mode = 'w', encoding='utf-8') as f:
        f.write(lst)

def mn():#
    keylst = ['一般日刊紙','産業･金融・流通','株式・証券・税務','交通・運輸・鉄鋼','建設・住宅・電気','石油・繊維・農林','スポーツ紙','海外紙・国内英字紙','青少年向き・レジャー・趣味','一般夕刊紙','各種の縮刷版・その他']
    return keylst

def rw():#row
    keylst = ['あ行','か行','さ行','た行','な行','は行','ま行','や行','ら行','わ行','英字','外語','週刊誌']
    return keylst
def kt():# Category:独: Kategorie
    keylst = ['一般紙','産業紙','業界紙','金融紙','スポーツ紙','海外紙','国内英字紙','青少年向き','レジャー・趣味','一般夕刊紙','各種の縮刷版・その他','全て']
    return keylst

def nw():
    a = ['朝日','毎日','読売','日経','産経','東京'] 
    b = ['工','日産','流通','ヴェリタス','フジサンケイ・ビジネスアイ']
    c = ['金融','株式','日本証券','税のしるべ']
    d = ['自動車','海事','ショッピング']
    e = ['鉄鋼']    
    f = ['建通','建産','建設','埼玉建設']
    g = ['電波','でんき']    
    h = ['燃料油脂','ぜんせき']
    i = ['せんけん','繊維ニュース']
    j = ['農業','全国農業','木材','ガイド']    
    k = ['報知','日刊スポ','スポニチ','サンスポ','東スポ','デイリー']
    l = ['F・T','WALL STREET JOURNAL ASIA']
    m = ['A','Y','JAPAN-NEWS','JAPAN-TIMES/NYT','US版','NYT']
    n = ['朝日小学生','朝日中高生','毎日小学生','ＫＯＤＯＭＯ','読売中高生','高校生','少年写真','少年少女きぼう新聞'] 
    o = ['つりニュース','へらニュース','碁','将棋']
    p = ['ゲンダイ','フジ','東スポ','ニューヨーク・タイムズ・ウィークリー・レビュー']
    q = ['朝日・縮刷版','毎日・縮刷版','読売・縮刷版','日経・縮刷版','日経産業・縮刷版','日経流通・縮刷版','流通・縮刷版','日刊工業・縮刷版','ジャパンタイムズ・縮刷版','電波・縮刷版']
    r = ['ニューヨーク・タイムズ','ウォールストリート・ジャーナル','ザ・タイムズ','ル・モンド','F・アルゲマイネ','AERA','文春','SPA!','週刊朝日','Newseek Japan','ダイアモンド','新潮','東洋経済','公明','聖教','赤旗','大百蓮華','創価新報','公明グラフ','未来ジャーナル']
    
    return a, b, c, d, e, f, g, h, i, j, k, l, m, n , o, p ,q , r

def reverse():
    arr = list(nw())
    arr[0] = nw()[0][::-1]
    return arr 

def ge(ww,wh):###
    keylst=[]
    if zm() == True:
        keylst = str(int(ww))+"x"+str(int(wh))+"+"+str(0)+"+"+str(0)
    elif zm() == False:
        keylst = str(int(ww/2-50))+"x"+str(int(wh/2))+"+"+str(0)+"+"+str(0)
    return keylst

def zm(): #
    file_ = "../setting/setting.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    dct = literal_eval(str(text)) # 文字列をリストや辞書に変換
    keylst = bool( dct['最大化']) # 整数int:0はFalse,0でない数値はすべてTrue。
    return keylst

def ft(): # font
    'SystemButtonFace'
    'FixedSys'
    'TkDefaultFont'
    file_ = "../setting/setting.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    keylst = [dct['large'] ,dct['middle'] ,dct['small']]
    return keylst

def alphabet():
    return ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def cl(): #coler
    keylst = ['black','#FCFCF9','white','red','#eCeCeC']
    return keylst

def sc():#system color
    "SystemButtonFace"
    keylst=['black','green','yellow','blue','aqua','purple','orange','silver','maroon','lime','navy','olive','fuchsia',"white","darkcyan","teal"]
    return keylst

def wd():##callで表示するkey
    keylst = ['区分','区間','名称1','号数','一時止','メモ1','メモ2','メモ3','メモ4']##順不同可。ls.kl()[5]  ls.wd()[6]  ls.wd()[7] ls.wd()[8]
    keylst = [kb(),kk(),mi(),gs(),ic(),mm()[1],mm()[2],mm()[3],mm()[4]]
    return keylst

def tm():##除外するkey #temporary 一時的,
    keylst = ['始月','始日','始刊','終月','終日','終刊','取扱']#['一時止','始月','始日','始刊','終月','終日','終刊','取扱']
    return keylst

def tg(): #tag 
    keylst = ['赤字','黒字']
    return keylst
def kl():#keywordlist #除外するkey
    keylst = ['区分','区間','名称1','号数','赤字','一時止','始月','始日','始刊','終月','終日','終刊','取扱','改ページ','幅','メモ1','メモ2','メモ3','メモ4']##順不同不可。kl()[14] kl()[15] kl()[16] kl()[17]
    return keylst
def mm():#memo
    keylst = ['','メモ1','メモ2','メモ3','メモ4']
    return keylst

def kb():#kubun
    return '区分'
def mi():#meisho1
    return '名称1'
def kk():#kukan
    return '区間'
def gs():#gosuu
    return '号数'
def ic():#ichicji
    return '一時止'
def tr():#ichicji
    return '取扱'
def kp():#kaipage
    return '改ページ'
def hb():#haba
    return '幅'
def ak():#akaji
    return '赤字'

def js(): #
    return {'黒字':'黒字'}

def pa():#Place name
    l =['内幸町','永田町']
    l =['〇〇町','凸凹町']
    return l
def ea(): #eria
    l = ['人事院','弁護士会館','富国生命','プレスセンター','厚生労働省','日比谷国際ビル','パークフロント'],['国会議事堂','総理大臣官邸','国会図書館']
    l = ['一丁目','二丁目','三丁目','四丁目','五丁目','六丁目','七丁目'],['凹ヶ丘','△△原','〇×ニュータウン']
    return l

def sh():#shift:シフト
    keylst =['日時','区分','作業者']
    return keylst
def rw():#row:行
    keylst =['さ行','その他']
    return keylst
def hu(): #human
    sa  = ['鈴木','須田','島村']
    etc = ['揖斐','萩田']
    return sa,etc

def dp(): #day of the week and public holiday and newspaper holiday
    keylst =['月','火','水','木','金','土','日','祝','㊡']
    return keylst

def dl(): #day of the week and public holiday
    keylst =['表示','全表示','曜日・祝日別','start','end','relord','barrier','group']
    return keylst
def cm(): #Cumulative:累計 
    keylst =['設定','全表示','グループ別','グループ設定']
    return keylst
def pg(): #改ページ
    keylst =['改ページ','有効','無効']
    return keylst
def dd(): #dusk：夕暮れ、dawn：夜明け
    return {'dusk':'dusk','dawn':'dawn'}
