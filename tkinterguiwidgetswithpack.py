from tkinter import *
root=Tk()
def callback():
     print("click!")
b1=Button(root,text="shravan",command=callback,bg="red",fg="green")
b2=Button(root,text="kamat",command=callback,bg="red",fg="green")
b1.pack()
b2.pack()
