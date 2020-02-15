from tkinter import *
root=Tk()
v=IntVar()
v.set(0)
lang_list=[("python",0),("wp",1),("jquery",2),("javascript",3)]
def showChoice():
    print("you have selected: ",v.get())
l=Label(root,text="select yourfavourite program: language: " )
l.pack()
for txt,val in lang_list:
    r=Radiobutton(root,text=txt,variable=v,command=showChoice,value=val)
    r.pack()
