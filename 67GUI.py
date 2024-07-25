# 67. Graphical User Interface in python [ 06:07:25]------------------------------------------------
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets
from tkinter import *
window= Tk() #instanttiate an instance of a window
window.geometry("420x420")
window.title("Mahir Dhiyan's first GUI Programme")
icon=PhotoImage(file="logo.png")
window.iconphoto(True,icon)
# window.config(background="#5cfcff")
window.config(background="black")
window.mainloop() #place window on computer screen, listen for events
