from typing import Any, Generator


def filter_by_currency(transactions: list[dict], code_of_currency: str = "USD") -> Generator[Any, Any, Any]:
    """Функция возвращает итератор с заданной валютой"""
    for transaction in transactions:
        try:
            currency_code = transaction["operationAmount"]["currency"]["code"]
        except KeyError:
            continue
        else:
            if currency_code == code_of_currency:
                yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[Any, Any, Any]:
    """сортировка по описанию операции"""
    for transaction in transactions:
        description = transaction["description"]
        yield description


def card_number_generator(start: int, stop: int) -> Generator[str, Any, Any]:
    """функция для генерации номера карты в заданном промежутке"""
    for number in range(start, stop + 1):
        starting_number = "0000000000000000"
        number_str = str(number)
        card_number = f"{starting_number[: -len(number_str)]}{number_str}"
        gen_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield gen_number
