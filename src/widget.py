from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """
    Принимает строку, содержащую тип и номер карты или счета, и возвращает строку с замаскированным номером.
    """
    if "Счет" in input_string:
        parts = input_string.split()
        account_number = parts[-1]
        masked_number = get_mask_account(account_number)
        return f"{' '.join(parts[:-1])} {masked_number}"
    else:
        parts = input_string.split()
        card_number = parts[-1]
        masked_number = get_mask_card_number(card_number)
        return f"{' '.join(parts[:-1])} {masked_number}"


card_number_for_mask = "Visa Platinum 7000792289606361"
masked_account_number = "Счет 73654108430135874305"
print(mask_account_card(card_number_for_mask))
print(mask_account_card(masked_account_number))


def get_date(date_string: str) -> str:
    """
    Принимает строку с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ".
    """
    date_part = date_string.split('T')[0]
    day, month, year = date_part.split('-')
    return f"{day}.{month}.{year}"


date_time_string = "2024-03-11T02:26:18.671407"
print(get_date(date_time_string))
