import sys
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from subprocess import Popen
import shlex
import time


class SyncUpload( PatternMatchingEventHandler ) :

    def __init__(self,*args, **kwargs):
        super(SyncUpload,self).__init__(*args,**kwargs)
        self.prcs = None

    def start(self, path ):
        self.watch_path  = path
        observer = Observer()
        observer.schedule( self, path, recursive=True )
        observer.start()

        try:
            observer.join()
        except KeyboardInterrupt:
            observer.stop()
        except:
            observer.stop()

    def on_any_event( self, evt ):
        if self.prcs and  self.prcs.poll() == None : # 実行中ならキャンセルする
            pass
        else:
            time.sleep(1)
            # cmd = "bash -c 'for  i in {1..3} ; do echo 1 ; sleep 1 ; done; ' "
            cmd = "rsync -avz  '%s'   server:path/to/dir/ " % self.watch_path
            self.prcs = Popen( shlex.split(cmd) )




if __name__ == '__main__':
    path = sys.argv[1] if len( sys.argv ) > 1 else './'

    obj = SyncUpload( ['*.php'] )
    obj.start( path )