import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_main(transactions):
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == transactions[0]
    assert next(generator) == transactions[1]


def test_desc_transact(transactions):
    result = transaction_descriptions(transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"


@pytest.mark.parametrize("start, stop, expected", [(28, 29, "0000 0000 0000 0028")])
def test_card_n_generator(start, stop, expected):
    assert next(card_number_generator(start, stop)) == expected
