import requests
import os
from datetime import datetime

# ---------- USER INPUT ----------
exercise_text = input("Tell me which exercises you did: ")

# ---------- NUTRITIONIX ----------
nutritionix_headers = {
    "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
    "x-app-key": os.getenv("NUTRITIONIX_API_KEY"),
}

nutritionix_body = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 175,
    "age": 25
}

response = requests.post(
    "https://trackapi.nutritionix.com/v2/natural/exercise",
    json=nutritionix_body,
    headers=nutritionix_headers
)
response.raise_for_status()
result = response.json()

# ---------- DATE & TIME ----------
today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")

# ---------- SHEETY ----------
sheety_headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
}

sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

for exercise in result["exercises"]:
    sheety_data = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(
        sheety_endpoint,
        json=sheety_data,
        headers=sheety_headers
    )
    response.raise_for_status()

print("✅ Workout logged successfully!")
