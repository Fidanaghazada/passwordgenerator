import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import itertools

API_KEY = "bf8cae0d694d727a3d917fb8df1c8faf"

def get_weather():
    city = city_entry.get()
    if not city:
        city = "Baku"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "Could not retrieve weather data"))
            return

        city_name = f"{data['name']}, {data['sys']['country']}"
        temp = f"{data['main']['temp']}°C"
        desc = data['weather'][0]['description'].title()
        icon_code = data['weather'][0]['icon']

        # Hava ikonunu yüklə
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        img_data = Image.open(BytesIO(icon_response.content))
        weather_icon = ImageTk.PhotoImage(img_data)

        # Tkinter etiketlərini yenilə
        city_label.config(text=city_name)
        temp_label.config(text=temp)
        desc_label.config(text=desc)
        icon_label.config(image=weather_icon)
        icon_label.image = weather_icon

        # Hava ikonu animasiyası üçün sadə dövr
        animate_icon(weather_icon)

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        messagebox.showerror("Error", f"Could not retrieve weather data\n{e}")

def animate_icon(icon):
    # Sadə loop animasiya üçün (ikon bəzən titrəyir)
    frames = itertools.cycle([icon])
    def update():
        icon_label.config(image=next(frames))
        root.after(500, update)
    update()

# Tkinter GUI
root = tk.Tk()
root.title("🌤 Weather App 🌤")
root.geometry("400x500")

# Gradient fon yaratmaq üçün Canvas
canvas = tk.Canvas(root, width=400, height=500)
canvas.pack(fill="both", expand=True)
gradient = canvas.create_rectangle(0, 0, 400, 500, fill="#a1c4fd", outline="")

frame = tk.Frame(canvas, bg="#ffffff", bd=3, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=450)

# Şəhər giriş
city_entry = tk.Entry(frame, font=("Helvetica", 16), justify="center")
city_entry.pack(pady=15, padx=10, fill="x")

search_button = tk.Button(frame, text="🔍 Search", font=("Helvetica", 14, "bold"), bg="#4e54c8", fg="white", command=get_weather)
search_button.pack(pady=10)

# Nəticələr üçün etiketlər
city_label = tk.Label(frame, text="", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#2c3e50")
city_label.pack(pady=10)

temp_label = tk.Label(frame, text="", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#e74c3c")
temp_label.pack(pady=5)

desc_label = tk.Label(frame, text="", font=("Helvetica", 16), bg="#ffffff", fg="#2980b9")
desc_label.pack(pady=5)

icon_label = tk.Label(frame, bg="#ffffff")
icon_label.pack(pady=10)

root.mainloop()
