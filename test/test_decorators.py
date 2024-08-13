from src.decorators import log
import pytest

def test_log(capsys):
    @log(filename="mylog.txt")
    def my_func(x, y):
        return x + y

    my_func(1,1)