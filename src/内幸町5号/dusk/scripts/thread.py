from multiprocessing import Pool
import tkinter as tk

import time
#https://qiita.com/taka-kawa/items/d1fc1bc0acb3a6ca3031
def f(x):
    tk.Label( text=x).pack()#grid( row= x, column=n )
    return x*x

if __name__ == "__main__":
    N = [5, 10]
    root =tk.Tk()
    frame=tk.Frame(root)
    print("単純実装")    
    for n in N:
        start = time.time()
        for x in range(n):
            f(x)
            #tk.Label( frame, text=x).grid(row= x, column=n )
        print("n:{} time:{}".format(n, time.time()-start))
    print("並列処理")
    for n in N:
        start = time.time()
        for x in range(n):
            f(x)
            with Pool(processes=8) as pool:
                pool.map(f, range(n))
        print("n:{} time:{}".format(n, time.time()-start))   
    frame.pack()
    root.mainloop()
