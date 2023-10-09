import tkinter as tk #external:外部
from ast import literal_eval
import ls 
import sys
import re
import sti
import math
import msg
import ext

def tategaki(string): 
    nm = 12#14
    moj = ','.join(string[:nm])#'丨'
    moj = moj.replace('ー','丨')
    moj = moj.replace(',','\n')
    return(moj)
    
def yonmoji(string):  
    s  = (4-len(string)) * ' '
    #print(5-len(string),s,len(s))
    string = s + string
    moj  = ','.join(string[0:4])
    moj = moj.replace(',','\n')
    moj = moj.replace('ー','丨')
    return(moj)
    
def gomoji(string):  
    s  = (5-len(string)) * ' '
    #print(5-len(string),s,len(s))
    string = s + string
    moj = ','.join(string[0:5])
    moj = moj.replace(',','\n')
    moj = moj.replace('ー','丨')
    return(moj)
    
def reLORD():
    file_ = "relord.txt"
    with open(file_, "r", encoding='utf-8') as f:
        data_list = f.read()        
    text = data_list.replace(" ","")
    dct = literal_eval(str(text))#文字列をリストや辞書に変換
    return dct 
def RElord(Bool):
    sys._getframe().f_code.co_name
    dct = reLORD()
    dct[ ls.dl()[5]] = Bool
    dct = str(dct).replace(" ","")
    dct = dct.replace( "}," ,"},\n" )
    file_ = "relord.txt"
    with open( file_, mode = 'w', encoding='utf-8') as f:
        f.write(dct)
  
def group(key,value):
    sys._getframe().f_code.co_name
    dct = ls.group()
    dct[ key] = value
    dct = str(dct).replace(" ","")
    with open( '../setting/group.txt' , mode = 'w', encoding='utf-8') as f:
        f.write(dct)

def long(i, value ):
    sys._getframe().f_code.co_name
    key='幅'
    if int(value) >= 0 :        
        lst = ls.customer()
        lst[i][key] = value
        lst = str(lst).replace(" ","")
        ext.store("customer.txt" ,lst)
        
tIME=[]    
def timer(root,timE,status): 
    global tIME
    if len(tIME) == 0 :
        tIME.insert(0,math.floor(timE))
    elif  len(tIME) >0 :
        tIME.insert(0,math.floor(timE))
        tim = tIME[0]- tIME[1]
        print(len(tIME),tIME[0],tim)
        if tim <=2:
            print("yellow")
            msg.alart() 
        
def clr(text):
    sys._getframe().f_code.co_name
    if text in "US版":#
        color = "yellow"
    elif text in "ゲンダイ":#
        color = "salmon"
    elif text in "フジ":#
        color = "coral"
    elif text in "ヴェリタス":#
        color = "violet"
    elif text in "F・T":#
        color = "orange"
    else:
        color = ls.cl()[1]
    return color

def font_clr(dct, text):   
    if text == '工':#
        color = "mediumseagreen"
    elif text == '日産':#
        color = "royalblue"
    elif text == 'ヨ':#
        color = "goldenrod"
    else:
        color = ls.cl()[0] 
    if text in sti.sti.wk() :
        color = ls.cl()[1]
    if dct[text]=='0':
        color = clr(text)
    return color  ##if not text in sti.sti.wk() else ls.cl()[1]

def fg(text):   
    if text == '工':#
        color = "mediumseagreen"
    elif text == '日産':#
        color = "royalblue"
    elif text == 'ヨ':#
        color = "goldenrod"
    else:
        color = ls.cl()[0] 
    return color 
def category(lst):
    ls.nm(None,None,sys._getframe().f_code.co_name).class_def()
    dic = { lst[i][ls.kb()]:None for i in range(len(lst))}
    return dic, None   

def divi_clr(cate_divi, divi):###区分によってwidgetの色分けをする関数   
    dic = cate_divi#ls.group()
    if type(dic) != dict or divi not in list(dic):
        return None
    elif type(dic) == dict and divi in list(dic):
        arr=list(dic)  
        inx = arr.index(divi)
        if inx < len(ls.sc()):
            color = ls.sc()[inx] if inx < len(arr) else ls.sc()[0]###:#system color
            return color
        elif inx <= len(ls.sc()):
            return "SystemButtonFace"
        else:
            return "SystemButtonFace"
    
def relieF(text):
    if text in ls.nw()[0]:#'サ'
        element = "groove"
    else:
        element= "raised"
    return element
def font(text):
    if text in ls.nw()[0][3]:#'サ'
        size = ( "メイリオ",ls.ft()[1]) 
    else:
        size = ( "メイリオ",ls.ft()[1]) 
    return size

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

def ichi(digi):    
    if digi == '1':
        digi = ''   
    if digi == '0':
        digi = ''
    else:
        pass
    return(digi)
    
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
    sys._getframe().f_code.co_name
    dct=ls.winfo()
    dct["w"]=long
    dct = str(dct).replace(" ","")
    dct = dct.replace( "}," ,"},\n" )
    file_name = "winfo.txt"
    with open(file_name, mode = 'w', encoding='utf-8') as f:
        f.write(dct)
            
def store_prot(file_ ,lst ):#試作
    key = list( ls.dusk_dawn().keys())[0]
    val = ls.dusk_dawn()[ key]
    
    if file_ == "customer.txt" :
        file_ = val + ".txt"        
    lst = str(lst).replace(" ","")
    lst = lst.replace( "}," ,"},\n" )
    sys._getframe().f_code.co_name
    with open( '../setting/' + file_, mode = 'w', encoding='utf-8') as f:
        f.write(lst)
        
def store(file_ ,lst ):
    lst = str(lst).replace(" ","")
    lst = lst.replace( "}," ,"},\n" )
    sys._getframe().f_code.co_name
    with open( '../setting/' + file_, mode = 'w', encoding='utf-8') as f:
        f.write(lst)

def validate_input(val):
    fmt = '^[0-9][0-9]?[0-9]?$'###'^[+-]?[0-9]{1,2}(?:[0-9])?$'###'^[0-9][0-9]?$'
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
    
def list_index(val,lst):
    if val !='' and int(val) <= len(lst)-1 :
        print(type(val),int(val),len(lst))
        return  lst[int(val)][ls.wd()[1]]
    elif val !='' and int(val) > len(lst)-1:
        return "該当する情報がありません"

def cnv_list(string):#conversion for list
    nm = 14 ##縦書き文字列上限 
    ln = len(string)
    wr = list(string)   
    total = ""    
    i = 0
    ii = 0
    tub = []
    for item in wr:
        total += item
        ##print(item,i,len(total))
        i += 1
        ii += 1
        
        if i == nm or ii == ln or '。' in item:
            total = total.replace('。','')
            tub.append(total)
            i=0
            total=""
            continue        
    return tub  

def cnv_name(string):#conversion for list
    nm = 5 ##縦書き文字列上限 
    ln = len(string)
    wr = list(string[:10])   
    total = ""    
    i = 0
    ii = 0
    tub = []
    for item in wr:
        total += item
        ##print(item,i,len(total))
        i += 1
        ii += 1
        
        if i == nm or ii == ln or '。' in item:
            total = total.replace('。','')
            tub.append(total)
            i=0
            total=""
            continue        
    return tub  
def elim(val):#eliminate:除去
    fmt = '^\S*$'
    if val=='' or re.match(fmt, val):
        return True
    return  False

def rnd_up(string):
    nm = 14 ##縦書き文字列上限    
    roundedup = -( -len( string ) // nm) # ed up:切り上げ演算      
    return roundedup      
def exhibition(lst):#展示
    dic = { lst[i][ls.kb()]:None for i in range(len(lst))}
    arr = [ li[ls.kb()] for li in lst ]
    ar_ = [lst[i][ls.kb()] for i in range(len(lst))]
    rev = [ lst[i][ls.kb()] for i in range(len(lst))[::-1]]
    tup = list(enumerate(arr))
    [ tp for tp in enumerate(rev)]
    divi = list(dic)
    arr,    ar_,   tuple(arr),    tup,    [arr.index(item) for item in divi]
    [ tp if tp[0] == 0 or tp[0] != 0 and arr[tp[0 ]-1] == tp[1] else tp[1] for tp in enumerate(arr)]
    [ i if i == 0 or i != 0 and lst[i-1][ls.kb()] != lst[i][ls.kb()] else None for i in range(len(lst))]
    keylst = ls.kl()

    [ [(lst[i][ls.kb()], di == lst[i][ls.kb()]) for i in range(len(lst))] for di in divi ]
    #print(arr.pop("人事院"))
    [rev.index(item) for item in divi[::-1]]
    list({ lst[i][ls.kb()]:None for i in range(len(lst)) })
    { np:lst[0][np] for np in lst[0] if np not in keylst }
    [[ n for n in lst[i] if n not in keylst ] for i in range(len(lst))]
    [ {k:v} for i in range(len(lst)) for k,v in lst[i].items() if k not in keylst ]
    { k:int(lst[i][k]) for i in range(len(lst)) for k in lst[i] if k not in keylst }
    { k:int(lst[i][k]) for i in range(len(lst)) if i==0 or i==3 for k in lst[i] if k not in keylst }
    [{k:v} for i in range(len(lst)) for k,v in lst[i].items() if k not in keylst ] 
    
   
    s = 'zero' if  0 in [10, 1] else "not in zero" if 1 not in [0, 10] else "not in one"# 条件式（三項演算子）の基本パターン # 条件式のネスト
    print(s)  # positive
            
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。 

    lst = ls.customer()
    exhibition(lst)
    dic = category(ls.customer())[0]
    divi_clr(dic , '人事院')