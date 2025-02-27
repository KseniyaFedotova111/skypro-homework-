import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("0000111122223333", "0000 11** **** 3333"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """
    Проверяет, что функция get_mask_card_number корректно маскирует номер карты
    """
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234567890", "**7890"),
        ("9876543210", "**3210"),
        ("0000009999", "**9999"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    """
    Проверяет, что функция get_mask_account корректно маскирует номер счета
    """
    assert get_mask_account(account_number) == expected
