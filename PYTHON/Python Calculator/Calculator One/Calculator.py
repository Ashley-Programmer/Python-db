import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
# Calculator


# Functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# GUI Section
root = tk.Tk()

window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def myclick(number):
    entry.insert(tk.END, number)

# def equal():
#     try:
#         y = str(eval(entry.get()))
#         entry.delete(0, tk.END)
#         entry.insert(0, y)
#     except SyntaxError:
#         tkinter.messagebox.showinfo("Error", "Syntax Error")


def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except SyntaxError:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
    except NameError:
        tkinter.messagebox.showinfo("Error", "Invalid input")
    except ZeroDivisionError:
        tkinter.messagebox.showinfo("Error", "Division by zero is not allowed")
    except Exception as e:
        tkinter.messagebox.showinfo("Error", str(e))


def clear():
    entry.delete(0, tk.END)


# Buttons 7 to 9
button_7 = tk.Button(master=frame, text="7", padx=18, pady=5, width=3,
                     command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)

button_8 = tk.Button(master=frame, text="8", padx=18, pady=5, width=3,
                     command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)

button_9 = tk.Button(master=frame, text="9", padx=18, pady=5, width=3,
                     command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)

# Buttons 4 to 6
button_4 = tk.Button(master=frame, text="4", padx=18, pady=5, width=3,
                     command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)

button_5 = tk.Button(master=frame, text="5", padx=18, pady=5, width=3,
                     command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)

button_6 = tk.Button(master=frame, text="6", padx=18, pady=5, width=3,
                     command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)

# Buttons 1 to 3
button_1 = tk.Button(master=frame, text="1", padx=18, pady=5, width=3,
                     command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)

button_2 = tk.Button(master=frame, text="2", padx=18, pady=5, width=3,
                     command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)

button_3 = tk.Button(master=frame, text="3", padx=18, pady=5, width=3,
                     command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)



# button 0
button_0 = tk.Button(master=frame, text="0", padx=18, pady=5, width=3,
                     command=lambda: myclick(0))
button_0.grid(row=4, column=0, pady=2)

# Operator(s) buttons
# Plus Operator
button_plus = tk.Button(master=frame, text="+", padx=18, pady=5, width=3,
                        command=lambda: myclick('+'))
button_plus.grid(row=5, column=0, pady=2)

# Minus Operator
button_minus = tk.Button(master=frame, text="-", padx=18, pady=5, width=3,
                         command=lambda: myclick('-'))
button_minus.grid(row=5, column=1, pady=2)

# Multiply Operator
button_multiply = tk.Button(master=frame, text="*", padx=18, pady=5, width=3,
                            command=lambda: myclick('*'))
button_multiply.grid(row=4, column=1, pady=2)

# Division Operator
button_division = tk.Button(master=frame, text="/", padx=18, pady=5, width=3,
                            command=lambda: myclick('/'))
button_division.grid(row=4, column=2, pady=2)

# Clear button
button_clear = tk.Button(master=frame, text="C", padx=18, pady=5,
                         width=3, command=clear)
button_clear.grid(row=5, column=2, pady=2)

# Assignment button
button_equal = tk.Button(master=frame, text="=", padx=18, pady=5,
                         width=12, command=equal)
button_equal.grid(row=6, column=1, columnspan=1, pady=2)

window.mainloop()
