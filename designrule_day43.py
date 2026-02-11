#DESIGN RULE FOR DAY 43
All services must follow the same pattern:
Copy code

Return:
    None → no alert
    "message" → alert
Uniform interface = clean scaling.
🧩 STEP 1 — CREATE ISS SERVICE
services/iss_service.py
Python#

import requests
from datetime import datetime

MY_LAT = 28.6
MY_LONG = 77.2

def check_iss():
    try:
        response = requests.get(
            "http://api.open-notify.org/iss-now.json",
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        iss_lat = float(data["iss_position"]["latitude"])
        iss_long = float(data["iss_position"]["longitude"])

        # Check if ISS is near
        near = abs(iss_lat - MY_LAT) < 5 and abs(iss_long - MY_LONG) < 5

        # Check if night
        hour = datetime.now().hour
        is_night = hour < 6 or hour > 18

        if near and is_night:
            return "🌌 ISS is overhead. Go outside and look up."

    except Exception:
        return None

    return None
Notice:
Returns message or None
Handles its own failure
No printing
No sleeping
No logging
That discipline matters.
🧩 STEP 2 — UPDATE SCHEDULER (CLEANLY)
scheduler.py
Replace single service call with list-based approach:
Python
Copy code
import time
import logging
from services.weather_service import check_rain
from services.iss_service import check_iss
from notifiers.console_notifier import notify

SERVICES = [
    check_rain,
    check_iss
]

def run():
    logging.info("Scheduler running")

    for service in SERVICES:
        try:
            alert = service()
            if alert:
                notify(alert)
        except Exception as e:
            logging.error(f"Service failed: {e}")

    time.sleep(600)
#
This is the key improvement:
You no longer hardcode logic per service.
You loop through services generically.
That’s clean engineering.
🧠 WHY THIS IS IMPORTANT
If tomorrow you add:
Stock checker
Price monitor
Habit reminder
You just add:

from services.stock_service import check_stock
SERVICES.append(check_stock)
And nothing else changes.
That’s scalability.
⚠️ DAY 43 COMMON FAILURE
If your scheduler looks like this:#

if check_rain():
    ...
if check_iss():
    ...
if check_stock():
    ...
That is beginner code.
Functional? Yes.
Scalable? No.
The list-based loop is better.