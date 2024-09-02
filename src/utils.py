import json
import logging
import os
from typing import Any

path_to_log = "logs/utils.log"
abs_path = os.path.abspath(path_to_log)


logger_utils = logging.getLogger("utils")
masks_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
masks_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
masks_handler.setFormatter(masks_formatter)
logger_utils.addHandler(masks_handler)
logger_utils.setLevel(logging.DEBUG)


def get_trans_dictionary(file_path: str) -> list[Any]:
    """функция выводит список операций"""
    try:
        with open(file_path, "r", encoding="utf-8") as operations_dict:
            try:
                logger_utils.info("Список найден")
                transactions_info = json.load(operations_dict)
                return transactions_info
            except json.JSONDecodeError:
                logger_utils.error("Не удалось декодировать файл")
                transactions_info = []
                return transactions_info
    except FileNotFoundError:
        logger_utils.warning("Файл не найден")
        transactions_info = []
        return transactions_info


print(get_trans_dictionary("..\\data\\operations.json"))
print(get_trans_dictionary("nothing"))
