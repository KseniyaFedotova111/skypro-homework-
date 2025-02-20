import pytest

from generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected_count, expected_ids", [
    ("USD", 2, [939719570, 142264268]),
    ("RUB", 1, [873908921]),
    ("EUR", 0, []),
])
def test_filter_by_currency(transactions, currency, expected_count, expected_ids):
    """
    Проверяет, что функция filter_by_currency корректно фильтрует транзакции по заданной валюте
    """
    filtered = list(filter_by_currency(transactions, currency))
    assert len(filtered) == expected_count
    if expected_count > 0:
        assert [transaction["id"] for transaction in filtered] == expected_ids


def test_filter_by_currency_no_transactions():
    """
    Проверяет, что функция filter_by_currency корректно обрабатывает пустой список транзакций
    """
    filtered = list(filter_by_currency([], "USD"))
    assert len(filtered) == 0


@pytest.mark.parametrize("transactions, expected_descriptions", [
    ([
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"}
    ], ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]),
    ([], [])
])
def test_transaction_descriptions(transactions, expected_descriptions):
    """
    Проверяет, что генератор transaction_descriptions возвращает правильные описания транзакций
    """
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected_descriptions


@pytest.mark.parametrize("start, stop, expected_numbers", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]),
    (10, 10, ["0000 0000 0000 0010"]),
    (1, 0, [])
])
def test_card_number_generator(start, stop, expected_numbers):
    """
    Проверяет, что генератор card_number_generator возвращает правильные номера карт
    """
    card_numbers = list(card_number_generator(start, stop))
    assert card_numbers == expected_numbers
