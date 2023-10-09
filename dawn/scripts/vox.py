import datetime # vox（ラテン語）:声
import pyttsx3
import locale
import ls
import msg

class dates():
    def actv():
        locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
        now= datetime.datetime.now()
        days = now.strftime('%m月%d日')
        times = now.strftime(' %H:%M')
        
        #参照した言葉
        words = [ "本日は", days , ' ', times, "です"][:2]
        #参照した言葉の出力
        word = "".join(words)
        # メッセージ
        voice.S( word)
        
class voice():
        
    def S(word):
        engine = pyttsx3.init()
        engine.getProperty("rate")
        engine.setProperty("rate",120)
        engine.getProperty('volume')
        engine.setProperty('volume',2.0)
        #
        engine.say(word)
        engine.runAndWait()
        
class LD():
    def LD_L_T( lst, itr, tpl):
        arr = []
        dct = {}
        start, end, txt = tpl
        for hss in lst[start:end]:
            for i in itr:
                ( i, hss.get(i))
                if '※' in hss.get(i):
                    ( bool ('※' in hss.get(i)), i, hss.get(i), hss.get(i).index('※'), hss.get(i)[hss.get(i).index('※'):])
                    dct = { **dct, **{ 'title': hss.get('名称1'), 'message': hss.get(i), 'detail': ''}}
                    arr.append( dct)
        return arr
        
class alr():
    # {'メモ':''}に※がある辞書があれば、読み上げ、ウィジェットを出現させる。    
    def actv():
        start = ls.start() 
        end = ls.end() 
        lst = ls.customer()
        # {'メモ':''}に※がある辞書を抽出。
        arr = LD.LD_L_T( lst, ['メモ1','メモ2','メモ3','メモ4'], ( start, end, '※')) # [{'title': '秘書室①', 'message': '人事※院', 'detail': ''}, {'title': '広告室③', 'message': '※', 'detail': ''}] [{'title': '秘書室①', 'message': '人事※院', 'detail': ''}, {'title': '広告室③', 'message': '※', 'detail': ''}]
        ld = [{ 'title': hss.get('名称1'), 'message': hss.get(i), 'detail': ''} for hss in lst[start:end] for i in ['メモ1','メモ2','メモ3','メモ4'] if '※' in hss.get(i)] 
        
        if len(ld) > 0:
            alr.loop( arr)
        
    def loop( arr):
        # 参照した言葉
        for dct in arr:
            txt = dct.get('message')
            inx = txt.index('※')
            ( dct.get('message'), txt, inx )
            ( txt[inx:], txt[ inx + 1:])
            dct['message'] = txt[ inx + 1:] #　※印以降の文字列をスライス
            (dct)
            msg.sr.alr( dct) # ウィジェットを出現させる
            voice.S( dct.get('message')) # 読み上げ
                
if __name__ == '__main__': 
    alr.actv()
    # module:モジュールとはPythonのファイル（.py）の事です。
