# tkinter for button
from tkinter import *

root = Tk()


# create a function for your button to do something
def myClick():
    myLabel = Label(root, text="The button has been clicked!")
    # place the label on the screen
    myLabel.pack()


# create a button
# invoke the function within it using "command"
myBtn = Button(root, text="Click Me!", fg="red", bg="lightgreen", padx=50, pady=20, command=myClick)

# place it on the screen
myBtn.pack()

root.mainloop()
