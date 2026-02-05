import requests

API_KEY = "YOUR_API_KEY"
LAT = 28.6
LON = 77.2

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)

response.raise_for_status()
weather_data = response.json()

will_rain = False

for forecast in weather_data["list"]:
    condition_code = forecast["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("☔ Bring an umbrella!")
else:
    print("No rain expected.")
