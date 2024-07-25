# 80. Menu Bar in python [08:05:25]-------------------------------------------------------
from tkinter import *
def openFile():
    print("File has been open")

def saveFile():
    print("File has been saved")
def cut():
    print("The file is cut")
def copy():
    print("You copied some text")
def paste():
    print("You pasted some text")
window=Tk()
# openImage = PhotoImage(file="open.png")
# saveImage=PhotoImage(file="save.png")
# exitImage = PhotoImage(file="exit.png")
menuBar=Menu(window)
window.config(menu=menuBar)

fileMenu=Menu(menuBar,tearoff=0,font=("MV Boli",15))
menuBar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,
                    #  image=openImage,
                     compound='left')
fileMenu.add_command(label="Save",command=saveFile,
                    #  image=saveImage,
                     compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,
                    #  image=exitImage,
                     compound='left')


editMenu = Menu(menuBar,tearoff=0,font=("MV Boli",15))
menuBar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)



window.mainloop()