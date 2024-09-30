def apply_all_func(int_list: list, *functions):
    if not functions:
        raise Exception("Нет функции для работы с числами")

    result = {}
    for function in functions:
        if callable(function):
            try:
                result[function.__name__] = function(int_list)
            except Exception as e:
                result[function.__name__] = f"Ошибка выполнения: {e}"
        else:
            result[str(function)] = "Не является вызываемой функцией"

    return result


# Пример, включающий не вызываемый объект
print(apply_all_func([6, 20, 15, 9], max, "нефункция"))

# Пример использования функции с ошибкой выполнения
print(apply_all_func([6, 20, 15, 9], max, int))

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
