import json

def get_trans_dictionary():
    try:
        with open("operations.json") as operations_dict:
            try:
                transactions_info = json.loads(operations_dict)
                return transactions_info
            except json.JSONDecodeError:
                transactions_info = []
                return transactions_info
    except FileNotFoundError:
        transactions_info = []
        return transactions_info