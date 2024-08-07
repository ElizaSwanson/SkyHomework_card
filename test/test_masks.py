import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number

@pytest.mark.parametrize(
    "user_input, expected", [
        ("0", None),
        ("6666111133332222", "6666 11** **** 2222")
    ]
)
def test_card_number(user_input, expected):
    assert get_mask_card_number(user_input) == expected

@pytest.mark.parametrize(
    "user_input_acc, expected_acc", [
        ("362717321313988131322321321131", None),
        ("12345678901234567890", "**7890")
    ]
)

def test_acc_number(user_input_acc, expected_acc):
    assert get_mask_account(user_input_acc) == expected_acc