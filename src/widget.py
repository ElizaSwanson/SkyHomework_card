import src.masks


def mask_account_card(card_acc_number: str) -> str:
    """это функция для маскировки номеров карт и счетов"""
    if "Счет" in card_acc_number:
        account_number = card_acc_number[-20:]
        return f"{card_acc_number[:-20]} {src.masks.get_mask_account(account_number)}"
    else:
        card_number = "".join(card_acc_number[-16:].split())
        return f"{card_acc_number[:-16]} {src.masks.get_mask_card_number(card_number)}"


def get_data(data_input: str) -> str | None:
    """Преобразование даты"""
    data_ = data_input.split("Т")[0]
    formated_data = f"{data_[-2:]}.{data_[5:7]}.{data_[:4]}"
    return formated_data
