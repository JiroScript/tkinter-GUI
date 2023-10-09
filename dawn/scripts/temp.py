import os.path
import tkinter as tk #Junction:分岐点
import ls
import edit
import call

class cmp(ls.sp): #compilation:編集
    def post_____________(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        dic= cc_    
        wdgt.forget( ee_)
        root = ee_ 
        root.title('一時止' + '編集' + ' ' + dic.get('名称1'))
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.geometry( ls.ge(ww,wh) )
        frame = tk.Frame(root )  
        fram_ = tk.Frame(frame )  
        fram_.pack( fill="x", padx=4, pady=4)
        frame.pack() 
        
        val0 = tk.IntVar(root)
        val0.set(str(dic[ ls.tm()[0]]))
        spn0 = tk.Spinbox(fram_, textvariable=val0, width=3, from_=1,  to=12, state = 'readonly')        
        spn0.pack(side="left", padx=4 ,pady=2) 
        tk.Label(fram_,text='月' ).pack(side="left")  
        val1 = tk.IntVar(root)
        val1.set(str(dic[ ls.tm()[1]]))
        spn1 = tk.Spinbox(fram_, textvariable=val1, width=3, from_=1,  to=31, state = 'readonly')        
        spn1.pack(side="left", padx=4 ,pady=2)   
        tk.Label(fram_,text='日' ).pack(side="left")
        txt1 = tk.StringVar(root)
        txt1.set(str(dic[ ls.tm()[2]]))
        opt1=tk.OptionMenu(fram_,txt1, '朝刊', '夕刊')  
        opt1.pack(side="left")  
        
        tk.Label(fram_,text='～' ).pack(side="left")  
        val2 = tk.IntVar(root)
        val2.set(str(dic[ ls.tm()[3]]))
        spn2 = tk.Spinbox(fram_, textvariable=val2, width=3, from_=1,  to=12, state = 'readonly')        
        spn2.pack(side="left", padx=2 ,pady=2) 
        tk.Label(fram_,text='月' ).pack(side="left") 
        val3 = tk.IntVar(root)
        val3.set(str(dic[ ls.tm()[4]]))
        spn3 = tk.Spinbox(fram_, textvariable=val3, width=3, from_=1,  to=31, state = 'readonly')        
        spn3.pack(side="left", padx=2 ,pady=2)   
        tk.Label(fram_,text='日' ).pack(side="left")
        txt3 = tk.StringVar(root)
        txt3.set(str(dic[ ls.tm()[5]]))
        opt3=tk.OptionMenu(fram_,txt3, '朝刊', '夕刊')  
        opt3.pack(side="left")  
        
        txt4 = tk.StringVar( root)
        txt4.set( str(dic[ ls.tm()[6]]))
        opt4= tk.OptionMenu( fram_, txt4, '無', '有')
        opt4.pack(side="left") # 
        tk.Button( fram_, text='次へ', command=lambda: edit.cmp.jnc( aa_, bb_, D.D_L( cc_, [ spn0.get(),spn1.get(),txt1.get(),spn2.get(),spn3.get(),txt3.get(),txt4.get()]), dd_, ee_) if spn0.get() !="" and spn1.get() !="" and txt1.get() !="" and spn2.get() !="" and spn3.get() !="" and txt3.get() !="" and txt4.get() !="" else tk.Label(root,text='未入力の箇所があります' ).pack(), relief="groove", bd=4 ).pack( side="left", padx=5)  
        if dic.get('取扱') in ['有', '無']: 
            tk.Button( frame, text="一時止情報の消去", command =lambda: call.cnsl( aa_, None, D.D(dic), None, root).post(), relief="groove",bg="lightgray").pack(padx=2)
        
        cmp.cancel(frame, aa_, dic, dd_,root)
        root.mainloop()
            
    def post(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c # 
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()
        dic= cc_    
        wdgt.forget( ee_)
        root = ee_ 
        root.title('一時止' + '編集' + ' ' + dic.get('名称1'))
        ww = root.winfo_screenwidth() 
        wh = root.winfo_screenheight()
        root.geometry( ls.ge(ww,wh) )
        root.option_add( '*font', [ 'TkDefaultFont', ls.ft()[0] ] )

        frame = tk.Frame(root )  
        r1__ = tk.Frame(frame )  
        r1__.pack( fill="x", padx=4, pady=4)
        frame.pack() 
        
        inv0, inv1, inv2, inv3 = tk.IntVar( root), tk.IntVar( root), tk.IntVar( root), tk.IntVar( root)
        inv0.set(dic.get( '始月')) #  ['始月','始日','始刊','終月','終日','終刊','取扱'] [,,'始刊',,,'終刊','取扱']
        inv1.set(dic.get( '始日')) 
        inv2.set(dic.get( '終月'))
        inv3.set(dic.get( '終日'))
        
        stv0, stv1, stv2 = tk.StringVar( root), tk.StringVar( root), tk.StringVar( root)
        stv0.set(dic.get( '始刊')) #  
        stv1.set(dic.get( '終刊'))
        stv2.set(dic.get( '取扱'))
        
        wdgt.sbx( r1__, inv0, 1, 12 ) # tk.Spinbox
        tk.Label( r1__, text='月' ).pack(side="left")  
        wdgt.sbx( r1__, inv1, 1, 31 )
        tk.Label( r1__, text='日' ).pack(side="left")
        wdgt.opm( r1__, stv0, '朝刊', '夕刊') # tk.OptionMenu
        tk.Label( r1__, text='～' ).pack(side="left")  
        wdgt.sbx( r1__, inv2, 1, 12 )
        tk.Label( r1__, text='月' ).pack(side="left") 
        wdgt.sbx( r1__, inv3,  1, 31 )
        tk.Label( r1__, text='日' ).pack(side="left")
        wdgt.opm( r1__, stv1, '朝刊', '夕刊')  
        wdgt.opm( r1__, stv2, '無', '有')
        tk.Button( r1__, text= '次へ', command= lambda: edit.cmp.jnc( aa_, bb_, D.D_L( cc_, [ inv0.get(),inv1.get(),stv0.get(),inv2.get(),inv3.get(),stv1.get(),stv2.get()]), dd_, ee_) if inv0.get() !="" and inv1.get() !="" and stv0.get() !="" and inv2.get() !="" and inv3.get() !="" and stv1.get() !="" and stv2.get() !="" else tk.Label(root,text='未入力の箇所があります' ).pack(), relief="groove", bd=4 ).pack( side="left", padx=5)  

        if dic.get('取扱') in ['有', '無']: 
            tk.Button( frame, text="一時止情報の消去", command =lambda: call.cnsl( aa_, None, D.D(dic), None, root).post(), relief="groove",bg="lightgray").pack(padx=2)
        
        cmp.cancel( frame, aa_, dic, dd_, root)
        root.mainloop()
        
    def cancel( frame, aa_, dic, dd_, root):
        btn = tk.Button( frame, text="キャンセル", command= lambda: call.cnsl( aa_, None, dic, dd_, root).post(), relief="groove", bd=4, anchor="e")
        btn.bind( '<Return>', lambda event: call.cnsl( aa_, None, dic, dd_, root).post() )
        btn.focus_force()  
        btn.pack( padx=2, pady=2) 

class D(): 
    # 一時止情報を加える
    def D_L( dic:dict, lis:list) -> dict: #
        ( lis) # ['1', '1', '朝刊', '1', '1', '夕刊', '有']
        for i , txt in enumerate( ls.tm()): # ['始月', '始日', '始刊', '終月', '終日', '終刊', '取扱']
            dic[ txt] = lis[i]
        return dic
    
    # 一時止情報の消去
    def D(dic):
        for i in ls.tm(): 
            dic[ i ] = '' 
        return dic # {'区分': '人事院', '区間': '', '名称1': '総務課②', '号数': '２', '赤字': '赤字', '一時止': '', '始月': '', '始日': '', '始刊': '', '終月': '', '終日': '', '終刊': '', '取扱': '',
        
class cnfg:###configuration:構成
    def tx(dic):###text
        if dic.get( ls.tm()[0]) != "" :
            "{0}月{1}日{2}～{3}月{4}日{5}迄　{6}"
            t0, t1, t2, t3, t4, t5, t6 = [ dic.get(i) for i in ls.tm()]
            return "{6}".format( t0, t1, t2, t3, t4, t5, t6 ) 
        else:
            return ''
        
    def fg(dic):
        if dic.get( ls.tm()[6]) == '無':
            return ls.cl()[0]   
        elif dic.get( ls.tm()[6]) == '有':
            return ls.cl()[1] 
        else:
            return ls.cl()[1]
    
    def bg(dic):
        if dic.get( ls.tm()[6]) == '無':
            return 'silver'  
        elif dic.get( ls.tm()[6]) == '有':
            return 'royalblue'  
        else:
            return ls.cl()[1]
    
    def relief(dic):
        if dic.get( ls.tm()[6]) == '無':
            return 'flat'  
        elif dic.get( ls.tm()[6]) == '有':
            return 'flat'  
        else:
            return 'flat' 

    
class wdgt: # widget       
    def sbx( frame, val, i0, i1 ): # Spinbox
        spn = tk.Spinbox(frame, textvariable=val, width=3, from_=i0,  to=i1, state = 'readonly')        
        spn.pack(side="left", padx=4, pady=2) 
        return spn
    
    def opm( frame, var, str0, str1): # OptionMenu
        opm = tk.OptionMenu(frame, var, str0, str1)  
        opm.pack(side="left")  
        return opm             
    
    def forget( root):
        children = root.winfo_children() 
        for child in children:
            child.destroy() 
            
if __name__ == '__main__':   ##これがないと外部からインポートされた際に処理が実行されてしまう。              
         
    root = tk.Tk() 
    aa_ = 1
    dic = ls.customer()[aa_]
    (dic)
    prfl = { 'ファイル名':os.path.basename(__file__)}
    cmp(aa_, ls.ic(), dic, prfl, root).post()

    for i, txt in enumerate( ls.tm() ):
        dic[ txt ] = ["","","","","","",""][i]
    (dic)
