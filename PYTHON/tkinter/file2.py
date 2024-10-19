# tkinter labels positioning
from tkinter import *

root = Tk()

# creating labels
myLabel1 = Label(root, text="Hello there!").grid(row=0, column=0)
myLabel2 = Label(root, text="I am Ashley.Programmer").grid(row=1, column=0)

# place onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)

root.mainloop()
