from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_acc_number: str) -> str | None:
    """это функция для маскировки номеров карт и счетов"""
    numbers = card_acc_number.split()
    number = numbers[-1]
    if card_acc_number.lower().startswith("счет"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    numbers[-1] = masked_number
    return " ".join(numbers)


def get_date(date_input: str) -> str:
    """Преобразование даты"""
    date_not_formated = date_input.split("Т")[0]
    formated_date = f"{date_not_formated[8:10]}.{date_not_formated[5:7]}.{date_not_formated[:4]}"
    return formated_date
