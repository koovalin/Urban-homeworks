
# Задача:
# Напишите 4 переменных которые буду обозначать следующие данные:
# Количество выполненных ДЗ (запишите значение 12)
# Количество затраченных часов (запишите значение 1.5)
# Название курса (запишите значение 'Python')
# Время на одно задание (вычислить используя 1 и 2 переменные)
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

hw_count = 12
hours_spent = 1.5
course_name = 'Python'
task_time = hours_spent / hw_count
print(f'Курс: {course_name}, всего задач: {hw_count}, затрачено часов: {hours_spent}, среднее время выполнения {task_time:.3f} часа.')
