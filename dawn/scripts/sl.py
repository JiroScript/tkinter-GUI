# solution:解法
import itertools 
import ls
#タプル内辞書を作成。
class TD():
    # 
    def D_LD_L( d:dict, ld:iter, arg:list )->tuple: 
        ( d ) # {'区分': '人事院', '区間': ''}
        ( ld ) # [{'区分': '人事院', '区間': '', '割当': '1'}, ]
        ( arg )
        for  i, hss in enumerate( ld ):
            bl =[ ( d .get(x) == hss.get(x) ) for x in arg ] # bool
            (bl)
            if sum(bl) == len(bl): 
                return i, hss # (0, {'区分': '人事院', '区間': '', '割当': 'None'})
# 配列内配列を作成。           
class LL():
    # 配列内辞書から抽出、argをキーとして抽出、配列内配列（イテラブル）を作成。
    def LD_L( ld :iter, arg :list)-> list: # 抜粋
        return  [[ dic.get(i) for i in arg ] for dic in ld ]
    
    # 配列内配列の同一の値の配列を統合
    def LL( itr :list, ll = [])-> list: # [[1,2,3],[1,2,3],[1,2,3]]
        for arr in itr: 
            (arr)
            if arr not in ll:
                ll.append(arr)
        return ll # [[1,2,3]]
    
    def D_S_L( dic:dict, con:str, arg:list):
        if con == "in" :
            ll = [[ k, v ] for k, v in dic.items() if k in arg ]
        elif con == "not in" :
            ll = [[ k, v ] for k, v in dic.items() if k not in arg ]
        return ll 
    
    def LD_S_S___( itr:list, con:str, arg:list )-> list: # 条件:conditions
        if con == "in" :
            ll = [ [ i , k ] for i in range( len( itr)) for k in itr[ i ].keys() if k in arg ]
        elif con == "not in" :
            ll = [ [ i , k ] for i in range( len( itr)) for k in itr[ i ].keys() if k not in arg ]
        return ll 
    
    def LD_S_L( itr:list, con:str, arg:list )-> list: # 条件:conditions
        if con == "in" :
            ll = [ [ i , k ] for i in range( len( itr)) for k in itr[ i ].keys() if k in arg ]
        elif con == "not in" :
            ll = [ [ i , k ] for i in range( len( itr)) for k in itr[ i ].keys() if k not in arg ]
        return ll 
    
    
    
class L():
    def L_S_L( itr:list, con:str, arg:list,): # 条件:conditions
        if con == "in" :
            l = [ i for i in itr if i in arg ]
        elif con == "not in" :
            l = [ i for i in itr if i not in arg ]
        return l 
    def LD( ld :iter)-> list: # 抜粋 [{'区分': '人事院', '区間': '', '割当': '1'}, {'区分': '弁護士会館', '区間': '', '割当': '2'}, 
        return [ i for dic in ld  for i in dic ] # ['区分', '区間', '割当', '区分', '区間', 
    
    def LD_S_D(ld:list, con:str, hss:dict): # [{'区分': '人事院', '区間': ''}, {'区分': '弁護士会館', '区間': ''}, {'区分': '富国生命', '区間': 'A'},
        (ld,con,hss)
        
        l=[]
        for i,dic in enumerate(ld):
            for k,v in dic.items():
                (v)
                if k in hss.keys() and v in hss.values():
                    (hss.keys() , hss.values())
                    l.append(i)
                    (v)
        (l)
        l=[]
        if con == "in" :
            l =  [ i for i, dic in enumerate(ld) for k,v in dic.items() if k in hss.keys() and v in hss.values()] # [2, 3]
        elif con == "not in" :
            l =  [ i for i, dic in enumerate(ld) for k,v in dic.items() if k in hss.keys() and v not in hss.values() ] # [0, 1, 4, 5, 6, 7, 8]
        return l 
        
    def LD_D( ld:list, hss:dict )->list: # 
        (ld, hss)
        s1 = set( ( i, dic.get('区分')) for i, dic in enumerate(ld) ) # {(3, '富国生命'), (0, '人事院'), (7, '日比谷国際ビル'), (4, 'プレスセンター'), (5, 'プレスセンター'), (8, 'パークフロント'), (1, '弁護士会館'), (2, '富国生命'), (6, '厚生労働省')}
        s2 = set( ( i, hss.get('区分')) for i, dic in enumerate(ld) ) # {(3, '富国生命'), (0, '人事院'), (7, '日比谷国際ビル'), (4, 'プレスセンター'), (5, 'プレスセンター'), (8, 'パークフロント'), (1, '弁護士会館'), (2, '富国生命'), (6, '厚生労働省')} {(3, '富国生命'), (7, '富国生命'), (0, '富国生命'), (4, '富国生命'), (1, '富国生命'), (5, '富国生命'), (2, '富国生命'), (6, '富国生命'), (8, '富国生命')}
        s3 = s1 - s2 # {(7, '日比谷国際ビル'), (0, '人事院'), (4, 'プレスセンター'), (5, 'プレスセンター'), (8, 'パークフロント'), (1, '弁護士会館'), (6, '厚生労働省')}
        l1 = [ i for i, s in s3 ] # [7, 0, 4, 5, 8, 1, 6]
        l2 = sorted(l1)
        return l2 # [0, 1, 4, 5, 6, 7, 8]
        
# 配列内辞書を作成。    dr.difr
class LD(): 
    def LD_L_L( ld:list, arg:list , l )->dict:
        ld = [ { k : v } for I in arg for k , v in ld[ I ].items() if k not in l ]
        return ld # [{'ア': '3'}, {'マ': '3'},]
    # 配列内辞書同士の差集合を配列内辞書で返す。
    def LD_LD_L( itr:list, ld:list, arg:list , arr=[])->list:
        for dic in itr:
            for  i, hss in enumerate( ld ):
                (dic,hss)
                if B.D_D_L( dic, hss, arg) :
                    arr.append( hss)
        return arr
    
    #配列内配列を配列内辞書に変換
    def LL(itr:iter, arg:list, dic:dict= {}, two:list = [])->list: # 
        (itr)
        for l in itr:
            ( l ) 
            for i in range( len( l )):
                dic = { **dic, **{ arg[i]: l [i] }}
            two.append(dic)
        (two)
        return two
    
# bool    
class B(): 
    # 二つの辞書,共通するの要素,値がすべて同じであればTrueを返す。
    def D_D_L( dic :dict, hss :dict, arg :list)-> bool: 
        l = [ ( dic.get(x) == hss.get(x) ) for x in arg ] # [True, True,]
        return sum( l ) == len( l ) # True, False
            
class DLD():
    def LD_DL( lst:iter, dl:dict, dic:dict= {})-> dict:  
        for s in dl : # {'1': [0, 1, 2, 3]}
            arg = dl [ s ] # [0, 1, 2, 3]
            itr = [ { k : v } for I in arg for k , v in lst[ I ].items() if k not in ls.kl()]
            dic[ s ] = itr 
        return dic # {'1': [{'ア': '3'}, {'マ': '3'}],'2': [{'ア': '5'}]}
            
class DD(): 
    # 辞書内辞書を作成。
    def LD_DL( lst:iter, dl:dict, dic:dict= {})-> dict: # 
        #
        dic = DLD.LD_DL( lst, dl, {})
        (DD.DLD( dic, {}))
        (dic)
        return DD.DLD( dic, {})
    # 辞書内配列内辞書を返す。
    # 辞書内辞書を返す。 {:{}}
    def DLD( dic:dict, dd )->dict:
        for s, ld in dic.items(): # {'1': [{'ア': '3'}, {'マ': '3'}],'2': [{'ア': '5'}]}
            (s,ld)
            hss = D.LD( ld , {} )
            dd[ s ]= hss
        return dd # 
    
    def LL_LD( ll:list, itr:list, hss:dict)->dict:
        for i, k in ll: # 
            hss.setdefault( i ,{})
            hss[ i ].setdefault( k , itr[ i ][ k ])
        return hss # {'0': {'': '', '': ''},'1': {'': '', '': ''}}
    
    def LD_S( lst, s ):
        DD = { dic.get( s ):{ k : v for k , v in dic.items() if k not in ls.kl() } for I , dic in enumerate(lst) } # { s:{k:v}}
        return DD # {'0': {'': '', '': ''},'1': {'': '', '': ''}}

        
class D():
    # 配列内辞書⇨辞書を返す。
    def LD( ld:list, hss:dict)->dict:
        for d in ld:
            (d)
            s0, s1 = T.D( d ) # 辞書をタプルに変換
            (s0,s1) # ア , 1
            hss.setdefault( s0, 0) 
            hss[ s0 ] += int( s1 )
        return hss # {'ア': 13, 'マ': 12, 'ヨ': 12}
    
    def LD_L( ld :iter,arg)-> list: # ls.customer()
        return  { dic.get(i):None for dic in ld for i in dic if i in arg } # {'人事院': None, '弁護士会館': None, '富国生命': None, 
    
class T():
    # 辞書をタプルに変換
    def D(dic:dict)->tuple:
        for s0, s1 in dic.items():
            return s0, s1
        
class LT():
    def T_T ( tpl0:tuple, tpl1:tuple ): # ( 3, 2*2, 2), ( 19, 19+3 )
        i0, i1, i2 = tpl0
        i3, i4 = tpl1
        i0 # column start
        i1 # column range -1
        i2 # column span
        i3 # row start
        i4 # row range -1
        l = [ ( c , r ) for r , c in itertools.product( range( i0, i1, i2), range( i3, i4 ) )]
        print(l)
        return l # [(19, 3), (20, 3), (21, 3)]
        
        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。  
    lst=ls.customer()
    LT.T_T( ( 3, 2*3, 2), ( 19, 19+3) ) # [(19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (19, 5), (20, 5), (21, 5), (22, 5), (23, 5), (24, 5), (19, 7), (20, 7), (21, 7), (22, 7), (23, 7), (24, 7), (19, 9), (20, 9), (21, 9), (22, 9), (23, 9), (24, 9)]
    itr = {'1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
           '2': [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]}
    ( DD.LD_DL( lst, itr, {}),)
    itr =[{'区分': '人事院', '区間': ''}, {'区分': '弁護士会館', '区間': ''}, {'区分': '富国生命', '区間': 'A'}, {'区分': '富国生命', '区間': ''}, {'区分': 'プレスセンター', '区間': 'A'}, {'区分': 'プレスセンター', '区間': ''}, {'区分': '厚生労働省', '区間': ''}, {'区分': '日比谷国際ビル', '区間': ''}, {'区分': 'パークフロント', '区間': ''}]
    (L.LD_S_D(itr, 'not in', { ls.kb():'富国生命'} ))
    L.LD_D(itr,  { ls.kb():'富国生命'})
    [ str(i) for i,dic in enumerate( itr,start=1)]