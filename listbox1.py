from tkinter import *
root=Tk()
def display():
     print(list1.get(ACTIVE))
list1=Listbox(root)
lst_entries=["Data0","Data1","Data2","Data3"]
for v in lst_entries:
     list1.insert(END,v)
b1=Button(root,text="Get",command=display)
list1.pack()
b1.pack()
del_index=int(input("enter Index to delete: "))
list1.delete(del_index)
