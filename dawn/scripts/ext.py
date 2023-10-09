import tkinter as tk # external:外部
from ast import literal_eval
import sys, os
import ls, re, sync

def tategaki(string): 
    return '\n'.join(string[:12]).replace('ー', '丨')
    
def gomoji(string):  
    return '\n'.join(string[:5].rjust(5).replace('ー', '丨'))
    
def renew(number:int, Bool:bool, file:str)-> dict: # {'relord':False,'number':26,'file':'root.py'}
    (sys._getframe().f_code.co_name)

    dct = reader('renew.txt')
    dct['number'] = number
    dct['relord'] = Bool
    dct['file'] = file
    dct = str(dct).replace(" ","")
    dct = dct.replace( "}," ,"},\n" )
    file_ = "renew.txt"
    with open( file_, mode = 'w', encoding='utf-8') as f:
        f.write(dct)
  
def reader(file):
    sys._getframe().f_code.co_name
    with open(file, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    return dct 
        
def group( tpl, txt): # ('人事院', '') '1' 
    dct = ls.group() # {('人事院', ''): '1', ('弁護士会館', ''): '2', ('富国生命', 'A'): '3', ('富国生命', ''): '4', 
    dct[ tpl] = txt
    dct = str(dct).replace(" ","")
    with open( '../setting/group.txt' , mode = 'w', encoding='utf-8') as f:
        f.write(dct)

def long( i, value ): # '幅'を保存。
    key= ls.hb() # '幅'
    if int(value) >= 0 :        
        lst = ls.customer()
        lst[i][key] = value
        lst = str(lst).replace(" ","")
        store("customer.txt" ,lst)

def east_asian(txt)->int: # 半角を1文字、全角を2文字としてカウント
    import unicodedata
    count = 0
    for c in txt:
        if unicodedata.east_asian_width(c) in 'FWA': # F, W, Aは全角（= 2文字分）
            count += 2
        else:
            count += 1
    return count        

def half_full(txt, half, full)->tuple: # 半角・全角の文字数を返す。
    import unicodedata
    for c in txt:
        if unicodedata.east_asian_width(c) in 'HNaN': # H, Na, Nは半角（= 1文字分）
            half += 1
        elif unicodedata.east_asian_width(c) in 'FWA': # F, W, Aは全角（= 2文字分）
            full += 1
    return half,full     
                
def clr(txt):
    sys._getframe().f_code.co_name
    d = {'US版':'yellow','ゲンダイ':'salmon','フジ':'coral','ヴェリタス':'violet','F・T':'orange','F・T':'orange','F・T':'orange'}
    s = d.get(txt)
    
    if s == None :
        s = ls.cl()[1] 
    return s

def font_clr( dct, txt):  
    #,'aqua','purple','orange','silver','maroon','lime','navy','olive','fuchsia','white','darkcyan','teal'
    d = {'工':'mediumseagreen','日産':'royalblue','朝日':'orangered','毎日':'blue','読売':'goldenrod','日経':'midnightblue','東京':'indigo'}
    s = d.get(txt)
    if s == None :
        s = ls.cl()[0] 

    if dct != None and dct[txt]=='0': # 対象の新聞が0部の場合
        s = clr(txt)
    return s

def fg(txt):   
    if txt == '工':#
        color = "mediumseagreen"
    elif txt == '日産':#
        color = "royalblue"
    elif txt == '読売':#
        color = "goldenrod"
    else:
        color = ls.cl()[0] 
    return color 

# keyの抽出    
def ki( lst:iter, k :str)->iter: # keyx
    hss = { dic[ k ]: None for dic in lst } # {'人事院': None, '弁護士会館': None, '富国生命': None, 'プレスセンター': None, '厚生労働省': None, '日比谷国際ビル': None, 'パークフロント': None}
    return  hss

def divi_clr( lst, divi): # 区分によってwidgetの色分けをする関数   
    dct = ki( lst, ls.kb()) # keyの抽出 
    arr = list(dct)  
    if type(dct) != dict or divi not in arr:
        return None
    elif type(dct) == dict and divi in arr:
        inx = arr.index(divi)
        if inx < len(ls.sc()):
            color = ls.sc()[inx] if inx < len(arr) else ls.sc()[0]###:#system color
            return color
        elif inx <= len(ls.sc()):
            return "SystemButtonFace"
        else:
            return "SystemButtonFace"
        
# strからカラーネームを返す。        
def colr(txt:str):
    if isinstance(txt, int):
        return sc(txt)
    elif isinstance(txt, str):
        num = re.sub(r"\D", "", txt) # 半角＆全角の数字を取り出す, '1'
        if bool(num) and len(num)==len(txt):
            return sc(int(num))
        else:
            return 'SystemButtonFace'
    else:
        return 'SystemButtonFace'
    
# intからカラーネームを返す
def sc(num:int)-> str: # system color
    if num < len(ls.sc()): # 1
        return ls.sc()[num] # 'green'
    else: # 16以上
        return 'SystemButtonFace'
        
def warning( titl ,texT ,ee_):
    sub = tk.Toplevel( ee_ )
    sub.title( titl )
    ww = sub.winfo_screenwidth() 
    wh = sub.winfo_screenheight()
    sub.geometry( ls.ge(ww,wh) )
    tk.Label(sub,text = texT ).pack(pady=10)
    cansell = tk.Button(sub, text="戻る" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
    cansell.focus_set() 
    cansell.bind('<Return>',lambda event:sub.destroy() )
    cansell.pack()   

def ich(num:str)-> str:    
    if num == '1' or num == '0':
        return ''   
    else:
        return num
    
def check(sub):
    tk.Label(sub,text='未入力の箇所があります' ).pack()
    
def save( key ,value ):
    if int(value) >= 0 :
        sys._getframe().f_code.co_name
        dct = ls.num()
        dct[key] = value
        dct = str(dct).replace(" ","")
        dct = dct.replace( "}," ,"},\n" )
        file_name = "num.txt"
        with open(file_name, mode = 'w', encoding='utf-8') as f:
            f.write(dct)
def winfo( long):
    dct = ls.winfo()
    dct["w"] = long
    dct = str(dct).replace(" ","")
    dct = dct.replace( "}," ,"},\n" )
    file_name = "winfo.txt"
    with open(file_name, mode = 'w', encoding='utf-8') as f:
        f.write(dct)
     
def write(file , dct ):
    with open( '../setting/' + file, mode = 'w', encoding='utf-8') as f:
        f.write( str(dct))
        
def store(file ,lst ):
    (sys._getframe().f_code.co_name,file)
    lst = str(lst).replace(" ","")
    lst = lst.replace( "}," ,"},\n" )
    with open( '../setting/' + file, mode = 'w', encoding='utf-8') as f:
        f.write(lst)
    if file == 'customer.txt': 
        sync.dr.synq( "store")
        
def storage( path, file , lst): # バックアップとして"T:\"に保存。
    try:
        path = path + '/' + sync.dr.area() + '/' + sync.dr.d_d() + '/'
        os.makedirs( path, exist_ok=True) # exist_ok=Trueとすると既に存在しているディレクトリを指定してもエラーにならない。
        lst = str(lst).replace(" ","")
        lst = lst.replace( "}," ,"},\n" )
        with open( path + file, mode = 'w', encoding='utf-8') as f:
            f.write(lst)
    except:
        pass # 保存されなくても無視する。

def validate_input(val):
    fmt = '^[0-9][0-9]?[0-9]?$' # '^[+-]?[0-9]{1,2}(?:[0-9])?$'###'^[0-9][0-9]?$'
    if val=='' or re.match(fmt, val):
        return True
    return False 

def active(enter,label):  #
    enter.configure(state='normal')
    label.configure(fg='SystemButtonText')    
    
def hide(enter,WidgetVariable,label1,label2):  #
    enter.configure(state='readonly')
    WidgetVariable.set('')
    label1.configure(fg='SystemButtonFace')   
    label2.configure(text='')   
    

# 縦書き文字列上限 
def lmen( string, limen = 14, total = '')->list: # しきい値（閾値、しきいち）: threshold、limen
    itr = list(string)  
    tub, tin = [],[]
    for i in itr:
        total += i
        tin.append( i )  
        if len(total) == limen  or '。' in i : #　改行
            total = total.replace('。','')
            tub.append(total)
            total = ''
        elif len(tin) == len(string): 
            tub.append(total)
    (tub)    
    return tub if limen != 5 else tub[:1] # 名称の時はリストの要素を一つに制限する

def elim(val):#eliminate:除去
    fmt = '^\S*$'
    if val=='' or re.match(fmt, val):
        return True
    return  False

def rnd_up(string):
    nm = 14 ##縦書き文字列上限    
    roundedup = -( -len( string ) // nm) # ed up:切り上げ演算      
    return roundedup      

def exhibition(lst:list):#展示
    list(enumerate([0,1,2,3]))
    for k, v in {'dawn':'朝刊','dusk':'夕刊'}.items():
        pass
    
def Type_Hints( a:any, c:complex, o:object, i:iter, ):
    pass
    
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。 
    lst = ls.customer()
    exhibition(lst)
    divi_clr(lst , '人事院')
    storage( r'' + 'T:/', "customer.txt", lst )
    (lmen( 'あああああああああああああ水曜日木曜日', 14, ''))
    # robocopy /mir "\\DESKTOP-32KSG98\Public\therblig\dawn\paper" "C:\Users\jiro\Downloads" フォルダを同期
