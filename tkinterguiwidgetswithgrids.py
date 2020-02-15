from tkinter import *
root=Tk()
def callback():
     print("click!")
b1=Button(root,text="shravan",command=callback)
b2=Button(root,text="kamat",command=callback)
b3=Button(root,text="cryogen",command=callback)
b4=Button(root,text="78",command=callback)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)
