from tkinter import *
root=Tk()
list1=Listbox(root,selectmode=EXTENDED)
list1.insert(0,"data1")
list1.insert(1,"data2")
list1.insert(2,"data3")
list1.insert(3,"data4")
'''def display():
     print(list1.get(ACTIVE))
lst_entries=["Data0","Data1","Data2","Data3"]
for v in lst_entries:
     list1.insert(END,v)
b1=Button(root,text="Get",command=display)
del_index=int(input("enter Index to delete: "))
list1.delete(del_index)'''
list1.pack()
#b1.pack()
