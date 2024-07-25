# 70. Entry Box in python [ 06:30:55]-----------------------------------------
from tkinter import *

window = Tk()
def submit():
    userName=entry.get()
    print("Hello "+userName)
    entry.config(state="disabled")
def delete():
        entry.delete(0,END)
def backspace():
      entry.delete(len(entry.get())-1,END)
entry = Entry(window,
              font=("Arial",50,'italic'),
              fg="#00FF00",
              bg="black",
              show="$")
entry.insert(0,"SpongeBob")
entry.pack(side="left")
submit_button=Button(window,
                     text="Submit",
                     command=submit
                     )
submit_button.pack(side="right")
delete_button=Button(window,
                     text="delete",
                     command=delete
                     )
delete_button.pack(side="right")
backspace_button=Button(window,
                     text="backspace",
                     command=backspace
                     )
backspace_button.pack(side="right")

window.mainloop()