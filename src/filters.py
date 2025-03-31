import re


def filter_operations(operations, search_string):
    """
    Функция фильтрации операций по строке поиска в описании
    """
    result = []

    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    for operation in operations:
        if 'description' in operation:
            if pattern.search(operation['description']):
                result.append(operation)

    return result


def count_by_categories(operations, categories):
    """
    Функция подсчитывает количество операций в каждой категории
    """
    result = {category: 0 for category in categories}

    for operation in operations:
        if 'description' in operation and operation['description'] in categories:
            result[operation['description']] += 1

    return result
