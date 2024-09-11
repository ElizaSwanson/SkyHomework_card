from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """функция выводит описание ошибки в консоль или записывает ее в текстовый файл"""

    def log_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("\n my function is OK")
                else:
                    print("\n my function is OK")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"\n my function error: {e}, inputs: {args}, {kwargs} \n")
                else:
                    print(f"\n my function error: {e}, inputs: {args}, {kwargs} \n")
            return wrapper

        return wrapper

    return log_decorator
