from unittest.mock import patch
import pytest
from src.external_api import get_transact_sum


@pytest.fixture
def test_data_1():
    return {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {"amount": "10.0", "currency": {"name": "USD", "code": "USD"}},
    }


@pytest.fixture
def test_data_2():
    return {
        "id": 921286598,
        "state": "EXECUTED",
        "date": "2018-03-09T23:57:37.537412",
        "operationAmount": {"amount": "25780.71", "currency": {"name": "руб.", "code": "RUB"}},
    }


@pytest.fixture
def test_data_3():
    return {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {"amount": "10.0", "currency": {"name": "USD", "code": "USD"}},
    }


@patch("requests.get")
def test_return_amount_trans(mock_get, test_data_1):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 10},
        "info": {"timestamp": 1725124218, "rate": 90.533737},
        "date": "2024-08-31",
        "result": 905.33737,
    }
    assert get_transact_sum(test_data_1) == 905.33737


@patch("requests.get")
def test_rub(mock_get, test_data_2):
    mock_get.return_value.json.return_value = "25780.71"
    assert get_transact_sum(test_data_2) == 25780.71


@patch("requests.get")
def test_return_amount_trans_NONE(mock_get, test_data_3):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 10},
        "info": {"timestamp": 1725124218, "rate": 90.533737},
        "date": "2024-08-31",
    }
    assert get_transact_sum(test_data_3) == None
