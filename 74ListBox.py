# 74 List Box [07:10:35]------------------------------------------------
from tkinter import *
def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered: ")
    for index in food: 
        print(index)
    # print(listbox.get(listbox.curselection()))
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())
window = Tk()
window.title("This is List Box")
listbox = Listbox(window,
                  font=("Constantia",35),
                  bg="#f7ffde",
                  width=20,
                  selectmode=MULTIPLE,
                  )
listbox.pack()
listbox.insert(1,"Pizza")
listbox.insert(2,"Spegatte")
listbox.insert(3,"Garlic Bread")
listbox.insert(4,"Cheesy Bites")
listbox.insert(5,"Choco Lava Cake")
listbox.insert(6,"Mushroom Bread")
listbox.config(height=listbox.size())
entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="Submit",
                      command=submit)
submitButton.pack()
addButton = Button(window,text="Add",
                      command=add)
addButton.pack()
deleteButton = Button(window,text="Delete",
                      command=delete)
deleteButton.pack()


window.mainloop()