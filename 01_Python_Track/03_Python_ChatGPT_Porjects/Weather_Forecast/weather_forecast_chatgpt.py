# Improved  (Weather Forecast App) after enhancements with ChatGPT
# Final Project Weather Forecast App

# Import necessary modules for GUI, themes, and HTTP requests
import tkinter as tk
from ttkthemes import ThemedTk
import requests

# OpenWeatherMap API key
API_KEY = "3ddd4f52ba3948414e7ec7bad4ef2ed2"

def fetch_weather():
    """
    Fetch weather data based on the user-provided location.
    """
    try:
        location = location_entry.get()
        validate_location(location)

        reset_variables() # Clear data from screen if user inter invalid city.

        # Construct API request
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": location, "appid": API_KEY, "units": "metric"}
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = response.json()
        update_gui(weather_data)

        clear_error_message() # Clear the old message if the user provides a valid city name.

    except requests.exceptions.RequestException as e:
        handle_request_exception(e)
    except (ValueError, KeyError) as e:
        handle_data_exception(e)

def validate_location(location):
    """
    Validate the user-provided location.
    """
    if not location:
        raise ValueError("Please enter a location.")

def reset_variables():
    """
    Reset GUI variables to empty strings.
    """
    temperature_var.set("")
    humidity_var.set("")
    wind_speed_var.set("")
    pressure_var.set("")
    precipitation_var.set("")

def update_gui(weather_data):
    """
    Update GUI with weather data.
    """
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    pressure = weather_data["main"]["pressure"]

    precipitation = get_precipitation(weather_data)

    temperature_var.set(f"Temperature: {temperature}°C")
    humidity_var.set(f"Humidity: {humidity}%")
    wind_speed_var.set(f"Wind Speed: {wind_speed} km/h")
    pressure_var.set(f"Pressure: {pressure} hPa")
    precipitation_var.set(f"Precipitation: {precipitation} %")

def get_precipitation(weather_data):
    """
    Extract precipitation information from weather data.
    """
    # It seems that precipitation data is not accessible in the free API-KEY in OpenWeatherMap
    precipitation = 0  # Default value

    for condition in ["rain", "snow"]:
        if condition in weather_data and "1h" in weather_data[condition]:
            precipitation = weather_data[condition]["1h"]
            break

    return precipitation

def clear_error_message():
    """
    Clear error message on the GUI.
    """
    error_label.config(text="")

def show_error_message(message):
    """
    Display an error message on the GUI.
    """
    reset_variables()
    error_label.config(text=message, wraplength=500)

def handle_request_exception(exception):
    """
    Handle exceptions related to API requests.
    """
    if "404" in str(exception):
        show_error_message("City not found. Please enter a valid city name.")
    else:
        show_error_message(f"Request Error: {exception}")

def handle_data_exception(exception):
    """
    Handle exceptions related to data processing.
    """
    show_error_message(f"Data Error: {exception}")

# GUI Setup
background_color = "#1c313a"
button_color = "#4CAF50"  # Green

window = ThemedTk(theme="clearlooks")
window.title("Weather Forecast 🌦")
window.configure(bg=background_color)
window.geometry("800x500")
window.minsize(425, 1)  # Set the minimum width to 425 pixels

margin_width = int(window.winfo_reqwidth() * 0.2)

location_label = tk.Label(window, text="Select Location:", bg=background_color, fg="white")
location_label.grid(row=0, column=0, padx=(margin_width, 10), pady=10, sticky="e", columnspan=2)

location_entry = tk.Entry(window)
location_entry.grid(row=0, column=2, padx=10, pady=10, sticky="w", columnspan=2)

fetch_button = tk.Button(window, text="Fetch Weather", command=fetch_weather, bg=button_color, fg="white")
fetch_button.grid(row=1, column=0, padx=(margin_width, 10), pady=10, sticky="w", columnspan=2)

# GUI variables
temperature_var = tk.StringVar()
humidity_var = tk.StringVar()
wind_speed_var = tk.StringVar()
pressure_var = tk.StringVar()
precipitation_var = tk.StringVar()

# Labels and variables for displaying weather information
labels = ["Temperature", "Humidity", "Wind Speed", "Pressure", "Precipitation"]
variables = [temperature_var, humidity_var, wind_speed_var, pressure_var, precipitation_var]

# Create and configure labels for weather information
for i, label_text in enumerate(labels, start=2):
    label = tk.Label(window, textvariable=variables[i-2], bg=background_color, fg="white")
    label.grid(row=i, column=0, padx=(margin_width, 10), pady=10, sticky="w", columnspan=3)

# Error label for displaying error messages
error_label = tk.Label(window, text="", fg="red", bg=background_color, wraplength=500)
error_label.grid(row=6, column=0, columnspan=4, pady=10)

# Label for displaying code authorship
code_label = tk.Label(window, text="</> by Ahmad Tantawy", fg="white", bg=background_color)
code_label.grid(row=7, column=4, sticky="se", padx=10, pady=10)

# Configure row and column weights for proper resizing
for i in range(8):
    window.rowconfigure(i, weight=1)
    window.columnconfigure(i, weight=1)

# Start the GUI event loop
window.mainloop()
