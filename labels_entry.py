from tkinter import *
root=Tk()
def display():
     print("Name: "+ent1.get())
l1=Label(root,text="enter name: ")
ent1=Entry(root)
b=Button(root,text="submit",command=display)
l1.grid(row=0,column=0)
ent1.grid(row=0,column=1)
b.grid(row=0,column=2)
