# tkinter for text input(entry)
from tkinter import *

root = Tk()

# use e as entry control
e = Entry(root, width=25)
# e.insert(0, "Enter your name here...")
# pack it on screen
e.pack()


def myClick():
    output = f"Hello {e.get()}"
    lbl = Label(root, text=output)
    lbl.pack()


btn = Button(root, text="Display Name", command=myClick, padx=25, pady=5)
btn.pack()

root.mainloop()
