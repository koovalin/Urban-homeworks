def calculate_structure_sum(data):
    total_sum = 0
    if isinstance(data, (int, float, bool)):
        return data  # Если аргументы – это число или вещественное число, возвращаем его как есть
    elif type(data) is str:
        return len(data)  # Если аргументы – это строка, возвращаем её длину

    for item in data:  # Если аргументы – это список
        if isinstance(item, (int, float, bool)):  # Если элемент – это число
            total_sum += item
        elif isinstance(item, str):  # Если элемент – это строка
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):  # Если элемент – это список или кортеж
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов
        elif isinstance(item, dict):  # Если элемент – это словарь
            total_sum += calculate_structure_sum(list(item.keys()))  # Суммируем ключи
            total_sum += calculate_structure_sum(list(item.values()))  # Суммируем значения
    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# data_structure = ["5", 5]
result = calculate_structure_sum(data_structure)
print(result)
