import time
import functools
import allure
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

def retry(times=3, delay=0.5, step_name=None):
    """
    Универсальный декоратор retry для методов страниц.
   
    :param times: сколько раз повторять
    :param delay: пауза между попытками
    :param step_name: название шага для Allure (если не указано, берётся имя метода)
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            method_name = func.__name__
            step = step_name or method_name


            for attempt in range(1, times + 1):
                try:
                    with allure.step(f"{step} (Attempt {attempt}/{times})"):
                        return func(*args, **kwargs)
                except (TimeoutException, StaleElementReferenceException) as e:
                    last_exception = e
                    time.sleep(delay)
            # Если все попытки не удались
            raise AssertionError(
                f"Метод '{method_name}' не удался после {times} попыток. "
                f"Ошибка: {type(last_exception).__name__}\n"
                f"Детали: {repr(last_exception)}"
            )
        return wrapper
    return decorator
