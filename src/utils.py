import json

def get_trans_dictionary(file_path: str) -> list:
    """функция выводит список операций"""
    try:
        with open(file_path, 'r', encoding="utf-8") as operations_dict:
            try:
                transactions_info = json.loads(operations_dict)
                return transactions_info
            except json.JSONDecodeError:
                transactions_info = []
                return transactions_info
    except FileNotFoundError:
        transactions_info = []
        return transactions_info