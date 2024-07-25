# 78. File Dialogue[07:48:48]-----------------------------------------------------------
from tkinter import *
from tkinter import filedialog
def openFile():
    filePath=filedialog.askopenfilename(initialdir="E:\\BorCodePython\\.vscode",
                                        title="Open File okay?",
                                        filetypes=(("text files","*.txt"),
                                                   ("all files","*.*")))
    file = open(filePath,'r')
    print(file.read())
    file.close()
window = Tk()
button = Button(text="Open",command=openFile)
button.pack()




window.mainloop()