import src.masks


def mask_account_card(card_acc_number: str) -> str:
    """это функция для маскировки номеров карт и счетов"""
    if "Счет" in card_acc_number:
        account_number = card_acc_number[-20:]
        return card_acc_number[:-20] + src.masks.get_mask_account(account_number)
    else:
        card_number = "".join(card_acc_number[-16:].split())
        return card_acc_number[:-16] + src.masks.get_mask_card_number(card_number)