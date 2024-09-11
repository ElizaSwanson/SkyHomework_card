from src.decorators import log


def test_log(capsys):
    @log(filename="mylog.txt")
    def my_func(x, y):
        return x + y

    my_func(1, 1)


def test_log_not_OK(capsys):
    @log(filename="mylog.txt")
    def my_func_1(x, y):
        return x + y == 11

    my_func_1(9)


def test_log_NO_filename(capsys):
    @log()
    def my_func(x, y):
        return x + y

    my_func(1, 3)


def test_log_filename_NOT_OK(capsys):
    @log()
    def my_func(x, y):
        return x + y == 0

    my_func(1)
