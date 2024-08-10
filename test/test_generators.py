import pytest

from src.generators import filter_by_currency


def test_filter_by_currency_main(transactions):
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_zero_currency(transactions):
    with pytest.raises(AssertionError):
        assert filter_by_currency(transactions) == "Пустой список"


def test_filter_another_currency(transactions):
    with pytest.raises(AssertionError):
        assert filter_by_currency(transactions, "yen") == "Такой код не найден"
