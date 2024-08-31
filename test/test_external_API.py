from unittest.mock import patch

from src.external_api import get_transact_sum

test_data = {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {"amount": "10.0", "currency": {"name": "USD", "code": "USD"}},
}


@patch("requests.get")
def test_return_amount_trans(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 10},
        "info": {"timestamp": 1725124218, "rate": 90.533737},
        "date": "2024-08-31",
        "result": 905.33737,
    }
    assert get_transact_sum(test_data) == 905.33737
