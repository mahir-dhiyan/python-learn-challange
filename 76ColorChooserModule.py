# 76. Color Chooser Module [ 07:37:27]------------------------------------------------------------
from tkinter import *
from tkinter import colorchooser
def click():
    # color = colorchooser.askcolor()
    # colorHex=color[1]
    # window.config(background=colorHex)
    window.config(bg=colorchooser.askcolor()[1])
window=Tk()

window.geometry("420x420")
button = Button(window,text="Click Me",command=click)
button.pack()
window.mainloop()