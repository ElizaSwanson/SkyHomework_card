import pandas as pd
import csv


def read_csv(path: str) -> list:
    """функция считывает путь до файла csv и возвращает список транзакций"""
    with open(path, encoding="utf-8") as csv_file:
        transactions_list = []
        python_convert = csv.DictReader(csv_file, delimiter=";")
        for data in python_convert:
            transactions_list.append(data)
    return transactions_list


def read_excel(path: str) -> list:
    """функция считывает путь до файла эксель и возвращает список транзакций"""
    to_py_from_exc = pd.read_excel(path)
    exc_dict = to_py_from_exc.to_dict(orient="records")
    return exc_dict

#print(read_csv("..\\data\\transactions.csv"))
#print(read_excel("..\\data\\transactions_excel.xlsx"))