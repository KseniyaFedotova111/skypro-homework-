import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card(input_string: str, expected: str) -> None:
    """
    Проверяет, что функция mask_account_card корректно маскирует номер карты или счета
    """
    assert mask_account_card(input_string) == expected


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2020-02-29T00:00:00.000000", "29.02.2020"),
    ],
)
def test_get_date(date_string: str, expected: str) -> None:
    """
    Проверяет, что функция get_date корректно форматирует дату
    """
    assert get_date(date_string) == expected
