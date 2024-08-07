import src.masks


def mask_account_card(card_acc_number: str) -> str | None:
    """это функция для маскировки номеров карт и счетов"""
    if "Счет" in card_acc_number:
        account_number = card_acc_number[-20:]
        return f"{card_acc_number[:-20]}{src.masks.get_mask_account(account_number)}"
    elif "Maestro" in card_acc_number:
        card_number = "".join(card_acc_number[-16:].split())
        return f"{card_acc_number[:-16]}{src.masks.get_mask_card_number(card_number)}"
    elif "Visa" in card_acc_number:
        card_number = "".join(card_acc_number[-16:].split())
        return f"{card_acc_number[:-16]}{src.masks.get_mask_card_number(card_number)}"
    else:
        return None


def get_date(date_input: str) -> str:
    """Преобразование даты"""
    date_not_formated = date_input.split("Т")[0]
    formated_date = f"{date_not_formated[8:10]}.{date_not_formated[5:7]}.{date_not_formated[:4]}"
    return formated_date
