from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinderL import TimezoneFinder
from datetime import datetime, timedelta
import requests
import pytz
from io import BytesIO
from PIL import Image, ImageTk

root=Tk()
root.title("Rashi's_Weather Forecasting App")
root.geometry("800x500")
root.resizable(True, True)

from PIL import Image, ImageTk

icon_img = Image.open("C:/Users/admin/OneDrive/Pictures/vecteezy_3d-weather-icon-day-with-rain_24825193__2_-removebg-preview (3).png")
icon_photo = ImageTk.PhotoImage(icon_img)
root.iconphoto(False, icon_photo)


bg_image = Image.open("C:/Users/admin/Downloads/—Pngtree—a stormy sky looms over_16369478.jpeg")
bg_image=bg_image.resize((1500,800))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)
bg_label.image=bg_photo
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#search bar
search_image= Image.open("C:/Users/admin/OneDrive/Pictures/—Pngtree—search bar png and icon_7771045 (1).png")
search_image=search_image.resize((350,45))
search_photo=ImageTk.PhotoImage(search_image)

search_label = Label(root, image=search_photo, bd=0, bg = "dark cyan")

search_label.image=search_photo
search_label.place(relx=0.48, rely=0.2, anchor="center", x=-2)

# Entry box (PNG ke upar overlap kar diya)
search_entry = Entry(root, font=("Aerial", 14,'bold'), width=17, bd=0, relief=FLAT, bg="white", fg="black")
search_entry.place(relx=0.48, rely=0.2, anchor="center", x=-5.6)  # x se thoda left adjust
search_entry.focus()

#Label
label1 =Label(root,text='Temperature',font=("Helvetica",18,'bold'),fg="white",bg="dark cyan")
label1.place(x=225,y=135)
label2=Label(root,text='Humidity',font=("Helvetica",18,'bold'),fg="white",bg="dark cyan")
label2.place(x=225,y=175)
label3 =Label(root,text='Pressure',font=("Helvetica",18,'bold'),fg="white",bg="dark cyan")
label3.place(x=225,y=215)
label4 =Label(root,text='Wind Speed',font=("Helvetica",18,'bold'),fg="white",bg="dark cyan")
label4.place(x=225,y=255)
label5 =Label(root,text='Description',font=("Helvetica",18,'bold'),fg="white",bg="dark cyan")
label5.place(x=225,y=295)

#bottom boxes
firstbox_image = Image.open("C:/Users/admin/OneDrive/Pictures/btm img.jpg")
firstbox_image = firstbox_image.resize((180, 120))
firstbox_photo = ImageTk.PhotoImage(firstbox_image)
firstbox_label = Label(root, image=firstbox_photo, bg="dark cyan")
firstbox_label.image = firstbox_photo
firstbox_label.place(x=20,y=370)

secondbox_image = Image.open("C:/Users/admin/OneDrive/Pictures/btm img.jpg")
secondbox_image = secondbox_image.resize((180, 120))
secondbox_photo = ImageTk.PhotoImage(secondbox_image)
secondbox_label = Label(root, image=secondbox_photo, bg="dark cyan")
secondbox_label.image = secondbox_photo
secondbox_label.place(x=210,y=370)

thirdbox_image = Image.open("C:/Users/admin/OneDrive/Pictures/btm img.jpg")
thirdbox_image = thirdbox_image.resize((180, 120))
thirdbox_photo = ImageTk.PhotoImage(thirdbox_image)
thirdbox_label = Label(root, image=thirdbox_photo, bg="dark cyan")
thirdbox_label.image = thirdbox_photo
thirdbox_label.place(x=400,y=370)

fourthbox_image = Image.open("C:/Users/admin/OneDrive/Pictures/btm img.jpg")
fourthbox_image = fourthbox_image.resize((180, 120))
fourthbox_photo = ImageTk.PhotoImage(fourthbox_image)
fourthbox_label = Label(root, image=fourthbox_photo, bg="dark cyan")
fourthbox_label.image = fourthbox_photo
fourthbox_label.place(x=590,y=370)

# --- Add icons (overlapping on boxes) ---
icon_path = "C:/Users/admin/OneDrive/Pictures/01d@2x.png"

day1 = Label(firstbox_label, text="", font=("Helvetica",12,'bold'), bg="darkcyan", fg="white")
day1.place(x=10, y=2)

day2 = Label(secondbox_label, text="", font=("Helvetica",12,'bold'), bg="darkcyan", fg="white")
day2.place(x=10, y=2)

day3 = Label(thirdbox_label, text="", font=("Helvetica",12,'bold'), bg="darkcyan", fg="white")
day3.place(x=10, y=2)

day4 = Label(fourthbox_label, text="", font=("Helvetica",12,'bold'), bg="darkcyan", fg="white")
day4.place(x=10, y=2)


#days
first=datetime.now()
day1.config(text=first.strftime("%A"))

second=first+timedelta(days=1)
day2.config(text=second.strftime("%A"))

third=first+timedelta(days=2)
day3.config(text=third.strftime("%A"))

fourth=first+timedelta(days=3)
day4.config(text=fourth.strftime("%A"))

#clock
clock_label=Label(root,font=("Helvetica",30,'bold'),fg="cyan",bg="DarkSlategrey",bd=0)
clock_label.place(x=50,y=10)
#timezone
timezone_label=Label(root,font=("Helvetica",20,'bold'),fg="cyan",bg="DarkSlategrey",bd=0)
timezone_label.place(x=510,y=10)

long_lat=Label(root,font=("Helvetica",10,'bold'),fg="cyan",bg="DarkSlategrey",bd=0)
long_lat.place(x=650,y=60)
# Function
# placeholders for icons and temp labels
icon_labels = []
temp_labels = []
for box in [firstbox_label, secondbox_label, thirdbox_label, fourthbox_label]:
    lbl = Label(box, bg="darkcyan")
    lbl.place(x=40, y=20)
    icon_labels.append(lbl)

    temp_lbl = Label(box, font=("Arial", 5, "bold"), fg="white", bg="darkcyan")
    temp_lbl.place(x=58, y=85)
    temp_labels.append(temp_lbl)

def get_weather():
    city = search_entry.get()
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return
    geolocator = Nominatim(user_agent="Rashi_weather_app")
    location = geolocator.geocode(city,timeout=10)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone_label.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 2)}, {round(location.longitude, 2)}")
    
    try:
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock_label.config(text=current_time)
    except:
        clock_label.config(text="_ _:_ _")

    # Current weather
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&units=metric&appid=361fe98d1413d0676c0dd72e43706757"
    json_data = requests.get(api).json()

    label1.config(text=f"Temperature : {json_data['main']['temp']} °C")
    label2.config(text=f"Humidity : {json_data['main']['humidity']} %")
    label3.config(text=f"Pressure : {json_data['main']['pressure']} hPa")
    label4.config(text=f"Wind Speed : {json_data['wind']['speed']} m/s")
    label5.config(text=f"Description : {json_data['weather'][0]['description'].capitalize()}")

    # Forecast
    forecast_api = f"https://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&units=metric&appid=361fe98d1413d0676c0dd72e43706757"
    forecast_data = requests.get(forecast_api).json()

    boxes = [firstbox_label, secondbox_label, thirdbox_label, fourthbox_label]

    # Clear old icons and temps
    for box in boxes:
        for widget in box.winfo_children():
            if widget not in [day1, day2, day3, day4]:
                widget.destroy()

    for i, box in enumerate(boxes):
        # approximate Day = 15:00, Night = 03:00
        day_index = i*8 + 4
        night_index = i*8 + 1
        day_data = forecast_data['list'][day_index]
        night_data = forecast_data['list'][night_index]

        # Day icon
        day_icon_code = day_data['weather'][0]['icon']
        day_icon_url = f"https://openweathermap.org/img/wn/{day_icon_code}@2x.png"
        
        day_icon_img = Image.open(BytesIO(requests.get(day_icon_url).content)).convert("RGBA").resize((40,40), Image.LANCZOS)
        day_icon_photo = ImageTk.PhotoImage(day_icon_img)
        day_icon_label = Label(box, image=day_icon_photo, bg="darkcyan")
        day_icon_label.image = day_icon_photo
        day_icon_label.place(x=20, y=30)

        # Day temp
        day_temp = int(day_data['main']['temp'])
        day_temp_label = Label(box, text=f"Day: {day_temp}°C", font=("Arial", 12, "bold"), fg="white", bg="darkcyan")
        day_temp_label.place(x=70, y=35)

        # Night icon
        night_icon_code = night_data['weather'][0]['icon']
        night_icon_url = f"https://openweathermap.org/img/wn/{night_icon_code}@2x.png"
        night_icon_img = Image.open(BytesIO(requests.get(night_icon_url).content)).convert("RGBA").resize((40,40), Image.LANCZOS)
        night_icon_photo = ImageTk.PhotoImage(night_icon_img)
        night_icon_label = Label(box, image=night_icon_photo, bg="darkcyan")
        night_icon_label.image = night_icon_photo
        night_icon_label.place(x=20, y=75)

        # Night temp
        night_temp = int(night_data['main']['temp'])
        night_temp_label = Label(box, text=f"Night: {night_temp}°C", font=("Arial", 12, "bold"), fg="white", bg="darkcyan")
        night_temp_label.place(x=70, y=80)



search_button = Button(root, text="🔍", font=("Arial", 12),bd=0, bg="darkcyan",command=get_weather)
search_button.place(relx=0.19, rely=0.2, anchor="center", x=80)  # right adjust

def on_enter_press(event):
    get_weather()
search_entry.bind("<Return>",on_enter_press)
root.bind("<Return>", on_enter_press)


root.mainloop()
