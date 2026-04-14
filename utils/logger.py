import logging
import os
from datetime import datetime


# =========================
# LOG DIRECTORY
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(
    LOG_DIR,
    f"log_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
)

# =========================
# LOGGER
# =========================

logger = logging.getLogger("framework")
logger.setLevel(logging.INFO)

# ❗ КЛЮЧЕВОЕ — отключаем прокидывание в root (иначе pytest выводит в консоль)
logger.propagate = False

# чтобы не дублировались хендлеры
if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


def log_method(method_name: str):
    logger.info("--------------------------------")
    logger.info(f"METHOD {method_name}")
    logger.info("--------------------------------")