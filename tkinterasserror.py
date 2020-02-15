from tkinter import *
from tkinter import messagebox
root=Tk()
def c1():
    messagebox.showinfo("information","Information")
def c2():
    messagebox.showwarning("warning","Warning")
def c3():
    messagebox.showerror("error","Error")
def c4():
    messagebox.askquestion("confirm","are u sure?")
    
root.geometry("100x100")

b1=Button(root,text="showinfo",command=c1)
b2=Button(root,text="showwarning",command=c2)
b3=Button(root,text="showerror",command=c3)
b4=Button(root,text="askquestion",command=c4)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
