from unittest.mock import patch

from src.CSV_excel_files import reading_xls_csv_files


@patch("src.CSV_excel_files.pd.read_csv")
def test_reading_csv(mock_read, test_data_frame):
    mock_read.return_value = test_data_frame
    result = reading_xls_csv_files("..\\data\\transactions.csv")
    expected = test_data_frame.to_dict(orient="records")
    assert result == expected


def test_zero():
    assert reading_xls_csv_files("") == []


@patch("src.CSV_excel_files.pd.read_excel")
def test_excel_reading(mock_read, test_excel):
    mock_read.return_value = test_excel
    result = reading_xls_csv_files("..\\data\\transactions_excel.xlsx")
    expected = test_excel.to_dict(orient="records")
    assert result == expected
