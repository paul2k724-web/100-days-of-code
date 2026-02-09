import requests
import os

LAT = 28.6
LON = 77.2
API_KEY = os.getenv("WEATHER_API_KEY")

def check_rain():
    params = {
        "lat": LAT,
        "lon": LON,
        "appid": API_KEY,
        "cnt": 4
    }

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/forecast",
        params=params,
        timeout=10
    )
    response.raise_for_status()

    data = response.json()

    for item in data["list"]:
        condition_id = item["weather"][0]["id"]
        if condition_id < 700:
            return "☔ Rain expected. Carry an umbrella."

    return None