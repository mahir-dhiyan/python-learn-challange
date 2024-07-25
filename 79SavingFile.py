# 79. Saving File[07:55:45]--------------------------------------------------------
from tkinter import *
from tkinter import filedialog
def saveFile():
    file = filedialog.asksaveasfile(initialdir="E:\\BorCodePython\\.vscode",
                                     defaultextension='.txt',
                                    filetypes=[("Text File",".txt"),
                                               ("HTML File",".html"),
                                               ("All Files",".*")])
    if file is None:
        return
    fileText=str(text.get(1.0,END))
    # fileText=input("Enter some text I guess: ")
    file.write(fileText)
    file.close()
window = Tk()
button = Button(text="Save",command=saveFile)
button.pack()
text=Text(window)
text.pack()






window.mainloop()