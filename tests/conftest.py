import pytest


@pytest.fixture
def sample_data() -> list[dict[str, str | int]]:
    """
    Фикстура, возвращающая тестовые данные в виде списка словарей.
    Каждый словарь содержит ключи: id (int), state (str), date (str).
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def card_number() -> str:
    """
    Фикстура, возвращающая тестовый номер карты в виде строки.
    """
    return "1234567812345678"


@pytest.fixture
def account_number() -> str:
    """
    Фикстура, возвращающая тестовый номер счета в виде строки.
    """
    return "1234567890"


@pytest.fixture
def card_number_input() -> str:
    """
    Фикстура, возвращающая тестовый номер карты с описанием в виде строки.
    """
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account_number_input() -> str:
    """
    Фикстура, возвращающая тестовый номер счета с описанием в виде строки.
    """
    return "Счет 73654108430135874305"


@pytest.fixture
def date_string_input() -> str:
    """
    Фикстура, возвращающая тестовую дату в виде строки.
    """
    return "2024-03-11T02:26:18.671407"
