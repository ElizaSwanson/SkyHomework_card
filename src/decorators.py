from functools import wraps
from typing import Callable, Any

def log(filename: str | None = None) -> Callable:
    def log_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                            file.write(f"\n my function is OK")
                else:
                    print(f"\n my function is OK")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"\n my function error: {e}, inputs: {args}, {kwargs} \n")
                else:
                    print(f"\n my function error: {e}, inputs: {args}, {kwargs} \n")
            return result
        return wrapper
    return log_decorator
