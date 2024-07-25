# 82. New windows in python [08:21:40]----------------------------------------------------
from tkinter import *
def create_window():
    new_window=Toplevel()      #Toplevel() = new window on top of other window,
                                #linked to a bottom window
    # new_window=Tk()
    # window.destroy()
window= Tk()

Button(window,text="Create New Window", command=create_window).pack()

window.mainloop()