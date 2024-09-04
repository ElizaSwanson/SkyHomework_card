import os

from processing import filter_by_request, filter_by_state, sort_by_date
from src.CSV_excel_files import get_transactions_csv, get_transactions_excel
from src.generators import filter_by_currency
from src.utils import get_trans_dictionary
from src.widget import get_date, mask_account_card

PATH_TO_FILE_JSON = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def main():
    """основная функция, осуществляющая фильтрацию операций по заданным параметрам"""

    while True:
        main_menu = input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями
        Выберите необходимый пункт меню
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
        )
        if main_menu == "1":
            print("Для обработки выбран JSON-файл.")
            transactions_reading = get_trans_dictionary(PATH_TO_FILE_JSON)
            break
        elif main_menu == "2":
            print("Для обработки выбран CSV-файл.")
            transactions_reading = get_transactions_csv(PATH_TO_FILE_CSV)
            break
        elif main_menu == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions_reading = get_transactions_excel(PATH_TO_FILE_EXCEL)
            break
        else:
            print("Такого пункта в меню нет")

    state_list = ["executed", "canceled", "pending"]

    while True:
        state_choose = input(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        ).lower()
        if state_choose not in state_list:
            print("Такого статуса нет")
        else:
            break

    filtered_operations = filter_by_state(transactions_reading, state_choose)

    sort_date = input("Отсортировать операции по дате? Да/Нет").lower()

    if sort_date == "да":
        reverse_or_not = input("Отсортировать по убыванию или возрастанию?").lower()
        if reverse_or_not == "по возрастанию":
            reverse_choose = False
        elif reverse_or_not == "по убыванию":
            reverse_choose = True
        else:
            reverse_choose = False
            print("Произведена сортировка по умолчанию")
        filtered_operations = sort_by_date(filtered_operations, reverse_choose)

    filter_RUB = input("Выводить только рублевые транзакции? Да/нет").lower()
    if filter_RUB == "да":
        rub_filter = filter_by_currency(filtered_operations, "RUB")
        filtered_operations = list(rub_filter)

    filter_specific_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
    if filter_specific_word == "да":
        specific_word = input("Введите слово: ")
        filtered_operations = filter_by_request(filtered_operations, specific_word)


    print("Распечатываю итоговый список транзакций...")
    if len(filtered_operations) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_operations)}")
        for data in filtered_operations:
            trans_date = get_date(data["date"])
            currency = data["operationAmount"]["currency"]["code"]
            if data["description"] == "Открытие вклада":
                acc_num = mask_account_card(data["to"])
            else:
                acc_num = f"{mask_account_card(data["from"])} -> {mask_account_card(data["to"])}"
            amount_op = data["operationAmount"]["amount"]
            print(
                f"""{trans_date} {data["description"]}
{acc_num}
Сумма: {round(float(amount_op))} {currency}"""
            )


if __name__ == '__main__':
    main()