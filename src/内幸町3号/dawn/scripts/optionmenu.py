import os.path
import tkinter as tk
import ls
import sys

class option(ls.sp): 
    def select(self):        
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        ls.nm(os.path.splitext( os.path.basename(__file__) )[0] ,__class__.__name__,sys._getframe().f_code.co_name).class_def() 
        if cc_.get() == ls.mn()[0]: #一般日刊紙など
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.nw()[0][0],command =lambda: dd_.set(ls.nw()[0][0]))
            bb_['menu'].add_command(label=ls.nw()[0][1],command =lambda: dd_.set(ls.nw()[0][1]))
            bb_['menu'].add_command(label=ls.nw()[0][2],command =lambda: dd_.set(ls.nw()[0][2]))#
            bb_['menu'].add_command(label=ls.nw()[0][3],command =lambda: dd_.set(ls.nw()[0][3]))
            bb_['menu'].add_command(label=ls.nw()[0][4],command =lambda: dd_.set(ls.nw()[0][4]))
            bb_['menu'].add_command(label=ls.nw()[0][5],command =lambda: dd_.set(ls.nw()[0][5]))         
                                       
        elif cc_.get() == ls.mn()[1]:
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.nw()[1][0],command =lambda: dd_.set(ls.nw()[1][0]))
            bb_['menu'].add_command(label=ls.nw()[1][1],command =lambda: dd_.set(ls.nw()[1][1]))
            bb_['menu'].add_command(label=ls.nw()[1][2],command =lambda: dd_.set(ls.nw()[1][2]))
            bb_['menu'].add_command(label=ls.nw()[1][3],command =lambda: dd_.set(ls.nw()[1][3]))
            bb_['menu'].add_command(label=ls.nw()[1][4],command =lambda: dd_.set(ls.nw()[1][4]))
        elif cc_.get() == ls.mn()[2]:
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.nw()[2][0],command =lambda: dd_.set(ls.nw()[2][0]))
            bb_['menu'].add_command(label=ls.nw()[2][1],command =lambda: dd_.set(ls.nw()[2][1]))
            bb_['menu'].add_command(label=ls.nw()[2][2],command =lambda: dd_.set(ls.nw()[2][2]))
            bb_['menu'].add_command(label=ls.nw()[2][3],command =lambda: dd_.set(ls.nw()[2][3]))
        elif cc_.get()== ls.mn()[3]:
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.nw()[3][0],command =lambda: dd_.set(ls.nw()[3][0]))
            bb_['menu'].add_command(label=ls.nw()[3][1],command =lambda: dd_.set(ls.nw()[3][1]))
            bb_['menu'].add_command(label=ls.nw()[3][2],command =lambda: dd_.set(ls.nw()[3][2]))
            bb_['menu'].add_command(label=ls.nw()[4][0],command =lambda: dd_.set(ls.nw()[4][0]))#
        elif cc_.get() == ls.mn()[4]:
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.nw()[5][0],command =lambda: dd_.set(ls.nw()[5][0]))
            bb_['menu'].add_command(label=ls.nw()[5][1],command =lambda: dd_.set(ls.nw()[5][1]))
            bb_['menu'].add_command(label=ls.nw()[5][2],command =lambda: dd_.set(ls.nw()[5][2]))
            bb_['menu'].add_command(label=ls.nw()[5][3],command =lambda: dd_.set(ls.nw()[5][3]))
            bb_['menu'].add_command(label=ls.nw()[6][0],command =lambda: dd_.set(ls.nw()[6][0]))#
            bb_['menu'].add_command(label=ls.nw()[6][1],command =lambda: dd_.set(ls.nw()[6][1]))
            
        elif cc_.get() == ls.mn()[5]:
            bb_['menu'].delete(0,tk.END) 
            bb_['menu'].add_command(label=ls.nw()[7][0],command =lambda: dd_.set(ls.nw()[7][0]))
            bb_['menu'].add_command(label=ls.nw()[7][1],command =lambda: dd_.set(ls.nw()[7][1]))
            bb_['menu'].add_command(label=ls.nw()[8][0],command =lambda: dd_.set(ls.nw()[8][0]))#
            bb_['menu'].add_command(label=ls.nw()[8][1],command =lambda: dd_.set(ls.nw()[8][1]))
            bb_['menu'].add_command(label=ls.nw()[9][0],command =lambda: dd_.set(ls.nw()[9][0]))#
            bb_['menu'].add_command(label=ls.nw()[9][1],command =lambda: dd_.set(ls.nw()[9][1]))
            bb_['menu'].add_command(label=ls.nw()[9][2],command =lambda: dd_.set(ls.nw()[9][2]))
            bb_['menu'].add_command(label=ls.nw()[9][3],command =lambda: dd_.set(ls.nw()[9][3]))
        elif cc_.get() == ls.mn()[6]:
            bb_['menu'].delete(0,tk.END) 
            bb_['menu'].add_command(label=ls.nw()[10][0],command =lambda: dd_.set(ls.nw()[10][0]))
            bb_['menu'].add_command(label=ls.nw()[10][1],command =lambda: dd_.set(ls.nw()[10][1]))
            bb_['menu'].add_command(label=ls.nw()[10][2],command =lambda: dd_.set(ls.nw()[10][2]))
            bb_['menu'].add_command(label=ls.nw()[10][3],command =lambda: dd_.set(ls.nw()[10][3]))
            bb_['menu'].add_command(label=ls.nw()[10][4],command =lambda: dd_.set(ls.nw()[10][4]))
            bb_['menu'].add_command(label=ls.nw()[10][5],command =lambda: dd_.set(ls.nw()[10][5])) 
        elif cc_.get() == ls.mn()[7]:
            bb_['menu'].delete(0,tk.END) 
            bb_['menu'].add_command(label=ls.nw()[11][0],command =lambda: dd_.set(ls.nw()[11][0]))
            bb_['menu'].add_command(label=ls.nw()[11][1],command =lambda: dd_.set(ls.nw()[11][1]))
            bb_['menu'].add_command(label=ls.nw()[12][0],command =lambda: dd_.set(ls.nw()[12][0]))#
            bb_['menu'].add_command(label=ls.nw()[12][1],command =lambda: dd_.set(ls.nw()[12][1]))
            bb_['menu'].add_command(label=ls.nw()[12][2],command =lambda: dd_.set(ls.nw()[12][2]))
            bb_['menu'].add_command(label=ls.nw()[12][3],command =lambda: dd_.set(ls.nw()[12][3]))
            bb_['menu'].add_command(label=ls.nw()[12][4],command =lambda: dd_.set(ls.nw()[12][4]))
            bb_['menu'].add_command(label=ls.nw()[12][5],command =lambda: dd_.set(ls.nw()[12][5]))
        elif cc_.get() == ls.mn()[8]:
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.nw()[13][0],command =lambda: dd_.set(ls.nw()[13][0]))
            bb_['menu'].add_command(label=ls.nw()[13][1],command =lambda: dd_.set(ls.nw()[13][1]))
            bb_['menu'].add_command(label=ls.nw()[13][2],command =lambda: dd_.set(ls.nw()[13][2]))
            bb_['menu'].add_command(label=ls.nw()[13][3],command =lambda: dd_.set(ls.nw()[13][3]))
            bb_['menu'].add_command(label=ls.nw()[13][4],command =lambda: dd_.set(ls.nw()[13][4]))
            bb_['menu'].add_command(label=ls.nw()[13][5],command =lambda: dd_.set(ls.nw()[13][5])) 
            bb_['menu'].add_command(label=ls.nw()[13][6],command =lambda: dd_.set(ls.nw()[13][6])) 
            bb_['menu'].add_command(label=ls.nw()[13][7],command =lambda: dd_.set(ls.nw()[13][7])) 
            
            bb_['menu'].add_command(label=ls.nw()[14][0],command =lambda: dd_.set(ls.nw()[14][0]))
            bb_['menu'].add_command(label=ls.nw()[14][1],command =lambda: dd_.set(ls.nw()[14][1]))
            bb_['menu'].add_command(label=ls.nw()[14][2],command =lambda: dd_.set(ls.nw()[14][2]))
            bb_['menu'].add_command(label=ls.nw()[14][3],command =lambda: dd_.set(ls.nw()[14][3]))
        elif cc_.get() == ls.mn()[9]:
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.nw()[15][0],command =lambda: dd_.set(ls.nw()[15][0]))
            bb_['menu'].add_command(label=ls.nw()[15][1],command =lambda: dd_.set(ls.nw()[15][1]))
            bb_['menu'].add_command(label=ls.nw()[15][2],command =lambda: dd_.set(ls.nw()[15][2]))
            bb_['menu'].add_command(label=ls.nw()[15][3],command =lambda: dd_.set(ls.nw()[15][3]))
        elif cc_.get() == ls.mn()[10]:
            bb_['menu'].delete(0,tk.END) 
            bb_['menu'].add_command(label=ls.nw()[16][0],command =lambda: dd_.set(ls.nw()[16][0]))
            bb_['menu'].add_command(label=ls.nw()[16][1],command =lambda: dd_.set(ls.nw()[16][1]))
            bb_['menu'].add_command(label=ls.nw()[16][2],command =lambda: dd_.set(ls.nw()[16][2]))
            bb_['menu'].add_command(label=ls.nw()[16][3],command =lambda: dd_.set(ls.nw()[16][3]))
            bb_['menu'].add_command(label=ls.nw()[16][4],command =lambda: dd_.set(ls.nw()[16][4]))
            bb_['menu'].add_command(label=ls.nw()[16][5],command =lambda: dd_.set(ls.nw()[16][5]))
            bb_['menu'].add_command(label=ls.nw()[16][6],command =lambda: dd_.set(ls.nw()[16][6]))
            bb_['menu'].add_command(label=ls.nw()[16][7],command =lambda: dd_.set(ls.nw()[16][7]))
            bb_['menu'].add_command(label=ls.nw()[16][8],command =lambda: dd_.set(ls.nw()[16][8]))
            bb_['menu'].add_command(label=ls.nw()[16][9],command =lambda: dd_.set(ls.nw()[16][9]))
            
            bb_['menu'].add_command(label=ls.nw()[17][0],command =lambda: dd_.set(ls.nw()[17][0]))
            bb_['menu'].add_command(label=ls.nw()[17][1],command =lambda: dd_.set(ls.nw()[17][1]))
            bb_['menu'].add_command(label=ls.nw()[17][2],command =lambda: dd_.set(ls.nw()[17][2]))
            bb_['menu'].add_command(label=ls.nw()[17][3],command =lambda: dd_.set(ls.nw()[17][3]))
            bb_['menu'].add_command(label=ls.nw()[17][4],command =lambda: dd_.set(ls.nw()[17][4]))
            bb_['menu'].add_command(label=ls.nw()[17][5],command =lambda: dd_.set(ls.nw()[17][5]))
            bb_['menu'].add_command(label=ls.nw()[17][6],command =lambda: dd_.set(ls.nw()[17][6]))
            bb_['menu'].add_command(label=ls.nw()[17][7],command =lambda: dd_.set(ls.nw()[17][7]))
            bb_['menu'].add_command(label=ls.nw()[17][8],command =lambda: dd_.set(ls.nw()[17][8]))
            bb_['menu'].add_command(label=ls.nw()[17][9],command =lambda: dd_.set(ls.nw()[17][9]))
            bb_['menu'].add_command(label=ls.nw()[17][10],command =lambda: dd_.set(ls.nw()[17][10]))
            bb_['menu'].add_command(label=ls.nw()[17][11],command =lambda: dd_.set(ls.nw()[17][11]))
            bb_['menu'].add_command(label=ls.nw()[17][12],command =lambda: dd_.set(ls.nw()[17][12]))

    def division(self): #division:区分
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        if cc_.get() == ls.pa()[0]:# Place name
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.ea()[0][0],command =lambda: dd_.set(ls.ea()[0][0]))
            bb_['menu'].add_command(label=ls.ea()[0][1],command =lambda: dd_.set(ls.ea()[0][1]))
            bb_['menu'].add_command(label=ls.ea()[0][2],command =lambda: dd_.set(ls.ea()[0][2]))#
            bb_['menu'].add_command(label=ls.ea()[0][3],command =lambda: dd_.set(ls.ea()[0][3]))
            bb_['menu'].add_command(label=ls.ea()[0][4],command =lambda: dd_.set(ls.ea()[0][4]))
            bb_['menu'].add_command(label=ls.ea()[0][5],command =lambda: dd_.set(ls.ea()[0][5]))
            bb_['menu'].add_command(label=ls.ea()[0][6],command =lambda: dd_.set(ls.ea()[0][6]))                                        
        elif cc_.get() == ls.pa()[1]:
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.ea()[1][0],command =lambda: dd_.set(ls.ea()[1][0]))
            bb_['menu'].add_command(label=ls.ea()[1][1],command =lambda: dd_.set(ls.ea()[1][1]))
            bb_['menu'].add_command(label=ls.ea()[1][2],command =lambda: dd_.set(ls.ea()[1][2]))   
            
    def human(self): #
        aa_ = self.a #
        bb_ = self.b #   
        cc_ = self.c #
        dd_ = self.d #  
        ee_ = self.e #        
        ls.sp(aa_,bb_,cc_,dd_,ee_).pasS()  
        if cc_.get() == ls.rw()[0]:# Place name
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.hu()[0][0],command =lambda: dd_.set(ls.hu()[0][0]))
            bb_['menu'].add_command(label=ls.hu()[0][1],command =lambda: dd_.set(ls.hu()[0][1]))
            bb_['menu'].add_command(label=ls.hu()[0][2],command =lambda: dd_.set(ls.hu()[0][2]))#
            bb_['menu'].add_command(label=ls.hu()[0][3],command =lambda: dd_.set(ls.hu()[0][3]))
            bb_['menu'].add_command(label=ls.hu()[0][4],command =lambda: dd_.set(ls.hu()[0][4]))
            bb_['menu'].add_command(label=ls.hu()[0][5],command =lambda: dd_.set(ls.hu()[0][5]))   
        elif cc_.get() == ls.rw()[1]:
            bb_['menu'].delete(0,tk.END)
            bb_['menu'].add_command(label=ls.hu()[1][0],command =lambda: dd_.set(ls.hu()[1][0]))
            bb_['menu'].add_command(label=ls.hu()[1][1],command =lambda: dd_.set(ls.hu()[1][1]))
            bb_['menu'].add_command(label=ls.hu()[1][2],command =lambda: dd_.set(ls.hu()[1][2]))#
            bb_['menu'].add_command(label=ls.hu()[1][3],command =lambda: dd_.set(ls.hu()[1][3]))
            bb_['menu'].add_command(label=ls.hu()[1][4],command =lambda: dd_.set(ls.hu()[1][4]))
            bb_['menu'].add_command(label=ls.hu()[1][5],command =lambda: dd_.set(ls.hu()[1][5])) 
          