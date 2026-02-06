import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/dp/B0XXXXX"  # example product URL

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-IN,en;q=0.9"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", class_="a-price-whole")

if price:
    price_value = int(price.text.replace(",", ""))
    print(f"Current price: ₹{price_value}")

    if price_value < 30000:
        print("🔥 Price dropped! Buy now.")
else:
    print("Could not find price.")
