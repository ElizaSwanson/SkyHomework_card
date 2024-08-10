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
    assert next(desc_) == "Перевод организации"
    assert next(desc_) == "Перевод со счета на счет"


def test_card_n_generator():
    num_ = card_number_generator(781377451, 17387851031)
    assert next(num_) == "0000 0007 8137 7451"
