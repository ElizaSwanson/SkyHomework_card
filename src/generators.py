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


def transaction_descriptions(transactions: list) -> Generator[Any, Any, Any]:
    """сортировка по описанию операции"""
    for description in transactions:
        yield description.get("description")
    if not description:
        raise ValueError("Такой транзакции нет")


def card_number_generator(start: int, stop: int) -> Generator[str, Any, Any]:
    """функция для генерации номера карты в заданном промежутке"""
    for number in range(start, stop + 1):
        starting_number = "0000000000000000"
        number_str = str(number)
        card_number = (f"{starting_number[: -len(number_str)]}{number_str}")
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
