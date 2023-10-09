import winsound
import ls

class alr():
    def sound(): # Windowsシステム音の再生
        winsound.PlaySound('SystemExit', winsound.SND_ALIAS) # ['SystemExit','SystemHand']
        
    # {'メモ':''}に♪（八分音符）がある辞書があればシステム音を鳴らす。    
    def actv():
        start = ls.start() 
        end = ls.end() 
        lst = ls.customer() 
        # {'メモ':''}に♪（八分音符）がある辞書を抽出。　♪：八分音符（はちぶおんぷ）、音符、おたまじゃくし
        ld = [{ 'title': hss.get('名称1'), 'message': hss.get(i), 'detail': ''} for hss in lst[start:end] for i in ['メモ1','メモ2','メモ3','メモ4'] if '♪' in hss.get(i)] 
        if len(ld) > 0 :
            alr.sound()
            
if __name__ == '__main__':
    alr.actv()