from tkinter import *
root=Tk()
def quit():
    root.quit()
    root.destroy()
    exit()
MenuBar=Menu(root)
root.config(menu=MenuBar)
fileMenu=Menu(MenuBar,tearoff=1)
fileMenu.add_command(label="New")

fileMenu.add_command(label="Exit",command=quit)
MenuBar.add_cascade(label="File",menu=fileMenu)
fileMenu1=Menu(MenuBar)
fileMenu1.add_command(label="Help")
MenuBar.add_cascade(label="About",menu=fileMenu1)



