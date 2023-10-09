import schedule
from time import sleep

class scdl(): # schedule
    def job( arr, i1):
        if len(arr) <= i1:
            #event.widget.flash()
            ("job関数　実行",len(arr), arr)
    
    def post( arr,i0 ,i1 ):
        schedule.every(i0).seconds.do( scdl.job, arr, i1)
        while len(arr) <= i1:# jobの実行監視、指定時間になったらjob関数を実行
            schedule.run_pending() # pending:保留中
            sleep(1)
            arr.append(len(arr))
 
if __name__ == '__main__':   
    scdl.post( [], 1 ,5) # （第二引数）秒ごとに（第三引数）回関数を実行する
    