from tkinter import *
from tkinter import StringVar
import requests

url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API key}'

def get_weather(get):
    lat = 40.7128    # replace with actual latitude
    lon = -74.0060   # replace with actual longitude
    API_key = '84f57fb17a45833e34c275bb464946ad'  # replace with your API key
    response = requests.get(url.format(lat=lat, lon=lon, API_key=API_key))
    data = response.json()
    # Process data here

app = Tk()
app.title("Weather App")
app.geometry("600x300+450+100")

city_text: StringVar = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app,  text="Search", width=12, command=lambda:get_weather(city_text.get()))
search_btn.pack()

location_lbl =  Label(app, text="Location",  font=("Arial", 20, "bold"))
location_lbl.pack()

image = Label(app, bitmap='')
image.pack()

temp_lbl = Label(app, text="")
temp_lbl.pack()

weather_lbl = Label(app, text="Weather")
weather_lbl.pack()


app.mainloop()