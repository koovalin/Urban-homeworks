def calculate_structure_sum(*args):
    total_sum = 0

    for item in args:
        if isinstance(item, (int, float, bool)):  # Если элемент – это число
            total_sum += item
        elif isinstance(item, str):  # Если элемент – это строка
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):  # Если элемент – это список или кортеж
            total_sum += calculate_structure_sum(*item)  # Рекурсивный вызов
        elif isinstance(item, dict):  # Если элемент – это словарь
            total_sum += calculate_structure_sum(*item.keys())  # Суммируем ключи
            total_sum += calculate_structure_sum(*item.values())  # Суммируем значения

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)
