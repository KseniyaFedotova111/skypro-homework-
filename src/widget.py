from src.masks import get_mask_account, get_mask_card_number
def mask_account_card(input_string: str) -> str:
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


