from typing import Any, Generator

import pytest

from test.conftest import transactions

def filter_by_currency(transactions: list, code_of_currency: str = "USD") -> Generator[Any, Any, Any]:
    """Функция возвращает итератор с заданной валютой"""
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == code_of_currency:
            yield transaction
        elif transactions == ():
            return "Пустой список"


def transaction_descriptions(transactions: list) -> Generator[Any, Any, Any]:
    """сортировка по описанию операции"""
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start: int, stop: int) -> Generator[str, Any, Any]:
    """функция для генерации номера карты в заданном промежутке"""
    for number in range(start, stop + 1):
        starting_number = "0000000000000000"
        number_str = str(number)
        card_number = f"{starting_number[: -len(number_str)]}{number_str}"
        gen_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield gen_number
