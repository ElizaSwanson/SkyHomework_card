from typing import Any, Generator


def filter_by_currency(transactions_list: list, code_of_currency: str = "USD") -> Generator[Any, Any, Any]:
    """Функция возвращает итератор с заданной валютой"""
    if len(transactions_list) > 0:
        for transaction in transactions_list:
            if transaction.get("operationAmount").get("currency").get("code") == code_of_currency:
                yield transaction
            elif transaction.get("operationAmount").get("currency").get("code") != code_of_currency:
                raise AssertionError("Такой код не найден")
    if transactions_list == ():
        raise AssertionError("Пустой список")
