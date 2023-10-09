import os.path #infix:挿入
import tkinter as tk
import notice
import optionmenu
from collections import defaultdict
import ls
import sys
import ext

class cmp(ls.sp):#compilation:編集
    def divi(self):         
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #    
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        wdgt.forget( ee_)
        sub = ee_ 
        sub.title( bb_ )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )        
        lst = cc_
        fram_ = tk.LabelFrame(sub, text = '編集')
        txt4 = tk.StringVar(sub)
        txt4.set('カテゴリ')
        opt4 = tk.OptionMenu(fram_, txt4,*ls.pa(),command=lambda event:optionmenu.option(opt4,opt5,txt4,txt5,sub).division())
        opt4.pack(side="left")
        txt5 = tk.StringVar(sub)
        txt5.set(lst[0][bb_])
        opt5=tk.OptionMenu(fram_,txt5,*ls.ea()[0],*ls.ea()[1])
        opt5.config(relief=tk.GROOVE)
        opt5.pack(side="left")        
        btn= tk.Button(fram_, command=lambda :infix(aa_, bb_, cmp.val_sum( bb_, cc_, txt5.get()), None, ee_).post(),text='次へ',relief="groove",bd=4)
        btn.bind('<Return>',lambda event:infix(aa_, bb_, cmp.val_sum( bb_, cc_, txt5.get()), None, ee_).post() )
        btn.pack()         
        fram_.pack(padx=1,pady=1)
        cansell = tk.Button(sub, text="キャンセル" , command =lambda : infix(aa_, bb_, cc_, None, ee_).post() )
        cansell.bind('<Return>', lambda event:infix(aa_, bb_, cc_, None, ee_).post() )
        cansell.pack(padx=4, pady=4)   
        
    def txst(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #   
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        wdgt.forget( ee_)
        sub = ee_ 
        lst = cc_
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh))
        fram_ = tk.Frame( sub)
        tk.Label( fram_,text=bb_,width=6).pack(side="left")  
        validate = sub.register( ext.elim)
        entry_val = tk.StringVar()
        enter0= tk.Entry(fram_, validate="key", validatecommand = (validate, "%P"), textvariable= entry_val ,relief="groove",bd=4,width=60)
        enter0.focus_set() 
        enter0.insert('end',lst[0][bb_])
        enter0.pack(side="left",fill="x",padx=1,pady=1)                 
        btn= tk.Button(fram_,command=lambda :infix(aa_, bb_, cmp.val_sum( bb_, cc_, enter0.get()), None, ee_).post(), text='次へ',relief="groove",bd=4)
        btn.bind('<Return>',lambda event:infix(aa_, bb_, cmp.val_sum( bb_, cc_, enter0.get()), None, ee_).post() )
        btn.pack()  
        fram_.pack()
        cansell = tk.Button(sub, text="キャンセル" , command =lambda : infix(aa_, bb_, cc_, None, ee_).post() )
        cansell.bind('<Return>', lambda event:infix(aa_, bb_, cc_, None, ee_).post() )
        cansell.pack( padx=4, pady=4)
        
    def bind_select(self):  #confirm:確認
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()
        #print(aa_,bb_,cc_,dd_,ee_)
        listbox=bb_
        index = listbox.curselection()[0]
        bb_ = listbox.get(index)[0]
        #print(listbox.get(index)[0],listbox.get(index)[1], list({listbox.get(index)[0]:listbox.get(index)[1]}.keys())[0])
        lst = cc_
        agrm = { ky : lst[0][ky] for ky in lst[0]  if ky not in ls.kl()}   #契約:Agreement     
        wdgt.forget( ee_)   
        sub = ee_ 
        sub.title(None)
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        fram_ = tk.LabelFrame(sub, text = '挿入')
        cmp.front_insert(aa_,bb_,cc_,dd_,ee_,sub,fram_,lst)
        fram_.pack(padx=1,pady=1) 
        fram_ = tk.LabelFrame(sub, text = '編集')
        cmp.edit(aa_,bb_,cc_,dd_,ee_,sub,fram_,lst)
        fram_.pack(padx=1,pady=1)
   
        fram_ = tk.LabelFrame(sub, text = '末尾に挿入')
        cmp.end_insert(aa_,bb_,cc_,dd_,ee_,sub,fram_,lst)
        fram_.pack(padx=1,pady=1)
        if len(agrm) > 1 :            
            fram_ = tk.LabelFrame(sub, text = '削除')
            cmp.delete(aa_,bb_,cc_,dd_,ee_,sub,fram_,lst)
            fram_.pack( )         
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack(pady=4)        
        
    def val_sum(bb_, cc_, obj):
        key = bb_
        lst = cc_
        val = obj ##object:(知覚できる)物、物体、対象、
        lst[0][key] = val
        return lst
    def lst_sum0(fnc, bb_, txt, cc_, spn):
        exis = bb_#既存:existing
        key = txt
        lst = cc_
        val = spn         
        inx = list(lst[0]).index(exis)
        rvers = list(lst[0])
        rvers.reverse()###元のリスト自体が書き換えられる破壊的処理。返り値はNoneなので注意。
        front = { ky:lst[0][ky] for ky in list(lst[0])[:inx]}       
        backs = { ky:lst[0][ky] for ky in reversed(rvers[:rvers.index(exis)])}
        if fnc == "front_insert":
            lst = [{**front,**{key:val},**{exis:lst[0][exis]},**backs,**{key:val}}]
        elif fnc == "edit":
            lst = [{**front,**{key:val},**backs}]
        elif fnc =="end_insert":
            lst = [{**front,**{exis:lst[0][exis]},**{key:val},**backs,**{key:val}}]
        elif fnc =="delete":
            lst = [{**front,**backs}]        
        return lst        

    def front_insert(aa_,bb_,cc_,dd_,ee_,sub,fram_,lst):
        fnc = sys._getframe().f_code.co_name
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,txt0,txt1,sub).select())
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set("")
        opt1=tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[2],*ls.nw()[3],*ls.nw()[4],*ls.nw()[5],*ls.nw()[12],*ls.nw()[15])    
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")                
        val = tk.IntVar(sub)
        spn = tk.Spinbox(fram_, textvariable=val, width=3, from_=1, to=999, state = 'readonly' )        
        spn.pack(side="left", padx=2 ,pady=2)
        tk.Label(fram_,text='部').pack(side="left")
        tk.Button(fram_,text='実行',width=4,command=lambda :infix(aa_,bb_,cmp.lst_sum0(fnc, bb_, txt1.get(), cc_, spn.get()),None,ee_).post() if txt1.get() != "" else tk.Label(sub,text='未入力の箇所があります' ).pack(),relief="groove",bd=4).pack(side="top",padx=1,pady=1)     

    def edit(aa_,bb_,cc_,dd_,ee_,sub,fram_,lst):
        fnc = sys._getframe().f_code.co_name
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,txt0,txt1,sub).select())
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set(bb_)
        opt1=tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[2],*ls.nw()[3],*ls.nw()[4],*ls.nw()[5],*ls.nw()[12],*ls.nw()[15])    
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")                
        val = tk.IntVar(sub)
        val.set(int(lst[0][bb_]))
        spn = tk.Spinbox(fram_, textvariable=val, width=3, from_=0, to=999, state = 'readonly')        
        spn.pack(side="left", padx=2 ,pady=2)      
        tk.Label(fram_,text='部').pack(side="left") 
        tk.Button(fram_,text='実行',command=lambda :infix(aa_,bb_,cmp.lst_sum0(fnc, bb_, txt1.get(), cc_, spn.get()),None,ee_).post(),relief="groove",bd=4).pack(side="top",padx=1,pady=1)

    def end_insert(aa_,bb_,cc_,dd_,ee_,sub,fram_,lst):
        fnc = sys._getframe().f_code.co_name
        txt0 = tk.StringVar(sub)
        txt0.set('カテゴリ')
        opt0 = tk.OptionMenu(fram_, txt0,*ls.mn(),command=lambda event:optionmenu.option(opt0,opt1,txt0,txt1,sub).select())
        opt0.pack(side="left")
        txt1 = tk.StringVar(sub)
        txt1.set("")
        opt1=tk.OptionMenu(fram_,txt1,*ls.nw()[0],*ls.nw()[1],*ls.nw()[2],*ls.nw()[3],*ls.nw()[4],*ls.nw()[5],*ls.nw()[12],*ls.nw()[15])    
        opt1.config(relief=tk.GROOVE)
        opt1.pack(side="left")                
        val = tk.IntVar(sub)
        spn = tk.Spinbox(fram_, textvariable=val, width=3, from_=1, to=999, state = 'readonly' )        
        spn.pack(side="left", padx=2 ,pady=2)        
        tk.Label(fram_,text='部').pack(side="left") 
        tk.Button(fram_,text='実行',width=4,command=lambda :infix(aa_,bb_,cmp.lst_sum0(fnc, bb_, txt1.get(), cc_, spn.get()),None,ee_).post() if txt1.get() != "" else tk.Label(sub,text='未入力の箇所があります' ).pack(),relief="groove",bd=4).pack(side="top",padx=1,pady=1)     
        #:infix(aa_, bb_, cmp.lst_sum( bb_, cc_, enter0.get()), 0, ee_).post()
    def delete(aa_,bb_,cc_,dd_,ee_,sub,fram_,lst):
        fnc = sys._getframe().f_code.co_name
        tk.Label(fram_,text=bb_).pack(side="left",padx=10)
        tk.Label(fram_,text=lst[0][bb_]).pack(side="left")
        tk.Label(fram_,text='部').pack(side="left") 
        tk.Button(fram_,command=lambda :infix(aa_,bb_,cmp.lst_sum0(fnc, bb_, None, cc_, None),0,ee_).post(), text='実行',relief="groove",bd=4).pack(side="right")       
        
class infix(ls.sp): #infix:挿入
    def __del__(self):
        pass#        print("killing me")
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
                
        if type(cc_) != list :###initial state:初期状態
            wdgt.forget(ee_)
            sub = ee_ ##tk.Toplevel()
            sub.title(None)
            ww = sub.winfo_screenwidth() 
            wh = sub.winfo_screenheight()
            sub.geometry( ls.ge(ww,wh))
            dct = { ky : "" for ky in ls.kl() }      
            dct[ls.hb()] = sub.winfo_width() ###幅  
            dct[ls.kp()] = '無効' ###改ページ
            dct[ls.nw()[0][3]] = '1' ###'': '1'
            lst = [dct]
        elif type(cc_) == list:
            wdgt.forget(ee_)
            lst = cc_
            sub = ee_
        { ky : lst[0][ky] for ky in lst[0]  if ky not in ls.kl()}
        
        frame = tk.Frame(sub)
        rig_t = tk.LabelFrame(frame, text="プレビュー")  
        infix.preview(rig_t, lst)
        rig_t.pack(side="right",padx=10,pady=1)   

        left = tk.Frame(frame) 
        f_ame = tk.LabelFrame(left, text="挿入する顧客情報を入力して下さい", labelanchor="n")
        fram_ = tk.Frame(f_ame)                
        fra__ = tk.LabelFrame(fram_, text="必須", fg="gray", borderwidth=4)
        fra__.pack() 
        fra_e = tk.LabelFrame(fram_)
        fra_e.pack() 
        
        for i,ke_ in enumerate(lst[0]):
            if ke_ in [ ls.kb()] :###区分
                fr___ = tk.Frame( fra__)                
                btn = tk.Button( fr___,text=ke_, relief="raised")
                btn.bind('<1>', lambda event:cmp( aa_,event.widget["text"],lst,None,sub).divi())
                btn.bind('<Return>', lambda event:cmp( aa_,event.widget["text"],lst,None,sub).divi())
                btn.pack(side="left")
                lbl = tk.Label( fr___, width= 11, text= lst[0][ke_], anchor= 'w', relief="groove" )
                lbl.pack(side="left")
                fr___.pack(side="top")
                pack_pad.post(btn,lbl)
            elif ke_ in [ ls.mi()]:###名称１
                fr___ = tk.Frame(fra__)                
                btn = tk.Button(fr___,text=ke_, relief="raised")
                btn.bind('<1>', lambda event:cmp(aa_,event.widget["text"],lst,None,sub).txst())
                btn.bind('<Return>', lambda event:cmp(aa_,event.widget["text"],lst,None,sub).txst())
                btn.pack(side="left",ipadx=1,padx=1, ipady=1, pady=1)
                lbl = tk.Label(fr___, width= 11, text= lst[0][ke_], anchor= 'w', relief= "groove")
                lbl.pack(side="left")
                fr___.pack(side="top")
                pack_pad.post(btn,lbl)

            elif ke_ in [ ls.gs()] + ls.mm()[1:]:
                fr___ = tk.Frame(fra_e)
                btn = tk.Button(fr___,text=ke_, relief="raised",fg=ls.cl()[3] if ke_== ls.mm()[2] or ke_== ls.mm()[4] else ls.cl()[0] )
                btn.bind('<1>', lambda event:cmp(aa_,event.widget["text"],lst,None,sub).txst())
                btn.bind('<Return>', lambda event:cmp(aa_,event.widget["text"],lst,None,sub).txst())
                btn.pack(side="left",ipadx=1,padx=1,ipady=1,pady=1)
                lbl = tk.Label(fr___, width= 11, text= lst[0][ke_], anchor= 'w', relief="groove")
                lbl.pack(side="left")
                val = tk.StringVar()           
                enr = tk.Entry(fr___, width= 11,textvariable= val)
                enr.insert(0,lst[0][ke_]) 
                enr.pack_forget
                fr___.pack()
                pack_pad.post(btn,lbl)
                
        fram_.pack(side="right")
        fram_ = tk.LabelFrame(f_ame,text="必須",fg="gray", borderwidth=4)
        scrollbar = tk.Scrollbar(fram_)
        scrollbar.pack(side="right",fill="y")
        var = tk.StringVar()
        listbox = tk.Listbox(fram_,listvariable=var,heigh=10,width=11,font=9)
        listbox.config(yscrollcommand=scrollbar.set)
        for i, ke_ in enumerate(lst[0]):
            if not ke_ in ls.kl():      
                listbox.insert(tk.END, [ ke_,lst[0][ke_ ] ])
        listbox.pack()
        listbox.bind("<<ListboxSelect>>", lambda event:cmp(aa_, listbox, lst, None, sub).bind_select() )
        scrollbar.config( command=listbox.yview)        
        fram_.pack(side="right")
        f_ame.pack()        
        left.pack()
        pack_pad.post(f_ame,fram_,fr___,f_ame,fra__,fra_e)
        
        fram_ = tk.Frame(frame)
        tk.Button(fram_, text="挿入", command = lambda:infix(aa_, None, lst, None, ee_).save() if infix.req(lst) else infix.alr(fram_,lst), borderwidth=4).pack( side="left", padx=4, pady=4) #anchor="e"
        cansell = tk.Button(fram_, text="キャンセル" , command = sub.destroy )
        cansell.focus_set() 
        cansell.bind('<Return>', lambda event:sub.destroy() )
        cansell.pack(side="left", padx=4, pady=4)
        fram_.pack(side="bottom", padx=4)        
        frame.pack()
        sub.mainloop()      
        
    def preview(rig_t,lst):###試演、試写
        up___ = tk.Frame(rig_t)
        fram_ = tk.Frame(up___)
        wr = ext.cnv_list( lst[0].get(ls.mm()[1]))##メモ１     
        for item in wr:
            tk.Label(fram_,text=ext.tategaki( item),bd=1,bg=ls.cl()[1]).pack(side="right")
        wr = ext.cnv_list( lst[0].get(ls.mm()[2]))##メモ2     
        for item in wr:
            tk.Label(fram_,text=ext.tategaki( item),bd=1,fg=ls.cl()[3],bg=ls.cl()[1]).pack(side="right")
        fram_.pack(side="right")  
        
        fram_ = tk.Frame(up___)
        fra__ = tk.Frame(fram_)##新聞名
        for w in lst[0].keys():
            if w not in ls.kl():#ls.tm() + ls.m2() + ls.ic()
                tk.Label(fra__, width=2, text=ext.gomoji(w), fg=ext.font_clr(lst[0], w), bg= ext.clr(w)).pack(padx=0,pady=0,side="right")
        fra__.pack()
        fra__ = tk.Frame(fram_)##部数  
        for  w in lst[0].keys():  
            if w not in ls.kl():
                tk.Label(fra__, width=2, text = ext.ichi(lst[0].get(w)) ,relief= ext.relieF(w),fg=ls.cl()[0] ,bg=ls.cl()[1] ).pack(side="right")
        fra__.pack() 
        
        fra__ = tk.LabelFrame(fram_)         
        tk.Label(fra__, text= lst[0].get(ls.gs()), bg=ls.cl()[1]).pack(padx=0,pady=0)#, font=("",ls.ft()[2])  
        tk.Label(fra__, text= ext.tategaki(lst[0].get(ls.mi())[:5]), relief ="flat",bg=ls.cl()[1], height=5).pack(padx=0,pady=0,side="right")##名称1  
        fra__.pack()        
        fram_.pack(side="right",pady=1)           
        
        fram_ = tk.Frame(up___)
        wr = ext.cnv_list( lst[0].get(ls.mm()[3]))##メモ2    
        for item in wr:
            tk.Label(fram_,text=ext.tategaki( item ), bd=1,bg=ls.cl()[1]).pack(side="right")
        wr = ext.cnv_list( lst[0].get(ls.mm()[4]))##メモ3     
        for item in wr:
            tk.Label(fram_,text=ext.tategaki( item ), bd=1,fg=ls.cl()[3],bg=ls.cl()[1]).pack(side="right")
        fram_.pack(side="right")  
        up___.pack(side="top")
        und_r = tk.Frame(rig_t)        
        fram_ = tk.Frame(und_r)
        tk.Button(rig_t,font=("",7)).pack( fill=tk.X)
        fram_.pack()  
        und_r.pack(side="top")
        
    def save(self):         
        aa_ = self.a #
        bb_ = self.b #entries
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.customer()        
        lst.insert( aa_, cc_[0])
        ext.store("customer.txt" ,lst)
        ins = notice.save("","","",0,ee_)
        ins.complete()                           
        
    def req(lst):###required:必須
        if lst[0][ls.kb()] == "":###区分
            return False#True#
        elif lst[0][ls.mi()] == "":###名称1
            return False#True#
        else:
            return True
    def alr(frame,lst):###alert  
        if lst[0][ls.kb()] == "":###区分
            return tk.Label(frame, text = ls.kb() + 'が未入力です', bg='yellow').pack()
        elif lst[0][ls.mi()] == "":###名称1
            return tk.Label(frame, text = ls.mi() + 'が未入力です', bg='yellow').pack()
        else:
            return None
        
    def test(self):  #confirm:確認
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def()
        dct = defaultdict( int)
        dct[aa_] += 88
        dct[aa_] += 12
        dct
        
class wdgt:#widget                       
    def forget(root):
        children = root.winfo_children() #print(children)     #print(children,len(children),type(children))
        for child in children:
            child.destroy() 
class pack_pad:### 設定の追加
    def post(*args):  
        type(args)
        for a in args:
            a.pack_configure(ipadx=2,padx=2,ipady=1)
    def child():
        return #ipadx=1,padx=1,ipady=1,pady=1
        
if __name__ == '__main__': ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    infix(0,None,None,None,root).post()
    
