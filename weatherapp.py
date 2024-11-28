import tkinter as tk
from tkinter import messagebox
import requests


# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name!")
        return

    # OpenWeatherMap API configuration
    api_key = "3dffbb9654128f09dd2f0faef88b38a1"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Build API request URL
    params = {"q": city, "appid": api_key, "units": "metric"}  # Metric for °C
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Extract relevant data
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display data
        result = (
            f"City: {city_name}, {country}\n"
            f"Temperature: {temp}°C\n"
            f"Weather: {weather_desc.capitalize()}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        result_label.config(text=result)
    else:
        messagebox.showerror("Error", f"Could not retrieve weather data for '{city}'.")
        result_label.config(text="")


# Set up the GUI
app = tk.Tk()
app.title("Weather App")
app.geometry("400x400")
app.resizable(False, False)

# App header
header_label = tk.Label(app, text="Weather App", font=("Papyrus", 16, "bold"))
header_label.pack(pady=10)

# City input
city_label = tk.Label(app, text="Enter City:", font=("Papyrus", 14))
city_label.pack(pady=5)
city_entry = tk.Entry(app, font=("Papyrus", 16), width=25)
city_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(app, text="Get Weather", font=("Papyrus", 12), bg = "pink", command=get_weather)
submit_button.pack(pady=10)

# Result display
result_label = tk.Label(app, text="", font=("Papyrus", 14), justify="left", wraplength=350)
result_label.pack(pady=20)

# Run the app
app.mainloop()
