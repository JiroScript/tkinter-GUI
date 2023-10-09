import os.path
import tkinter as tk
import notice
import ls
import sys
import ext

class trns(ls.sp): #transfer：移動する
    def titl():  
        return '顧客情報の移動'
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #  
        cc_ = self.c #
        dd_ = self.d #
        ee_ = self.e #        
        ls.sp( aa_ ,bb_ ,cc_ ,dd_ ,ee_).pasS()
        root = ee_ 
        root.title( trns.titl() )
        root.option_add( '*font', 'Meiryo' + ls.ft()[1])##YuGothic
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
         
        lst = ls.customer()
        fram_ = tk.LabelFrame(root,text='顧客情報を移動する') 
        fra__ = tk.Frame(fram_) 
        fr___ =  tk.Frame(fra__) 
        tk.Label(fr___, text="顧客番号").pack(side="left")
        validate = root.register(ext.validate_input)
        enr5_val = tk.StringVar()
        enr5_val.trace("w" ,lambda uno,duo,tres:lBL1.configure( text = ext.list_index( enr5_val.get() ,lst) ))
        enr5 = tk.Entry(fr___ ,validate="key", validatecommand = (validate, "%P"), textvariable= enr5_val ,width=4)
        enr5.pack(side="left" ,padx=3 ,pady=10)  
        tk.Label(fr___ ,text="番").pack(side="left") 
        fr___ .pack(side="top")  
        lBL1 = tk.Label(fra__ )
        lBL1.pack(side="bottom",padx=1 ,pady=20)
        fra__.pack(side="left" )
        ###########
        fra__ = tk.Frame(fram_)       
        vr = tk.IntVar() 
        vr.set(0)
        f____=tk.Frame(fra__)  
        rdo1 = tk.Radiobutton(f____ ,value=0 ,command=lambda: ext.active(enr6,label), variable=vr, text= "から")  
        rdo1.pack(padx=2 ,pady=5)
        rdo2 = tk.Radiobutton(f____ ,value=1 ,command=lambda: ext.hide(enr6,enr6_val,label,lBL2), variable=vr, text= "のみ")
        rdo2.pack(padx=2 ,pady=5)
        tk.Label(f____ ).pack(padx=1 ,pady=20)
        f____.pack()
        fra__.pack(side="left" )
        ###########
        fra__ = tk.Frame(fram_)
        fr___ =  tk.Frame(fra__) 
        validate = root.register(ext.validate_input)  
        enr6_val = tk.StringVar()
        enr6_val.trace("w" ,lambda uno,duo,tres:lBL2.configure( text = ext.list_index( enr6_val.get() ,lst) ))
        enr6 = tk.Entry(fr___, validate="key" ,validatecommand =(validate, "%P") ,textvariable =enr6_val ,width=4)
        enr6.pack(side="left" , padx=3 ,pady=10)
        label =tk.Label(fr___ ,text="番を")
        label.pack(side="left")   
        fr___ .pack(side="top")  
        lBL2 = tk.Label(fra__ )
        lBL2.pack(side="bottom",padx=1 ,pady=20)  
        fra__.pack(side="left")   
         
        fra__ = tk.Frame(fram_) 
        vAR = tk.IntVar() 
        vAR.set(0)  
        f____=tk.Frame(fra__)  
        rdo3 = tk.Radiobutton(f____ ,value=0 ,command=lambda: ext.active(enr1,labeL) ,variable=vAR)
        rdo3.pack(padx=2 ,pady=5)   
        rdo4 = tk.Radiobutton(f____ ,value=1 ,command=lambda: ext.hide(enr1,enr1_val,labeL,lBL3) ,variable=vAR, text= "")
        rdo4.pack(padx=2 ,pady=5) 
        tk.Label(f____ ).pack(padx=1 ,pady=20)      
        f____.pack()         
        fra__.pack(side="left")    
        
        fra__ = tk.Frame(fram_) 
        fr___ =  tk.Frame(fra__) 
        f____=tk.Frame(fr___) 
        validate = root.register(ext.validate_input)
        enr1_val = tk.StringVar()       
        enr1_val.trace("w" ,lambda uno,duo,tres:lBL3.configure( text = ext.list_index( enr1_val.get() ,lst) ))
        enr1 = tk.Entry(f____ ,validate="key" ,validatecommand=(validate, "%P") ,textvariable =enr1_val ,width=4)
        enr1.pack(side="left" ,padx=1 ,pady=2)  
        labeL =tk.Label(f____ ,text='番の前に移動する。')
        labeL.pack(side="left",padx=2 ,pady=5) 
        f____.pack(side="top")   
        #####        
        f____=tk.Frame(fr___) 
        tk.Label(f____,text='末尾に移動する。').pack(side="left",padx=2 ,pady=5) 
        f____.pack(side="bottom")
        fr___ .pack(side="top")  
        lBL3 = tk.Label(fra__ )
        lBL3.pack(side="bottom",padx=1 ,pady=20)
        fra__.pack(side="left")   
        #####          
        fram_.pack( padx=5 ,pady=10)
        
        button0= tk.Button(root ,command = lambda :trns(aa_ ,enr5.get() ,enr6.get() if vr.get()== 0 else enr5.get() ,enr1.get() if vAR.get()== 0 else str(len(lst)-1) ,ee_).check() ,text='次へ',relief="groove",bd=4)
        button0.pack() #anchor="e"
        cansell = tk.Button(root ,text="キャンセル" ,command =root.destroy ,relief="groove" ,bd=4 ,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>' ,lambda event:root.destroy())
        cansell.pack()  
        root.mainloop()      
                
    def check(self):  #入力された値をチェック
        aa_ = self.a
        bb_ = self.b    
        cc_ = self.c
        dd_ = self.d  
        ee_ = self.e        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        print(aa_,bb_,cc_,dd_,ee_)
        lst = ls.customer()
        print(len(lst))
        if bb_ == "" or cc_ == "" or dd_ == "" :
            ext.warning(trns.titl(),'未入力の箇所があります' ,ee_)
        elif bb_ != "" and cc_ != "" and dd_ != "" :
            bbb = int( bb_)
            ccc = int( cc_)
            ddd = int( dd_)
            
            if  bbb > ccc :# 
                ext.warning(trns.titl(),"入力した数字に不正があります" ,ee_)
            elif bbb <= ddd and ccc >= ddd:
                ext.warning(trns.titl(),"入力した数字に不正があります" ,ee_)
            elif ccc >= len(lst) :
                ext.warning(trns.titl(),"入力した数字に不正があります" ,ee_)
            elif ddd > len(lst) :
                ext.warning(trns.titl(),"入力した値に顧客情報の総数\nを超えている箇所があります" ,ee_)
            else:
                trns(aa_, bb_  ,cc_ ,dd_ ,ee_).cfm()            
        
    def cfm(self):  #confirm:確認
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        sub = tk.Toplevel(ee_) 
        sub.title( trns.titl() )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        lst = ls.customer()
        bbb = int( bb_)
        ccc = int( cc_)
        ddd = int( dd_)
        
        frame = tk.LabelFrame(sub,text='')
        tk.Label(frame ,text = bb_ + '番「' + lst[ bbb][ ls.wd()[1]] + '」').pack()
        tk.Label(frame ,text = 'から' if bb_ !=cc_ else 'のみ').pack() 
        tk.Label(frame ,text = cc_ + '番「' + lst[ ccc][ ls.wd()[1]] + '」').pack() if bbb !=ccc else None
        tk.Label(frame ,text = 'までを' if bb_ !=cc_ else '').pack()
        tk.Label(frame ,text = dd_ + '番「' + lst[ ddd][ ls.wd()[1]] + '」').pack()
        tk.Label(frame ,text = 'の前に移動する' if ddd !=len(lst)-1 else 'の末尾に移動する').pack()
        button0= tk.Button(frame ,command=lambda :trns(aa_,bb_,cc_,dd_,ee_).save() ,text='実行' ,relief="groove" ,bd=4)
        button0.pack(pady=5)#anchor="e"
        frame.pack(padx=2,pady=1)
        fram_ = tk.Frame(sub)        
        cansell = tk.Button(sub ,text="キャンセル" ,command = sub.destroy ,relief="groove" ,bd=4 ,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>' ,lambda event:sub.destroy())
        cansell.pack()          
        fram_.pack()
        
    def save(self):         
        aa_ = self.a #
        bb_ = self.b #
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.customer()
        bb_ = int(bb_)
        cc_ = int(cc_)
        dd_ = int(dd_)
        
        tub = []    
        front = lst[:dd_]
        back  = lst[dd_:]
        for i in range( bb_ ,cc_+1):
            print(i)
            if bb_ > dd_:
                tub.append( back.pop( bb_-len(front)))
            elif bb_ < dd_:
                tub.append( front.pop( bb_))
        if dd_ != len(lst)-1:
            lst = front + tub + back
        elif dd_ == len(lst)-1:
            lst = front + back + tub
        ext.store("customer.txt" ,lst)
        print(tub ,"\n")
        for i in range( len(lst) ):
            print(lst[i]["名称1"] ,"\n")
        for item in front:
            print(item["名称1"] ,"\n")
        for item in back:
            print(item["名称1"] ,"\n")
        ins = notice.save("","","",0,ee_)
        ins.complete()   
        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    ww = root.winfo_screenwidth() 
    wh = root.winfo_screenheight()
    root.geometry( ls.ge(ww,wh) )    
    trns(0,6,7,1,root).post()
    #root.mainloop()
    