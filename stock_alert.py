import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# ---------------- STOCK DATA ----------------
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(
    "https://www.alphavantage.co/query",
    params=stock_params
)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]

dates = list(data.keys())
yesterday = float(data[dates[0]]["4. close"])
day_before = float(data[dates[1]]["4. close"])

difference = yesterday - day_before
percent = round((difference / day_before) * 100, 2)

# ---------------- CHECK CHANGE ----------------
if abs(percent) > 5:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(
        "https://newsapi.org/v2/everything",
        params=news_params
    )
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]

    client = Client(TWILIO_SID, TWILIO_TOKEN)

    for article in articles:
        message = (
            f"{STOCK}: {percent}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}"
        )

        client.messages.create(
            body=message,
            from_="+123456789",
            to="+91XXXXXXXXXX"
        )
