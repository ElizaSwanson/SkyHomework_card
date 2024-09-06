from src.utils import get_trans_dictionary


def test_empty():
    assert get_trans_dictionary("") == []


def test_incorrect_path():
    assert get_trans_dictionary(file_path="src.enc") == []


def test():
    print(get_trans_dictionary("..\\data\\operations.json"))
