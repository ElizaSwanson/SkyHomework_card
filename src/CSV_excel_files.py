import pandas as pd
import csv


def reading_xls_csv_files(path: str) -> list[dict]:
    try:
        if ".csv" in path[-4:]:
            data_frame = pd.read_csv(path, delimiter=";")
            result = data_frame.to_dict(orient="records")
            return result
        elif ".xlsx" in path[-5:]:
            data_frame = pd.read_excel(path)
            result = data_frame.to_dict(orient="records")
            return result
    except FileNotFoundError:
        return []

#print(reading_xls_csv_files("..\\data\\transactions.csv"))
print(reading_xls_csv_files("..\\data\\transactions_excel.xlsx"))