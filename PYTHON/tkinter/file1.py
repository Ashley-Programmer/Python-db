# tkinter for label
from tkinter import *

root = Tk()

# creating a label widget
myLabel = Label(root, text="Hello World!")

# place it onto the screen
myLabel.pack()

# create an event loop
root.mainloop()
