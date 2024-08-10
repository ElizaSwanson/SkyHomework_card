import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_main(transactions):
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == transactions[0]
    assert next(generator) == transactions[1]


def test_filter_by_zero_currency(transactions):
    with pytest.raises(AssertionError):
        assert filter_by_currency(transactions) == "Пустой список"


def test_filter_another_currency(transactions):
    with pytest.raises(AssertionError):
        assert filter_by_currency(transactions, "yen") == "Такой код не найден"


def test_desc_transact(transactions):
    desc_ = transaction_descriptions(transactions)
    for i in range(4):
        print(next(desc_))


def test_card_n_generator():
    for card_num in card_number_generator(1, 5):
        print(next(card_num))