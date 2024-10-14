def custom_write(file_name, strings):
    # Создаем пустой словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл для записи с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        # Переменная для отслеживания номера строки
        line_number = 1

        # Проходим по каждой строке из списка
        for string in strings:
            # Получаем текущую позицию в файле
            position = file.tell()

            # Записываем строку в файл с добавлением перевода строки
            file.write(string + '\n')

            # Добавляем в словарь кортеж (номер строки, позиция в байтах) и строку
            strings_positions[(line_number, position)] = string

            # Увеличиваем номер строки
            line_number += 1

    # Возвращаем заполненный словарь
    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

# Вызываем функцию и печатаем результат
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
