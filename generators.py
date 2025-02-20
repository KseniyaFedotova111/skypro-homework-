from typing import Iterator


def filter_by_currency(lst: list[dict], currency: str = "USD") -> Iterator[dict]:
    """
    Генератор, который возвращает транзакции, где валюта операции соответствует заданной
    """
    for transaction in lst:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873908921,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Maestro 4598300720424501",
        "to": "Счет 43597928997568165086"
    }
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(lst: list[dict]) -> Iterator[dict]:
    """
    Генератор, который возвращает описание каждой операции по очереди
    """
    for transaction in lst:
        yield transaction["description"]


descriptions = transaction_descriptions(transactions)
for _ in range(3):
    print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Iterator[dict]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, stop + 1):
        yield f"{number:016}"[:4] + " " + f"{number:016}"[4:8] + " " + f"{number:016}"[8:12] + " " + f"{number:016}"[
                                                                                                     12:]


for card_number in card_number_generator(1, 5):
    print(card_number)
