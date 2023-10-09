import datetime # announcement of time:時報
import pyttsx3
import locale

class dates():
    def actv():
        locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
        now= datetime.datetime.now()
        days = now.strftime('%m月%d日')
        times = now.strftime(' %H:%M')
        
        #参照した言葉
        words = [ "本日は", days , ' ', times, "です"][1:2]
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
        
                
if __name__ == '__main__': 
    dates.actv()
