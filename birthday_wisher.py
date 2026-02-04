import pandas as pd
import smtplib
import datetime as dt
import random
import os

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

birthdays = {
    (row["month"], row["day"]): row
    for _, row in data.iterrows()
}

if today_tuple in birthdays:
    person = birthdays[today_tuple]

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )
