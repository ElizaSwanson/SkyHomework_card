import pytest

from src.widget import mask_account_card
from src.widget import get_date


@pytest.mark.parametrize(
    "user_input, expected", [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("щет 12873895712974912439127648216472189", None),
        ("Счет 64686473678894779589", "Счет **9589")
    ]
)


def test_card(user_input, expected):
    assert mask_account_card(user_input) == expected


@pytest.mark.parametrize(
    "user_input, expected", [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ]
)

def test_data(user_input, expected):
    assert get_date(user_input) == expected