from tkinter import *
import _thread
import time

def test(ta):
    print("inta")
    while 1:
        time.sleep(5)       
        f = open("IP1.txt","r")
        test=f.read()
        f.close()
        ta.set(test)
    
    

def guir(cip):
    print("imthread")
    root = Tk()
    var=StringVar()
    w = Label(root, textvariable=var)
    var.set(cip)
    w.pack()
    _thread.start_new_thread(test, (var,)) 
    root.mainloop()
