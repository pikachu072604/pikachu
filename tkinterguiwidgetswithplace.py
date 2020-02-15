from tkinter import *
root=Tk()
def callback():
     print("click!")
b1=Button(root,text="shravan",command=callback,bg="red",fg="blue")
b2=Button(root,text="kamat",command=callback,bg="red",fg="blue")
b1.place(x=200,y=200)
b2.place(x=500,y=500)
