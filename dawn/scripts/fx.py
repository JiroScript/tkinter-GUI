import ls
# fixed point :定点観測

class r: # root.py
    def u(*args): # uno
        try:
            (' '.join([ str(i) for i in args]))
        except IndexError:
            print("IndexError")
            pass
    def x(*args): #  
        try:
            (' '.join([ str(i) for i in args]))
        except IndexError:
            print("IndexError")
            pass
        
    def d( txt, start, end, pail, tub, lst): # duo   
        try:
            (txt,
                  start,
                  end,
                  pail,
                  len(tub[1:]),
                  # tub,
                  # tub[:-1],
                  sum(tub),
                  lst[ end - pail][ ls.mi()][0:1],
                  lst[ end - pail][ ls.hb()],
                  lst[ end - pail][ ls.pg()[0]][0:1],)
        except IndexError:
            print("IndexError")
            pass

class a: # auxi.py
    def u(*args): # uno
        try:
            (' '.join([ str(i) for i in args]))
        except IndexError:
            print("IndexError")
            pass

class l: # auxi.py
    def u(*args): # uno
        try:
            (' '.join([ str(i) for i in args]))
        except IndexError:
            print("IndexError")
            pass
    def d(*args): # duo
        try:
            (' '.join([ str(i) for i in args]))
        except IndexError:
            print("IndexError")
            pass
    def t(*args): # duo
        try:
            print(' '.join([ str(i) for i in args]))
        except IndexError:
            print("IndexError")
            pass