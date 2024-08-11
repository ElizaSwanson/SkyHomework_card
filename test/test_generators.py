import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_main(transactions):
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == transactions [0]
    assert next(generator) == transactions [1]


@pytest.mark.parametrize('transactions_1, code_of_currency_1, expected', [((), "RUB", "Пустой список")])
def test_filter_by_no_currency(transactions_1, code_of_currency_1, expected):
    generator = filter_by_currency(transactions_1, code_of_currency_1)
    assert generator == expected

def test_desc_transact():
    assert transaction_descriptions(transactions) == ["Перевод организации",
                                                      "Перевод со счета на счет",
                                                      "Перевод с карты на карту"
                                                      "Перевод организации"]


@pytest.mark.parametrize("start, stop, expected", [(28, 29, "0000 0000 0000 0028")])
def test_card_n_generator(start, stop, expected):
    assert next(card_number_generator(start, stop)) == expected