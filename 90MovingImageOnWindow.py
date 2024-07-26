# 90. Moving Image on window[09:18:27]-----------------------------------------------
from tkinter import *
from PIL import Image, ImageTk
window=Tk()

window.geometry("500x500") 
def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())
# Insitiate image
pil_image = Image.open('car.png')
# Resize the image
resized_image = pil_image.resize((100, 100), Image.LANCZOS)
# Convert the PIL image to a Tkinter PhotoImage
tk_image = ImageTk.PhotoImage(resized_image)
# myimage=PhotoImage(file='car.png')
# ----------------------------------------------
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)
label=Label(window,image=tk_image)
label.place(x=0,y=0)


window.mainloop()