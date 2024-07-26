from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.geometry("500x500")
pil_image = Image.open("car.png")
resize_image=pil_image.resize((100,100),Image.LANCZOS)
image=ImageTk.PhotoImage(resize_image)
label=Label(window,image=image,bg="red")
label.place(x=0,y=0)





window.mainloop()