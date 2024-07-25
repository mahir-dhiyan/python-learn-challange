# 83. Seperate Tabs [08:25:42]------------------------------------------------------------
from tkinter import *
from tkinter import ttk
window=Tk()
notebook=ttk.Notebook(window) #widget that manages a colloection of windows/displays

tab1=Frame(notebook)
tab2=Frame(notebook)

notebook.add(tab1,text="Tab-1")
notebook.add(tab2,text="Tab-2")
notebook.pack(expand=True,fill=BOTH)
Label(tab1,text="Hello!! This is tab#1",width=50,height=25).pack()
Label(tab2,text="Goodbye!! This is tab#2",width=50,height=25).pack()
window.mainloop()