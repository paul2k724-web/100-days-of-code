import time
import logging
from services.weather_service import check_rain
from services.iss_service import check_iss
from notifiers.console_notifier import notify as console_notify
from notifiers.email_notifier import notify as email_notify

SERVICES = [
    check_rain,
    check_iss
]

NOTIFIERS = [
    console_notify,
    email_notify
]

def run():
    logging.info("Scheduler running")

    for service in SERVICES:
        try:
            alert = service()
            if alert:
                for notifier in NOTIFIERS:
                    notifier(alert)
        except Exception as e:
            logging.error(f"Service failed: {e}")

    time.sleep(600)