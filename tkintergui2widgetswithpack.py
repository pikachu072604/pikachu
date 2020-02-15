from tkinter import *
root=Tk()
def left():
     print("click!")
b1=Button(root,text="shravan",command=left)
b2=Button(root,text="kamat",command=left)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
