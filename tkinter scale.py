from tkinter import *
root=Tk()
s1=Scale(root,from_=0,to=80)
s1.pack()
s2=Scale(root,from_=0,to=50,orient=HORIZONTAL)
s2.pack()
def getValue():
    print(s1.get())
    print(s2.get())
b1=Button(root,text="GetValue",command=getValue)
b1.pack()
