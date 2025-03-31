import logging

logger = logging.getLogger("masks")

file_handler = logging.FileHandler("masks.log", mode="a", encoding="utf-8")

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX
    """
    try:
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        logger.info(f"Успешно создана маска для номера карты: {masked_card_number}")
        return masked_card_number
    except Exception as e:
        logger.error(f"Ошибка при создании маски для номера карты: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """
    Принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате **XXXX
    """
    try:
        masked_account_number = f"**{account_number[-4:]}"
        logger.info(f"Успешно создана маска для номера счета: {masked_account_number}")
        return masked_account_number
    except Exception as e:
        logger.error(f"Ошибка при создании маски для номера счета: {e}")
        raise
