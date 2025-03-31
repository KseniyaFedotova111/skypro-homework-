import pytest

from src.filters import count_by_categories, filter_operations


@pytest.mark.parametrize("search_string, expected", [
    ("перевод", [
        {"id": 1, "description": "Перевод на счет друга"},
        {"id": 5, "description": "Перевод зарплаты"}
    ]),
    ("вклад", []),
    ("оплата", [
        {"id": 2, "description": "Оплата интернета"},
        {"id": 4, "description": "Оплата коммунальных услуг"}
    ]),
    ("покупка", [
        {"id": 3, "description": "Покупка товаров в магазине"}
    ]),
    ("ничего", [])
])
def test_filter_operations(sample_operations, search_string, expected):
    """
    Тестирует функцию filter_operations на множестве различных входных данных
    """
    result = filter_operations(sample_operations, search_string)
    assert result == expected


# Параметризованный тест для count_by_categories
@pytest.mark.parametrize("categories, expected", [
    (["Перевод на счет друга", "Оплата интернета", "Оплата коммунальных услуг"], {
        "Перевод на счет друга": 1,
        "Оплата интернета": 1,
        "Оплата коммунальных услуг": 1
    }),
    (["Взнос наличных", "Открытие вклада"], {
        "Взнос наличных": 0,
        "Открытие вклада": 0
    }),
    (["Перевод на счет друга", "Оплата несуществующей услуги"], {
        "Перевод на счет друга": 1,
        "Оплата несуществующей услуги": 0
    }),
    ([], {}),
    (["Описание отсутствует"], {"Описание отсутствует": 0})
])
def test_count_by_categories(sample_operations, categories, expected):
    """
    Тестирует функцию count_by_categories на множестве различных входных данных
    """
    result = count_by_categories(sample_operations, categories)
    assert result == expected
