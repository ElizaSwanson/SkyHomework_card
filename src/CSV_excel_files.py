import pandas as pd


def reading_xls_csv_files(path: str) -> list[dict]:
    """эта функция ищет csv либо excel файлы, считывает их и выводит содержимое"""
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
        return None
