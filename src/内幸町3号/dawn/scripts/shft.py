import os.path #shift:当番
from collections import Counter
import tkinter as tk 
import optionmenu
import notice
import ls
import re
import sys

def validate_input(val):
    fmt = '^[0-9]{,1}[0-9]{,1}?$'#'^[+-]?[0-9]{1,2}(?:\.[0-9]{,2})?$'
    if val=='' or re.match(fmt, val):
        return True
    return False        
def no_entered(sub):
    tk.Label(sub,text='未入力の箇所があります' ).pack()

class dsp(ls.sp):#display:表示・陳列       
    def uno(self):   
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #  
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        lst = ls.sheet()  
        year ="{:02d}".format(bb_)
        month ="{:02d}".format(cc_)
        day ="{:02d}".format(dd_)
        um =str(self.d)
        clr = year + month + day
        for i in range(len(lst)):
            if clr ==  lst[i]['日時']:
                ##print(i,clr,lst[i]['作業者'])
                um += "\n"+lst[i]['作業者'] +":"+lst[i]['区分']
                
            elif clr !=lst[i]['日時']:
                pass
                #print(um)
        return um
    
class cum: #Cumulative:累計
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def post(self):   
        self.year = self.a
        self.month = self.b
        year  = "{:02d}".format(self.year)
        month = "{:02d}".format(self.month)
        lst = ls.sheet()  
        li=[]
        ll=[]
        lll=[]
        for i,item in enumerate(lst):
            YM = year + month
            if YM in item[ls.sh()[0]][:len(YM)]:
                li.append( {item[ls.sh()[2]]:item[ls.sh()[1]]} )
                ll.append(item[ls.sh()[2]])
            #li.append( {item['作業者']:item['区分']})
        ##print( set(ll))
        lse = set(ll)#重複を削除
        for nme in lse:
            
            ln = [d.get(nme) for d in li if d.get(nme)]
            li_dic = list(Counter(ln).items())
            tp=''.join(map(str,li_dic))
            tp=tp.replace("'","")
            lll.append(nme)
            lll.append(tp)
            lll.append("\n")
        return "".join(lll)
    
    
class eny(ls.sp):#entry:登録      
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #    
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        sub = tk.Toplevel( ee_ ) 
        sub.title("")
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        pnt = dd_.find("\n") if "\n" in dd_ else None
        dd_ = int(dd_[:pnt])
        year  = "{:02d}".format(bb_)
        month = "{:02d}".format(cc_)
        day   = "{:02d}".format(dd_)
        fram_ = tk.LabelFrame(sub, text = '登録')
        tk.Label(fram_,text=ls.sh()[0] + ':' ).pack(side="left")
        tk.Label(fram_,text= year + month + day).pack(side="left")
        txt4 = tk.StringVar(sub)
        txt4.set('カテゴリ')
        opt4 = tk.OptionMenu(fram_, txt4,*ls.pa(),command=lambda event:optionmenu.option(opt4,opt5,txt4,txt5,sub).division())
        opt4.pack(side="left")
        txt5 = tk.StringVar(sub)
        txt5.set(ls.sh()[1])
        opt5=tk.OptionMenu(fram_,txt5,*ls.ea()[0],*ls.ea()[1])
        opt5.config(relief=tk.GROOVE)
        opt5.pack(side="left")     
        
        txt6 = tk.StringVar(sub)
        txt6.set(ls.sh()[2])
        opt6=tk.OptionMenu(fram_,txt6,*ls.hu()[0],*ls.hu()[1])
        opt6.config(relief=tk.GROOVE)
        opt6.pack(side="left")   
        button2= tk.Button(fram_,text='次へ',command=lambda :cfm(aa_,year+month+day,txt5.get(),txt6.get() ,ee_).compil() if txt5.get() != ls.sh()[1] and txt6.get() != ls.sh()[2] else no_entered(sub) ,relief="groove",bd=4)
        button2.pack(side="top",padx=1,pady=1)        
        fram_.pack(padx=1,pady=1)        
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()
        dlt(aa_,bb_,cc_,dd_,sub).post()
class cfm(ls.sp):#confirm:確認
    def compil(self):  #編集 
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #    
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        sub = tk.Toplevel( ee_ ) 
        sub.title( bb_ )
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame = tk.LabelFrame(sub,text='下記の内容で保存しますか？')
        tk.Label(frame,text=ls.sh()[0] + ':' + bb_ + ' '  + ls.sh()[1] + ':'  + cc_ + ' ' + ls.sh()[2] + ':' + dd_).pack(side="left",padx=15)
        button0= tk.Button(frame,command=lambda :cfm(aa_,bb_,cc_,dd_,ee_).save(),text='実行',relief="groove",bd=4)
        button0.pack(side="left",anchor="e") 
        frame.pack(padx=2,pady=1)
        frame_ = tk.Frame(sub)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()           
        frame_.pack()
        
    def save(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
       
        lst = ls.sheet()
        text = str(lst).replace(" ","")
        lis =[bb_,cc_,dd_]
        dct={}             
        for i, item in enumerate(ls.sh()):
            dct[ item ] = lis[i] 
        lst.insert(0,dct)
        print(lst)
        tex_=text.replace(text,str(lst).replace(" ", "") ,1)
        ls.store("sheet.txt" ,tex_)
        
        ins = notice.save(0,0,0,0,ee_)
        ins.complete()    
        

class dlt(ls.sp):#delete
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #    
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        
        year  = "{:02d}".format(bb_)
        month = "{:02d}".format(cc_)
        day   = "{:02d}".format(dd_)
        date = year + month + day 
        lst = ls.sheet() 
        frame = tk.LabelFrame(ee_, text = '削除')
        tk.Label(frame,text= year + month + day + '付').pack(side="top")  
        fram = tk.Frame(frame)

        scrollbar = tk.Scrollbar(fram)
        scrollbar.pack(side="right",fill="y")
        var = tk.StringVar(ee_)
        listbox = tk.Listbox(fram,listvariable=var,heigh=10)
        listbox.config(yscrollcommand=scrollbar.set)
        
        for i,item in enumerate(lst):
            if date in lst[i][ls.sh()[0]]:#日時 
                listbox.insert(tk.END, [ item[ls.sh()[1]] ,item[ls.sh()[2]]])
        listbox.pack()
        listbox.bind("<<ListboxSelect>>", lambda event:dlt.bind_selected( date ,listbox ,ee_) )
        scrollbar.config(command=listbox.yview)
        
        fram.pack(side="right",padx=2)  
        frame.pack(padx=1,pady=1)      
        cansell = tk.Button(ee_, text="キャンセル" ,command = ee_.destroy,relief="groove",bd=4,anchor="e")
        cansell.focus_set() 
        cansell.bind('<Return>',lambda event:ee_.destroy() )
        cansell.pack()
        
    def bind_selected(date,listbox,ee_):#**kwargs: 複数のキーワード引数を辞書として受け取る
        if len(listbox.curselection()) == 0:
            return
        index = listbox.curselection()[0]
        dlt(0, date ,listbox.get(index)[0] ,listbox.get(index)[1],ee_ ).cfm()
        
    def cfm(self):  #編集 
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #    
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        sub = tk.Toplevel(ee_) 
        sub.title(bb_)
        ww = sub.winfo_screenwidth() 
        wh = sub.winfo_screenheight()
        sub.geometry( ls.ge(ww,wh) )
        frame = tk.LabelFrame(sub,text='下記の内容を削除しますか？')
        tk.Label(frame,text= bb_ + ' ' + cc_ + ' ' + dd_).pack(side="left",padx=15)
        button0= tk.Button(frame,command=lambda :dlt(aa_,bb_,cc_,dd_,ee_).save(),text='実行',relief="groove",bd=4)
        button0.focus_set()
        button0.bind('<Return>',lambda event:dlt(aa_,bb_,cc_,dd_,ee_).save() )
        button0.pack(side="left",anchor="e") 
        frame.pack(padx=2,pady=1)
        frame_ = tk.Frame(sub)
        cansell = tk.Button(sub, text="キャンセル" ,command = sub.destroy,relief="groove",bd=4,anchor="e")
        cansell.bind('<Return>',lambda event:sub.destroy() )
        cansell.pack()       
        frame_.pack()
    def save(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d # 
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS() 
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
       
        lst = ls.sheet()
        text = str(lst).replace(" ","")
        
        date = bb_
        content = cc_ #Business content
        worker = dd_
        for i, item in enumerate(lst):
            if date in item[ls.sh()[0]] and content in item[ls.sh()[1]] and worker in item[ls.sh()[2]]:
                #lst.pop(i)
                lst.pop(i)
          
        tex_=text.replace(text,str(lst).replace(" ", "") ,1)
        ls.store("sheet.txt" ,tex_)
        ins = notice.save(0,0,0,0,ee_)
        ins.complete()   
        
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
    root = tk.Tk() 
    eny(0,2020,9,"20",root).post()