import src.masks


def mask_account_card(card_acc_number: str) -> str:
    """это функция для маскировки номеров карт и счетов"""
    if "Счет" in card_acc_number:
        account_number = card_acc_number[-20:]
        return f"{card_acc_number[:-20]} {src.masks.get_mask_account(account_number)}"
    else:
        card_number = "".join(card_acc_number[-16:].split())
        return f"{card_acc_number[:-16]} {src.masks.get_mask_card_number(card_number)}"


def get_date(date_input: str) -> str | None:
    """Преобразование даты"""
    date_not_formated = date_input.split("Т")[0]
    formated_date = f"{date_not_formated[-2:]}.{date_not_formated[5:7]}.{date_not_formated[:4]}"
    return formated_date
