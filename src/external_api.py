import os
from dotenv import load_dotenv
import requests

load_dotenv("../.env")

def get_transact_sum(transactions: dict) -> float:
    code_ = transactions["operationAmount"]["currency"]["code"]
    amount_ = transactions["operationAmount"]["amount"]
    if code_ == "RUB":
        return amount_
    if code_ == "EUR" or "USD":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_}&amount={amount_}"
        api_key = os.getenv("API_KEY")
        headers = {"Api_key": api_key}
        response = requests.request("GET", url, headers=headers)
        result = response.json()
        return result

print(get_transact_sum({
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {
      "amount": "92688.46",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }
})
)