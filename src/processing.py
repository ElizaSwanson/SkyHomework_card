import re
from collections import Counter
from typing import Any


def filter_by_state(state_dict: list[dict[str, str | Any]], state: str) -> list[dict[str, str | Any]]:
    operations: list = [operation for operation in state_dict if operation.get("state") == state.upper()]
    return operations


def sort_by_date(state_dict: list[dict[str, Any]], reversed_list: bool = True) -> list[dict[str, Any]]:
    """в этой функции происходит сортировка словарей по дате"""
    sorted_list = sorted(
        state_dict,
        key=lambda new_list: new_list["date"],
        reverse=reversed_list,
    )
    return sorted_list


def filter_by_request(transactions_list: list[dict], user_input: str) -> list[dict]:
    """функция поиска по заданному слову"""
    final_list = []
    lower_user_input = user_input.lower()
    for transaction in transactions_list:
        if re.search(lower_user_input, transaction.get("description", ""), flags=re.IGNORECASE):
            final_list.append(transaction)
        else:
            continue
    return final_list


def count_transaction_categories(transactions_list: list[dict]) -> dict:
    """функция подсчета количества операций по конкретным категориям"""
    categories_list = []
    for transaction in transactions_list:
        categories_list.append(transaction["description"])
    counted_categs = dict(Counter(categories_list))
    return counted_categs
