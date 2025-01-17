from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# search box
search_image = Image.open(file="C:/Users/USER/Desktop/Official Projects/PYTHON/Python API/Weather App/images/searching.png")
search_image = ImageTk.PhotoImage(search_image)
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", 
                     width=17, font=("Poppins", 25, "bold"), 
                     bg="#404040", border=0, fg="#fff")
textfield.place(x=50, y=50)
textfield.focus()

# search icon
search_icon = PhotoImage(file="search.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2")

root.mainloop()