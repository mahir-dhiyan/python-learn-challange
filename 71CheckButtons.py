# 71. Check Buttons [06:40:23]-----------------------------------------------------------
from tkinter import *
window=Tk()
def display():
    if(x.get()==1):
        print("Oh! wow! You agree to this")
    else: 
        print("Oh no! You don't agree with this :(")

star_photo=PhotoImage(file="logo.png")
x=IntVar()
# x=BooleanVar()
# x=StringVar()
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           fg="#00FF00",
                           bg="black",
                           font=("Arial",20,"italic"),
                           activebackground="black",
                           activeforeground="#00FF00",
                           padx=10,
                           pady=10,
                           image=star_photo,
                           compound="left",
                           )
check_button.pack()
window.mainloop()