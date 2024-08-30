from unittest.mock import patch

from src.external_api import get_transact_sum

test_data = {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {"amount": "10.0", "currency": {"name": "USD", "code": "USD"}},
}


@patch('requests.get')
def test_return_amount_trans(mock_get):
    mock_get.return_value.json.return_value = {'result': 906.55322}
    assert get_transact_sum(test_data) == 906.55322
    mock_get.assert_called_once()
    mock_get.assert_called_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10.0',
                                headers={'apikey': '6VSAurE9kur7G2761TwmC0bLSLtwQnxu'})
