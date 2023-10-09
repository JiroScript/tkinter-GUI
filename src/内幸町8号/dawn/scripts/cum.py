import tkinter as tk
import ls
import sys
import os
import re
import ext
class cum(): #Cumulative:累計
    def post():
        lst = ls.customer()
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        keylst = ls.wd() + ls.tm()
        dic={}
        for i in range(len(lst)):
            for n, ke_ in enumerate( lst[i].keys() ): 
                if ke_ not in keylst :
                    dic.setdefault( lst[i][ls.wd()[0]] ,{})
                    dic[ lst[i][ls.wd()[0]] ].setdefault(ke_,0)#( ..)φメモメモ：ネスト構造
                    ##print(lst[i][ls.wd()[0]],ke_, ke_ in dic[ lst[i][ls.wd()[0]] ].keys(),   "None" if ke_ not in dic[ lst[i][ls.wd()[0]] ].keys() else dic[ lst[i][ls.wd()[0]] ][ke_])
                    dic[ lst[i][ls.wd()[0]] ][ke_] = int(lst[i][ke_]) if ke_ not in dic[ lst[i][ls.wd()[0]] ].keys() else int(dic[ lst[i][ls.wd()[0]] ][ke_]) +  int(lst[i][ke_])
        
        dict_sorted = cum.fmat(dic)
        cum.scll(dict_sorted)
    def fmat(dic):    #format    
        key_val={}
        for i,key in enumerate( dic.keys() ):   
            key_val.setdefault( key ,{})
            for ii in range(len( ls.nw() )):                
                for iii in range(len(ls.nw()[ii])):
                    if ls.nw()[ii][iii] in dic[key].keys():
                        ##print(key, ls.nw()[ii][iii],dic[key][ls.nw()[ii][iii]] )
                        key_val[key].setdefault(  ls.nw()[ii][iii]  ,dic[key][ls.nw()[ii][iii]])
                        
        return key_val
    def scll(dic): #
        sub =tk.Toplevel()
        sub.title("【累計】")
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame = tk.Frame(sub)        
        fram = tk.Frame(frame)
        keY =[]
        valuE=[]
        multi =[] #multidimensional:多次元
        for i,key in enumerate( dic.keys()  ):
            keY.append( key  )
            valuE.append(dic[key] )
            multi.append(key + re.sub("'|{|}", ' ',str( dic[key] )) )
            #multi.append( key + ' : ' + re.sub("dict_items(|)|([(|)])|'|,", '',re.sub(" '", ':',str(dic[key].items()) )) )

        scrollbarx = tk.Scrollbar(fram)
        scrollbarx.pack(side="bottom",fill="x")        
        scrollbary = tk.Scrollbar(fram)
        scrollbary.pack(side="right",fill="y")
        var = tk.StringVar(value = multi)
        listbox = tk.Listbox(fram,listvariable=var,width=80)
        listbox.config(xscrollcommand=scrollbarx.set)
        listbox.config(yscrollcommand=scrollbary.set)
        listbox.pack(fill="x")        
        listbox.bind("<<ListboxSelect>>", lambda event:cum.cfm(keY[listbox.curselection()[0]],valuE[ listbox.curselection()[0]] ,sub) )
        scrollbarx.config(orient=tk.HORIZONTAL,command=listbox.xview)      
        scrollbary.config(orient=tk.VERTICAL,command=listbox.yview)   
        fram.pack(padx=3)
        frame.pack(padx=2)
        tk.Button(sub,command=sub.destroy,text='戻る',relief="groove",bd=4).pack(padx=1,pady=1)
        sub.mainloop() 
          

    def cfm(ke,dic,ee_):  #confirm:確認
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        for k, v in dic.items():
            print(k, v)
        sub = tk.Toplevel(ee_) 
        sub.title("【部数】")
        ww = sub.winfo_screenwidth()
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()
        frame = tk.LabelFrame(sub)
        tk.Label(frame,text= str(ke) + "\n" + str(dic)   ).pack(side="left")
        frame.pack(padx=2,pady=1)

class table(ls.sp): #部数    
    def post():
        lst = ls.customer()
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        keylst =  ls.tm()+ls.kl()[4:]
        dic={}
        for i in range(len(lst)):
            for n,key in enumerate( lst[i].keys() ): 
                if key not in keylst :
                    dic.setdefault( i ,{})
                    dic[ i ].setdefault(key, lst[i][key])
        table.scll(dic)
    def scll(dic): #
        sub = tk.Toplevel()
        sub.title("【部数】")
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame = tk.Frame(sub)        
        fram=tk.Frame(frame)
        keY =[]
        valuE=[]
        multi =[] #multidimensional:多次元
        for i,key in enumerate( dic.keys()  ):
            keY.append( key  )
            valuE.append(dic[key] )
            #multi.append(str(key) + '' + re.sub("dict_items(|)|([(|)])|'|,", '',re.sub(" '", ':',str(dic[key].items()) )) )
            multi.append(str(key) + '' + re.sub("'|{|}", ' ',str( dic[key] )) )
        scrollbarx = tk.Scrollbar(fram)
        scrollbarx.pack(side="bottom",fill="x")        
        scrollbary = tk.Scrollbar(fram)
        scrollbary.pack(side="right",fill="y")
        var = tk.StringVar(value = multi)
        listbox = tk.Listbox(fram,listvariable=var,width=80)
        listbox.config(xscrollcommand=scrollbarx.set)
        listbox.config(yscrollcommand=scrollbary.set)
        listbox.pack(fill="x")
        listbox.bind("<<ListboxSelect>>", lambda event:table( keY[listbox.curselection()[0]],valuE[listbox.curselection()[0]],0,0,sub ).cfm())      
        #print( keY[listbox.curselection()[0]],valuE[listbox.curselection()[0]])
        scrollbarx.config( orient=tk.HORIZONTAL ,command=listbox.xview)      
        scrollbary.config( orient=tk.VERTICAL   ,command=listbox.yview)   
        fram.pack(padx=3)
        frame.pack(padx=2)
        tk.Button(sub ,command=sub.destroy ,text='戻る' ,relief="groove" ,bd=4).pack( padx=1 ,pady=1)
        sub.mainloop() 
        
    def cfm(self):  #confirm:確認
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        sub = tk.Toplevel(ee_) 
        sub.title( lst[aa_][ls.wd()[1]] )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        frame = tk.LabelFrame(sub,text='下記の契約を編集しますか？')
        label0= tk.Label(frame,text= ls.wd()[0] + ': ' + bb_[ls.wd()[0]] + "\n" +  ls.wd()[1] + ': ' + bb_[ls.wd()[1]] + "\n" )
        label0.pack(side="left")
        #####
        ##tk.Button(frame, text= "次へ",relief="groove",command=lambda:call.call(aa_,0,0,0,ee_).post() ).pack(anchor="e")
        tk.Button(frame, text= "次へ",relief="groove",command=lambda:table(aa_,0,0,0,ee_).ll() ).pack(anchor="e")
        #####
        frame.pack(padx=2,pady=1)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        
    def ll(self,*args):          
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #  
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        ext.save( ls.dl()[5] ,True ) #relord       
        ext.save( ls.dl()[3] ,aa_ )
        ext.save( ls.dl()[4] ,aa_+1   ) 
        ee_.destroy() 
        #pass

    def store(self,*args):  
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #  
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()  
        start = aa_ 
        ext.save( ls.dl()[3] ,start    )
        ext.save( ls.dl()[4] ,start + 1)
        
        sub = tk.Toplevel(ee_)  
        sub.title( lst[aa_][ls.wd()[1]] )  
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge( ww,wh) )         
        frame = tk.Frame( sub)
        label0= tk.Label( frame,text ="一旦閉じます。再起動してください。")
        label0.pack(side="top",padx=2,pady=5)
        button0= tk.Button( frame ,text='OK' ,command =lambda: ee_.destroy())
        button0.pack(side="top",padx=2,pady=1) 
        frame.pack()

if __name__ == '__main__':
    cum.post()
    #table.post()