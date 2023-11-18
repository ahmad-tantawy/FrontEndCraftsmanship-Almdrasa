# Link for Planning: https://miro.com/app/board/uXjVNPgia48=/?moveToWidget=3458764570243569054&cot=14
# Final Project Weather Forecast App

import tkinter as tk
import requests

API_KEY = "3ddd4f52ba3948414e7ec7bad4ef2ed2"

# Create the main window
window = tk.Tk()
window.title("Weather Forecast")
window.geometry("400x300")

# Widgets for user input
city_label = tk.Label(window, text="Location:")
city_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

city_entry = tk.Entry(window)
city_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

fetch_button = tk.Button(window, text="Fetch Weather", bg="#4CAF50", fg="white")
fetch_button.grid(row=1, column=0, padx=10, pady=10, sticky="w", columnspan=2)

# Variables to hold weather data
temperature_var = tk.StringVar()
humidity_var = tk.StringVar()
wind_speed_var = tk.StringVar()
pressure_var = tk.StringVar()
precipitation_var = tk.StringVar()

labels = ["Temperature", "Humidity", "Wind Speed", "Pressure", "Precipitation"]
variables = [temperature_var, humidity_var, wind_speed_var, pressure_var, precipitation_var]

# Display weather information labels
for i, label_text in enumerate(labels, start=2):
    label = tk.Label(window, textvariable=variables[i-2])
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w", columnspan=2)

error_label = tk.Label(window, text="", fg="red")
error_label.grid(row=7, column=0, columnspan=2, pady=10)

# Set weights for row and column resizing
for i in range(8):
    window.rowconfigure(i, weight=1)
    window.columnconfigure(i, weight=1)

# Function to fetch weather data
def get_weather():
    try:
        clear_data()
        clear_error()  # Clear old error messages

        city = city_entry.get()
        if not city:
            raise ValueError("Enter a city.")

        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = response.json()

        # Display Weather Data
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        pressure = weather_data["main"]["pressure"]

        # It seems that rain data is not accessible in the free API-KEY in OpenWeatherMap
        precipitation = 0
        for condition in ["rain", "snow"]:
            if condition in weather_data and "1h" in weather_data[condition]:
                precipitation = weather_data[condition]["1h"]
                break

        # Update the GUI with the weather information
        temperature_var.set(f"Temp: {temperature}°C")
        humidity_var.set(f"Humidity: {humidity}%")
        wind_speed_var.set(f"Wind: {wind_speed} km/h")
        pressure_var.set(f"Pressure: {pressure} hPa")
        precipitation_var.set(f"Precipitation: {precipitation} %")

    except requests.exceptions.RequestException as e:
        if "404" in str(e):
            show_error("City not found. Enter a valid city.")
        else:
            show_error(f"Request Error: {e}")

    except (ValueError, KeyError) as e:
        show_error(f"Data Error: {e}")

# Function to clear weather data
def clear_data():
    temperature_var.set("")
    humidity_var.set("")
    wind_speed_var.set("")
    pressure_var.set("")
    precipitation_var.set("")

# Function to clear error messages
def clear_error():
    error_label.config(text="")

# Function to display error messages
def show_error(message):
    clear_data()
    error_label.config(text=message)

# Assign the get_weather function to the button click event
fetch_button["command"] = get_weather

# Start the main event loop
window.mainloop()
