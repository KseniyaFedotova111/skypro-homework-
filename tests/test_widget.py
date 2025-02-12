from src.widget import mask_account_card, get_date


def test_mask_account_card_with_card_number(card_number_input):
    expected = "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(card_number_input) == expected


def test_mask_account_card_with_account_number(account_number_input):
    expected = "Счет **4305"
    assert mask_account_card(account_number_input) == expected


def test_get_date(date_string_input):
    expected = "2024.03.11"
    assert get_date(date_string_input) == expected
