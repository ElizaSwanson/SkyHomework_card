from unittest.mock import patch

import requests

from src.external_api import get_transact_sum

test_data = {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {"amount": "10.0", "currency": {"name": "USD", "code": "USD"}},
}


@patch("requests.get")
def test_api(mock_get):
    mock_get.return_value.json.return_value = "10.0"
    assert get_transact_sum(test_data) == "10.0"
