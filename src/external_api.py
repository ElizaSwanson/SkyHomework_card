import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transact_sum(transactions: dict) -> float:
    """функция конвертирует сумму операций в рубли"""
    code_ = transactions["operationAmount"]["currency"]["code"]
    amount_ = transactions["operationAmount"]["amount"]
    amount_float = float(amount_)
    if code_ == "RUB":
        return amount_float
    else:
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_}&amount={amount_float}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        result_ = response.json()
        if "result" in result_:
            return result_["result"]
        else:
            return None
