class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model

        if self.__is_valid_vin(vin):
            self.__vin = vin

        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


scenarios = [
    ("Model1", 1000000, 'f123dj'),  # Валидный VIN и номер
    ("Model2", "1234567", "abc123"),  # Некорректный тип VIN
    ("Model3", 2020202, "шт123М"),    # Валидный VIN и номер
    ("Model4", 9999999, "a1b2c3"),    # Валидный VIN и номер
    ("Model5", 3050305, "1234567"),   # Неверная длина номера
    ("Model6", 5005000, 'abc12'),     # Неверная длина номера
    ("Model7", 200, 'zxy123'),        # Неверный диапазон VIN
    ("Model8", 1000000, 123456)       # Некорректный тип номера
]

for model, vin, numbers in scenarios:
    try:
        car = Car(model, vin, numbers)
    except IncorrectVinNumber as exc:
        print(f'{model}: {exc.message}')
    except IncorrectCarNumbers as exc:
        print(f'{model}: {exc.message}')
    else:
        print(f'{car.model} успешно создан')
