import csv
import json

import pandas as pd

from src.filters import count_by_categories, filter_operations


def load_data(file_type):
    """
    Загружает данные о транзакциях из выбранного типа файла
    """
    if file_type == "1":
        print("Для обработки выбран JSON-файл")
        with open("transactions.json", "r", encoding="utf-8") as file:
            return json.load(file)
    elif file_type == "2":
        print("Для обработки выбран CSV-файл")
        with open("transactions.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            operations = []
            for row in reader:
                operations.append(row)
            return operations
    elif file_type == "3":
        print("Для обработки выбран XLSX-файл")
        data = pd.read_excel("transactions.xlsx")
        operations = []
        for _, row in data.iterrows():
            operations.append(dict(row))
        return operations
    else:
        print("Неверный выбор типа файла")
        return None


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        file_type = input("Введите номер пункта: ").strip()
        if file_type in ["1", "2", "3"]:
            break
        print("Неверный выбор. Пожалуйста, введите 1, 2 или 3")

    operations = load_data(file_type)
    if not operations:
        print("Не удалось загрузить данные. Завершение программы")
        return

    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию\n"
                       "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip()
        search_string = status.upper()
        filtered_operations = filter_operations(operations, search_string)
        if filtered_operations:
            print(f"Операции отфильтрованы по статусу \"{status.upper()}\"")
            break
        print(f"Статус операции \"{status}\" недоступен")

    if filtered_operations:
        categories = []
        for operation in filtered_operations:
            description = operation.get('description', '').strip()
            if description and description not in categories:
                categories.append(description)

        category_counts = count_by_categories(filtered_operations, categories)
        print("\nПодсчет операций по категориям:")
        for category, count in category_counts.items():
            print(f"Категория: {category}, Количество: {count}")

    sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_choice == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        if sort_order == "по возрастанию":
            filtered_operations.sort(key=lambda x: x.get('date', ''))
        elif sort_order == "по убыванию":
            filtered_operations.sort(key=lambda x: x.get('date', ''), reverse=True)
        else:
            print("Неверный выбор сортировки. Пропускаю сортировку")

    ruble_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if ruble_choice == "да":
        new_filtered_operations = []
        for operation in filtered_operations:
            if operation.get('currency') == 'RUB':
                new_filtered_operations.append(operation)
        filtered_operations = new_filtered_operations

    word_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if word_choice == "да":
        search_word = input("Введите слово для поиска в описании: ").strip()
        filtered_operations = filter_operations(filtered_operations, search_word)

    if not filtered_operations:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("\nРаспечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_operations)}\n")

        for i, operation in enumerate(filtered_operations, start=1):
            date = operation.get('date', 'Дата не указана')[:10]
            description = operation.get('description', 'Описание не указано')
            from_account = operation.get('from', 'Счет отправителя не указан').replace(' ', '')[-4:].rjust(4, '*')
            to_account = operation.get('to', 'Счет получателя не указан').replace(' ', '')[-4:].rjust(4, '*')
            amount = operation.get('amount', 'Сумма не указана')
            currency = operation.get('currency', 'Валюта не указана')

            print(f"{i}. {date} {description}")
            print(f"   {' -> '.join([from_account, to_account])}")
            print(f"   Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
