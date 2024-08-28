# 1. Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    list_ = [a, b, c]
    print(*list_)


def task_1():
    print_params()
    print_params(b=25)
    print_params(c=[1, 2, 3])


# 2. Распаковка параметров:
def task_2():
    values_list = [2, 'строка', False]
    values_dict = {'a': 3, 'b': 'строка', 'c': None}

    print_params(*values_list)
    print_params(**values_dict)

    print_params(*values_list, **values_dict)


# 3. Распаковка + отдельные параметры:
def task_3():
    values_list_2 = [2, 'строка']
    print_params(*values_list_2, 42)

    values_list_2 = [54.32, 'Строка']
    print_params(*values_list_2, 42)


tasks_list = (task_1, task_2, task_3)
for task in tasks_list:
    try:
        task()
    except:
        print(f'Ошибка внутри функции {task.__name__}')


# Important notice!
# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
# def a(my_list = [])) – это приводит к ошибкам!
#
# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
# def append_to_list(item, list_my=None):
#   if list_my is None:
#    list_my = []
#   list_my.append(item)
# print(list_my)
