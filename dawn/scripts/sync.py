import os
import sys
import pathlib
import datetime
import platform
import socket
import shelve
from ast import literal_eval
import re

#from smb.SMBConnection import SMBConnection
import ls

class cnc():
    # 通信の有無、関連情報を返す 
    def smb(): # pssmb:ファイル共有を利用できるモジュールで、SMB/CIFSクライアントとして動作します。
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        hostname = ('[%s]' % socket.gethostname())[1:-1] # ホスト名
        ip4ad = socket.gethostbyname(hostname) # IPv4アドレス
        try:
            conn = SMBConnection(
                '<user>',
                '<password>',
                platform.uname().node,
                hostname, # <remote_hostname>DESKTOP-32KSG98
                domain = '', # 「指定しない」'WORKGROUP'
                use_ntlm_v2 = True)
            conn.connect(ip4ad, 139)#192.168.50.246
            items = conn.listPath( 'Public', ix.ph()['source'], pattern= 'customer.txt')###,サーバー側の共有フォルダ名,path,pattern:検索結果のフィルタ
            items = [item.filename for item in items]
            
            conn.echo('success')
            if 'customer.txt' in items:
                return True, conn # (True, <smb.SMBConnection.SMBConnection object at 0x000001F26483B5C8>)
            conn.close()
        except Exception as e:
            ('type:' + str(type(e))
            ,'args:' + str(e.args)
            ,'e自身:' + str(e))
            return  False, None
            conn.close()
            
    def stte(boolean:bool, stt:str)->str:
        if dr.therblig(): # srcフォルダの有無, bool
            stt = "normal"
        if boolean == True: 
            stt = "normal"
        elif boolean == False: 
            stt = "disabled"
        return stt
    
    
class S():
    def hostname():
        try:
            return ('[%s]' % socket.gethostname())[1:-1] # 'LAPTOP-9BTLS87T'
        except :
            return False        
        
class dr(): # Connection:接続
    # ファイルの送受信、およびBoolを返す
    def synq( string:str): # ファイルを同期する
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 

        boolean, conn = cnc.smb() # SMBConnection
        if dr.exis() and boolean:
            if string == "store": # 保存    
                dr.store( conn)
                conn.close()
            elif string == "retrieve": # retrieve:取得
                dr.retrieve( conn)
                conn.close()
        
        elif dr.exis() == False or boolean == False:
            return False
        
    # 送信        
    def store(conn): # store:保存      
        with open( ix.ph()['client'], 'rb') as file: # '../'+ 'setting' +'/'+ 'customer.txt'
            conn.storeFile( 'Public', ix.ph()['host'], file) # \therblig\src\内幸町8号\dusk\setting\customer.txt 
        file.close()
        
    # 受信    
    def retrieve(conn): # retrieve:取得 
        with open( ix.ph()['client'], 'wb') as file:
            conn.retrieveFile( 'Public', ix.ph()['host'], file) 
        file.close()
        
    # 各フォルダの有無をboolで返す。
    def exis()->bool: # existence:存在, 有無,
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        try:
            if dr.therblig() == False:
                bl = False
            if dr.area() == False:
                bl = False
            elif dr.area() != False:
                bl = True
            return bl  
        except ( FileNotFoundError, TypeError):
            return False
        
    # src・sysフォルダ配下であればTrueを返す。
    def src()->bool: # Under the directory:ディレクトリ 配下
        return 'src' in __file__ or 'sys' in __file__ 
        
    def therblig()->bool: # Under the directory:ディレクトリ 配下
        return 'therblig' in __file__ or 'sys' in __file__ 

    def customer(ph):
        file_ = ph # + 'customer.txt'
        with open(file_, "r", encoding='utf-8') as f:
            data_list = f.read()        
        text = data_list.replace(" ","")
        lst = literal_eval(str(text))#文字列をリストや辞書に変換
        return lst
    
    def client()->list: # 
        try:
            return os.listdir( ix.dr()['階層'] ) # ['dawn', 'source.txt', 'src', 'sys', '内幸町8号']
        except FileNotFoundError:
            return False
        
    def host()->list: # (ix.dr()['階層'] + '../'+'host')
        try:
            return os.listdir( ix.dr()['階層'] + 'src' ) # ['内幸町1号', '内幸町3号', '内幸町5号', '内幸町8号']
        except FileNotFoundError:
            return False
    
    # "区域"を返す。
    def area(): # 内幸町8号
        return dr.brnc( dr.client(),dr.host(), )
    
    def brnc( client:list,host:list,): # Conditional branch:条件分岐 
        #共通するフォルダ名をsetで返す。
        common = set(client) & set(host) # {'内幸町8号'}
        #共通するフォルダの数
        length = len(common) 
        if bool(common) == False:
            ele = False            
            ("共通するフォルダがありません")
        elif length == 0:
            ele = False
            ('/'+ix.dr()['システム名']+'/に' + "必要なフォルダがありません" )
        elif bool(common) and length == 1:
            ele = "".join(common)
            (ele)
        elif length > 1:
            ele  = False
            ('/'+ix.dr()['システム名']+'/に' + "不必要なフォルダがあります" )
        return ele 
        
    # 'dusk',' dawn'、実行中のファイルの絶対パスに含まれている方を返す
    def d_d(): # dusk or dawn
        if "dusk" in __file__: #　__file__:実行中のファイルの絶対パス
            return "dusk"
        elif 'dawn' in __file__:
            return "dawn"
                    
    def directory(): # directory
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        ( 'DESKTOP-32KSG98', 'laptop-9btls87t' )
        os.getcwd() # カレントディレクトリを表示
        ph= '../'
        ([ li for li in os.listdir( ph) if os.path.isdir( os.path.join( ph, li))])
                
        path = ix.dr()['階層'] + 'therblig' 
        for d, s, f in os.walk(path):
            ('')
            ('── {}'.format(d))
            (' └── {}'.format(s))
            ('   └── {}'.format(f))
            
    # 更新時間の取得。     
    def date(ph):
        pathlib.Path(ph)
        t = os.path.getmtime(ph)
        d = datetime.datetime.fromtimestamp(t)
        d
        
    # 日本語が含まれていればTrueを返す。
    def jpn( txt = "鎌鼬"):
        return bool( re.search('[あ-んア-ン一-鿐]', txt )) #文字列すべてが検索対象で、先頭にない文字列にもマッチする。match()と同じく、マッチする場合はマッチオブジェクトを返す。
    
    def shlf(): # shelfは動作速度が遅い
        inx = shelve.open( 'index')
        inx['dir'] = { '階層':'./../../', 'システム名':'therblig', 'src':'src'}
        inx['dir']
        inx.close()
        
        inx = shelve.open('index',writeback= True)
        inx['dir']['dusk']='hello'
        inx.close()
        
           
class ix():
    def dr(): # directory
        return { '階層':'./../../', 'システム名':'therblig', '区域':'area', 'file':'setting/customer.txt'}
           
    def ph():###起源：source,端末:terminal,本体:host
        dic= {'source':'/'+ 'therblig' + '/'+ 'src'+ '/'+ dr.area()+ '/'+ dr.d_d()+ '/'+ 'setting' + '/',
              'client': '../'+ 'setting' +'/'+ 'customer.txt', # 'terminal'　端末
              'host': ix.path() + 'customer.txt' }
        return dic
    # \therblig\src\内幸町8号\dusk\setting\customer.txt 
    def path():
        return '/'+ ix.dr()['システム名']+ '/'+ 'src'+ '/'+ dr.area()+ '/'+ dr.d_d()+ '/'+ 'setting' + '/'#+ 'customer.txt'
    # \\DESKTOP-32KSG98\Public\therblig\src\内幸町8号\dusk\setting\customer.txt   
    
if __name__ == '__main__': # これがないと外部からインポートされた際に処理が実行されてしまう。      
    cnc.smb#() # 通信の有無、関連情報を返す,(True, <smb.SMBConnection.SMBConnection object at 0x000001F26483B5C8>, '通信が確立されました')
    volume = 'Z:/'
    (os.listdir(volume)) # 
    file = r'' + volume + 'customer.txt'
    file = r'\\DESKTOP-FFUQU9R\Users\Public\therblig\dawn\scripts\root.py'
    file = r'\\LAPTOP-9BTLS87T\Public\therblig\dawn\scripts\root.py'
    os.startfile(file, operation='open') # ファイルを開く

    dr.shlf # shelfは動作速度が遅い
    print(dr.area())        
    print(dr.client(), dr.host())
    # (dr.synq( "store"))
    # (dr.synq( "retrieve")) # retrieve:取得 
    (os.listdir( './../../' + '../' )) # Publicフォルダ
    (os.path.isdir('./../../' + '../host')) # ディレクトリの存在確認
    (os.path.basename(__file__),) # sync.py
    (os.path.split(__file__),) # ('\\\\laptop-9btls87t\\Public\\therblig\\dawn\\scripts', 'sync.py')
    (os.path.exists(os.path.basename(__file__)),) # True
    dr.directory()
    S.hostname()