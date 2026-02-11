import smtplib
import os

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def notify(message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(EMAIL_USER, EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_USER,
                to_addrs=EMAIL_USER,
                msg=f"Subject:Sentinel Alert\n\n{message}"
            )
    except Exception:
        pass