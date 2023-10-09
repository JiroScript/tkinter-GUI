import os
import sys
import pathlib
import datetime
from ast import literal_eval
sys.path.append(os.path.join('../', 'scripts'))
import ls
import panda

class anlys():###数値,analysis:解析,
    
    def post():
        os.path.exists('../src/内幸町8号')#C:\Users\jiro\Documents\WPy64-3741\scripts
        os.path.exists('./lan.py')
        print(os.listdir(path='./../src/'))
        os.path.exists('C:/Users/Public/Videos')#DESKTOP-32KSG98/Videos
        
        os.getcwd()#カレントディレクトリを表示
        ph= '../src/'
        pathlib.Path(ph)
        t = os.path.getmtime(ph)
        d = datetime.datetime.fromtimestamp(t)
        print(t,d)
        print([li for li in os.listdir(path=ph)	if os.path.isdir(os.path.join(ph,li))])
        di = '../src/'###directory:「住所録」
        ct = '/dusk'
        ory= '/setting/customer.txt'
        dct={}
        for re in os.listdir(path= di):
            if os.path.isdir(os.path.join(di, re)) and os.path.exists(di+re+ct+ory):
                #print(di+re+ct+ory, os.path.exists(di+re+ct+ory))
                print(anlys.num(anlys.customer(di+re+ct+ory)))
                #dct[re]=anlys.customer(di+re+ct+ory)
        print(dct)
        
    def customer(directory): 
        file_ = directory
        with open(file_, "r", encoding='utf-8') as f:
            data_list = f.read()        
        text = data_list.replace(" ","")
        lst = literal_eval(str(text))#文字列をリストや辞書に変換
        return lst
    
    def num(lst):###  
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        keylst = ls.kl()
        d__= {}
        dic= {}
        dc = {}       
        di_= {}
        for i in range(len(lst)):
            for  tp in lst[i].items(): 
                ky= tp[0]
                vl= tp[1]
                #
                if ky not in keylst:
                    d__.setdefault( ky, 0)
                    d__[ky] += int( vl) #if ky not in dic[ lst[i][ls.kb()] ].keys() else int(dic[ lst[i][ls.kb()]][ky]) +  int(vl)
                    
                    dic.setdefault( lst[i][ls.kb()] ,{})
                    dic[ lst[i][ ls.kb()] ].setdefault( ky,0)#( ..)φメモメモ：ネスト構造
                    dic[ lst[i][ ls.kb()]][ky] = int(vl) if ky not in dic[ lst[i][ls.kb()] ].keys() else int(dic[ lst[i][ls.kb()]][ky]) +  int(vl)
                    dc.setdefault(ky,None)
                di_= anlys.section( lst, di_, keylst, i, ky, vl)
                
        dict = panda.cum.fmat(dic)
        dict["人事院"]['マ']
        return d__, panda.cum.fmat(dic), panda.cum.fm_t(dc), di_
          
    def section( lst, di_, keylst, i, ky, vl):
        if ky not in keylst or ky in ls.kk():
            di_.setdefault( lst[i][ls.kb()], {})
            if ky in ls.kk():
                di_[ lst[i][ ls.kb()]].setdefault( vl, {})
                #print( di_[ lst[i][ ls.kb()]])
            if ky not in ls.kk():
                #print(di_[ lst[i][ ls.kb()]] )
                di_[ lst[i][ ls.kb()]][ lst[i][ ls.kk()]].setdefault( ky,0)
                di_[ lst[i][ ls.kb()]][ lst[i][ ls.kk()]][ky] = int(vl) if ky not in di_[ lst[i][ ls.kb()]][ lst[i][ ls.kk()]].keys() else int(di_[ lst[i][ ls.kb()]][ lst[i][ ls.kk()]][ky] ) +  int(vl)
        return di_
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。       
    anlys.post()