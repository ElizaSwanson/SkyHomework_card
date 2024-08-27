import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("API_KEY")


def get_transact_sum(transactions: dict) -> float:
    """функция конвертирует сумму операций в рубли"""
    code_ = transactions["operationAmount"]["currency"]["code"]
    amount_ = transactions["operationAmount"]["amount"]
    if code_ == "RUB":
        return amount_
    if code_ == "EUR" or "USD":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_}&amount={amount_}"
        headers = {"Api_key": api_key}
        response = requests.get(url, headers=headers)
        result = response.json()
        return result
