from unittest.mock import Mock

import requests

from src.external_api import get_transact_sum

test_data = {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {"amount": "10.0", "currency": {"name": "USD", "code": "USD"}},
}


def test_api():
    test_api_mock = Mock(return_value=" ")
    api_return = test_api_mock
    assert get_transact_sum(test_data) == " "
    test_api_mock.assert_called_once_with("  ")



def test_api_1():
    print(get_transact_sum(test_data))