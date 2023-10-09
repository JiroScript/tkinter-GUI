import time
import atexit
import tkinter as tk

def setup():
    print("!!!Set up!!!")
def ext(root):
    print(" !")
    try:
        root.destroy()
        #sys.exit()
        ###os.kill(os.getpid(), signal.SIGINT)
    except SystemExit:  # 処理する例外の型が指定されている
        pass
        print('SystemExit!') # ここが実行される
    except NameError as e:
        print(type(e),e) 
    except KeyError as e:
        print(type(e),e) 
    except TypeError as e:  # 
        print(type(e),e) 
    except Exception as e:  # 
        print(type(e),e) 
    except: # NameError 以外はここで処理
        print('Unknown exception!')
    else:
        print('Everything went ok.') 
    finally:
        print('Always executed.') 

def main():
    setup()
    time.sleep(1)
    root = tk.Tk()
    #tk.Button(root,command=lambda:root.destroy() ,text='button' ,relief="groove" ,bd=4).pack( padx=1 ,pady=1)
    tk.Button(root,command = root.quit ,text='button' ,relief="groove" ,bd=4).pack( padx=1 ,pady=1)
    
    tk.Button(root,command=lambda:ext(root) ,text='button' ,relief="groove" ,bd=4).pack( padx=1 ,pady=1)
    
    root.mainloop() 
    
    try:
        atexit.register(print("atexit!"))
    except SystemExit:  # 処理する例外の型が指定されている
        pass
        print('SystemExit!') # ここが実行される
    except NameError as e:
        print(type(e),e) 
    except KeyError as e:
        print(type(e),e) 
    except TypeError as e:  # 
        print(type(e),e) 
    except Exception as e:  # 
        print(type(e),e) 
    except: # NameError 以外はここで処理
        print('Unknown exception!')
    else:
        print('Everything went ok.') 
    finally:
        print('Always executed.') 

if __name__ == "__main__":
    main()