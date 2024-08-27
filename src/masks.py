import logging
import os

path_to_log = "logs/masks.log"
abs_path = os.path.abspath(path_to_log)


logger_masks = logging.getLogger("masks")
masks_handler = logging.FileHandler("../logs/masks.log", "w", encoding="utf-8")
masks_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
masks_handler.setFormatter(masks_formatter)
logger_masks.addHandler(masks_handler)
logger_masks.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str | None:
    """ "эта функция получает номер карты и скрывает часть номера"""
    if card_number.isdigit() and len(card_number) == 16:
        logger_masks.info("Номер карты корректный")
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        logger_masks.warning("Некорректный номер карты")
        return None

print(get_mask_card_number("1234567890123456"))
print(get_mask_card_number("123456789012133456"))

def get_mask_account(acc_number: str) -> str | None:
    """эта функция получает номер банк.счета и возвращает последние 4 цифры"""
    if acc_number.isdigit() and len(acc_number) == 20:
        logger_masks.info("Номер счета верный")
        return f"{'*' * 2}{acc_number[-4:]}"
    else:
        logger_masks.warning("Номер счета некорректный")
        return None

print(get_mask_account("123456789012133456"))
print(get_mask_account("12345678901213345612"))