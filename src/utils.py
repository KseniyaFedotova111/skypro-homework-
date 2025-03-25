import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "utils.log"
file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_data(path):
    """
    Загружает данные из JSON-файла и возвращает их в виде списка
    """
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        if data:
            logger.info("Успешно загружены данные из файла")
            return data
        return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {path}")
        return []
