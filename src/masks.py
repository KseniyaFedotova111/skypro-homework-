def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX
    """
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_card_number


card_number_for_mask = "7000792289606361"
print(get_mask_card_number(card_number_for_mask))


def get_mask_account(account_number: str) -> str:
    """
     Принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате **XXXX
    """
    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number


account_number_for_mask = "73654108430135874305"
print(get_mask_account(account_number_for_mask))
