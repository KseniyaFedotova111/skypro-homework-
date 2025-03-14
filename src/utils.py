import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/utils.log')
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
            logger.info("Возврат списка словарей с данными о финансовых транзакциях")
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден")
        return []
