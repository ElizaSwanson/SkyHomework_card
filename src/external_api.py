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
        return amount_
    else:
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_}&amount={amount_float}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        result_ = response.json()
        return result_['result']


test_data = {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {"amount": "10.0", "currency": {"name": "USD", "code": "USD"}},
}

print(get_transact_sum(test_data))