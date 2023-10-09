from ast import literal_eval
import sys

class sp():
    def __init__(self, a,b,c,d,e):
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
        print(file__,class_,def___)
def Read(file_):
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    return dct
def Write(file_ ,dct ):
    dct = str(dct).replace(" ","")
    dct = dct.replace( "}," ,"},\n" )
    sys._getframe().f_code.co_name
    with open( file_, mode = 'w', encoding='utf-8') as f:
        f.write(dct)
def customer_prot():
    key = list( dusk_dawn().keys())[0]
    val = dusk_dawn()[ key]
    file_ = "../setting/" + val + ".txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    lst = literal_eval(str(text))#文字列をリストや辞書に変換
    return lst
def customer():
    file_ = "../setting/customer.txt"
    with open(file_, "r", encoding='utf-8') as f:
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
def start________________():
    file_ = "setting.txt"
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
    dic = literal_eval(str(text))#文字列をリストや辞書に変換
    return dic

def sheet():
    file_ = "../setting/sheet.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    lst = literal_eval(str(text))#文字列をリストや辞書に変換
    return lst

def store(file_name ,lst ):
    lst = str(lst).replace(" ","")
    lst = lst.replace( "}," ,"},\n" )
    sys._getframe().f_code.co_name
    with open( '../setting/' + file_name, mode = 'w', encoding='utf-8') as f:
        f.write(lst)

def mn():#
    keylst = ["一般日刊紙","産業･金融・流通","株式・証券・税務","交通・運輸・鉄鋼","建設・住宅・電気","石油・繊維・農林","スポーツ紙","海外紙・国内英字紙","青少年向き・レジャー・趣味","一般夕刊紙","各種の縮刷版・その他"]
    return keylst
def rw():#row
    keylst = ['あ行','か行','さ行','た行','な行','は行','ま行','や行','ら行','わ行','英字','外語','週刊誌']
    return keylst


def nw():
    general = ["ア","マ","ヨ","サ","産","ト"] 
    industr = ["工","日産","流通","ヴェリタス","フジサンケイ・ビジネスアイ"]
    Finance = ["金融","株式","日本証券","税のしるべ"]
    traffic = ["自動車","海事","ショッピング"]
    steel__ = ["鉄鋼"]    
    constru = ["建通","建産","建設","埼玉建設"]
    electri = ["電波","でんき"]    
    fuel___ = ["燃料油脂","ぜんせき"]
    fiber__ = ["せんけん","繊維ニュース"]
    Agricul = ["農業","全国農業","木材","ガイド"]    
    sport__ = ["報知","日刊スポ","スポニチ","サンスポ","東スポ","デイリー"]
    oversea = ["F・T","WALL STREET JOURNAL ASIA"]
    english = ["A","Y","JAPAN-NEWS","JAPAN-TIMES/NYT","US版","NYT"]
    youth__ = ["朝日小学生","朝日中高生","毎日小学生","ＫＯＤＯＭＯ","読売中高生","高校生","少年写真","碁"] 
    hobby__ = ["つりニュース","へらニュース","碁","将棋"]
    evening = ["ゲンダイ","フジ","東スポ","ニューヨーク・タイムズ・ウィークリー・レビュー"]
    small__ = ["朝日・縮刷版","毎日・縮刷版","読売・縮刷版","日経・縮刷版","日経産業・縮刷版","日経流通・縮刷版","流通・縮刷版","日刊工業・縮刷版","ジャパンタイムズ・縮刷版","電波・縮刷版"]
    etc____ = ["ニューヨーク・タイムズ","ウォールストリート・ジャーナル","ザ・タイムズ","ル・モンド","F・アルゲマイネ","AERA","文春","SPA!","週刊朝日","Newseek Japan","ダイアモンド","新潮","東洋経済"]
    
    return general,industr,Finance,traffic,steel__,constru,electri,fuel___,fiber__,Agricul,sport__,oversea,english,youth__ ,hobby__,evening ,small__ ,etc____

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
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    keylst = bool( dct['最大化'])##整数int:0はFalse,0でない数値はすべてTrue。
    return keylst

def ft(): #font
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
    keylst=['black','green','yellow','blue','aqua','purple','orange','silver','maroon','lime','navy','olive','fuchsia',"white","darkcyan","teal"]
    return keylst

def wd():##callで表示するkey
    keylst = ['区分','区間','名称1','号数','メモ1','メモ2','メモ3','メモ4']##順不同可。ls.kl()[5]  ls.wd()[6]  ls.wd()[7] ls.wd()[8]
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
def kp():#kaipage
    return '改ページ'
def hb():#haba
    return '幅'
def ak():#akaji
    return '赤字'

def alphabet():
    return ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def pa():#Place name
    keylst =['内幸町','永田町']
    return keylst
def ea(): #eria
    uchisaiwai_cho = ['人事院','弁護士会館','富国生命','プレスセンター','厚生労働省','日比谷国際ビル','パークフロント']
    nagata_cho = ['国会議事堂','総理大臣官邸','国会図書館']
    return uchisaiwai_cho, nagata_cho

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
def vc(): #vocabulary:用語
    keylst =['longs']
    return keylst
def pg(): #改ページ
    keylst =['改ページ','有効','無効']
    return keylst
