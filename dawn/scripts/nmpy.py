import os
import numpy as np
import log

    
class I():
    def exhibition(): # 展示
        arr = np.array([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        arr = np.array([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 238]).reshape(3, 4)
        arr.ndim
        arr.T.ndim
        
class T():
    def DD( dd:dict, dct )->list: # 差集合を追加
        tpl = log.anlys.nw() # ('ト', '産', 'サ', 'ヨ', 'マ', 'ア', '工', '日産', 
        for K, V in dd.items():
            for k in V:
                dct[ k] = None
        # dct['鎌鼬'] = None
        ( dct)
        ({ k for K, V in dd.items() for k in V })
        dct.keys(),
        sets = { k for K, V in dd.items() for k in V }
        ( sets - set(tpl), len( sets - set(tpl)))
        sets = sets - set(tpl) # {'鎌鼬'}、　差集合
        if bool( sets):
           lis = [ i for i in sets ] # ['鎌鼬']
           l = list(tpl) + lis
           tpl = tuple(l)
        ([ tpl.index(i) for i in sets ]) # [5, 4, 3, 2, 1, 0, 8, 10, 41, 29, 33, 35, 56, 34, 6, 7, 9, 39, 32, 16, 24, 19, 23, 42, 38, 47, 48, 58, 37, 26, 59, 15, 27, 22, 13, 17, 85]
        
        return tpl # ('ト', '産', 'サ', 'ヨ', 'マ', 'ア', '鎌鼬')
   
class L():
    #　行方向の差分を取得
    def L_D( arr, d ):
        nparr = np.array( arr) # [ 203 181 355 270 247 271 203 181 355 270 248 272 ]
        nparr = nparr.reshape( d['r'], d['c']) # [[203 181 355 270 247 271] [203 181 355 270 248 272 ]]
         # 差分、行方向 
        nparr = np.diff( nparr, axis=0) 
        (nparr.ndim, nparr.T.ndim, nparr.shape, len(nparr)) #  
        return nparr# [[ 0  0  0  0  1  1 ]
    
class D(): 
    def DD( dd:dict)-> dict:
        dd = DD.DD( dd, {}) # {'20220606170712.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, '流通': 16, 'フジサンケイ・ビジネスアイ': 1, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2},
        tpl = T.DD( dd, {}) # ('ト', '産', 'サ', 'ヨ', 'マ', 'ア', '鎌鼬')
        arr = [ V.get( i, 0) for K, V in dd.items() for i in tpl ] # [ 203 181 355 270 247 271 203 181 355 270 248 272 ]
        
        # nparrayを作成。
        nparr = L.L_D( arr , { 'r':len(dd), 'c': len(tpl) } ) 
        # [[ 0  0  0  0  1  1  0  0  0  0  0  0  0  0  0  0  0  ]
        #  [ 0  0  0  0  0  0  1  1  0  0  0  0  0  0  0  0  0  ]
        #  [ 0  0  0  0  0  0 -1  0  0  0  0  0  0  0  0  1  1  ]]
        
        # 非ゼロ要素のインデクスを取得
        sets= { tpl[i] for i in np.nonzero(nparr)[1] } # { 'マ', 'ア', '工', '鉄鋼' }
        lis = [ i for i in tpl if i in sets ]
        arr = [ V.get( i, 0) for K, V in dd.items() for i in lis ] # ['マ', 'ア', '工', '鉄鋼']
        nparr = L.L_D( arr , { 'r':len(dd), 'c': len(lis) } ) # [[ 1  1  0  0] [ 0  0  1 -1]]
        return { 'keys':dd.keys(), 'nw':lis, 'nparray':nparr, 'np.shape':nparr.shape } # Multidimensional array
    
class DD(): 
    #　ソート 、　”更新日時”順に
    def DD( dd:dict, duo ):
        ( dd) # {'20220101000018.txt': {'ア': 271, 'マ': 247, 'ヨ': 271,
        ( os.listdir('../log/'), len( os.listdir('../log/')))
        for txt in log.dirc.srt(): # ['20220609030618.txt', '20220609090722.txt', '20220609223354.txt']
            ld = log.anlys.customer('../log/' + txt)
            duo[ txt] = log.anlys.num( ld, {}) 
        return duo # {'20220606170712.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, '流通': 16, 'フジサンケイ・ビジネスアイ': 1, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2},

if __name__ == '__main__': # これがないと外部からインポートされた際に処理が実行されてしまう。    
    dd = {'20220606170712.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, '流通': 16, 'フジサンケイ・ビジネスアイ': 1, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}, '20220606173754.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, '流通': 16, 'フジ': 2, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, '自動車': 3, 'せんけん': 2}, '20220606191115.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, '流通': 16, '埼玉建設': 1, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}, '20220606191218.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, '流通': 16, 'ヴェリタス': 43, '日本証券': 1, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}, '20220607172323.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, '流通': 16, 'ヴェリタス': 43, '日本証券': 0, '日産': 72, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}, '20220607172408.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, '流通': 16, 'ヴェリタス': 43, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}, '20220607172415.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, '流通': 16, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}, '20220610173831.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, 'ショッピング': 1, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, '流通': 15, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}, '20220610173900.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, '流通': 15, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}, '20220610200028.txt': {'ア': 271, 'マ': 248, 'ヨ': 272, 'サ': 356, '産': 180, 'ト': 203, 'A': 15, '農業': 10, '報知': 1, 'スポニチ': 3, '碁': 2, '日刊スポ': 10, '工': 35, '日産': 62, '流通': 15, 'ヴェリタス': 42, 'F・T': 9, 'ガイド': 7, '海事': 10, 'でんき': 75, '建通': 1, '電波': 6, 'Y': 5, 'デイリー': 4, '朝日小学生': 3, '朝日中高生': 2, 'ゲンダイ': 5, '東スポ': 1, 'ぜんせき': 7, 'フジ': 1, '自動車': 3, 'せんけん': 2}}
    DD.DD( dd, {}) # ソート 、　”更新日時”順に
    T.DD( dd, {})
    D.DD( dd)
    dd = {'20220606170712.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203},    '20220606173754.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203},    '20220606191115.txt': {'ア': 271, 'マ': 247, 'ヨ': 271, 'サ': 356, '産': 180, 'ト': 203}}
