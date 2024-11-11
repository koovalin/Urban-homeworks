from pprint import pprint


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj)

    # Получаем список всех атрибутов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем список всех методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Получаем модуль, к которому принадлежит объект
    module = obj.__class__.__module__

    # Опционно: выводим другие интересные свойства объекта
    properties = {}
    if hasattr(obj, '__doc__'):
        properties['doc'] = obj.__doc__
    if hasattr(obj, '__name__'):
        properties['name'] = obj.__name__

    # Формируем словарь с собранной информацией
    info = {
        'type'            : obj_type.__name__,
        'attributes'      : attributes,
        'methods'         : methods,
        'module'          : module,
        'other_properties': properties
    }

    return info


# Пример использования
class ExampleClass:
    """Пример пользовательского класса"""

    def __init__(self, value):
        self.value = value

    def example_method(self):
        return f"Value is {self.value}"


# Инстанцируем объект
example_obj = ExampleClass(42)
number_info = introspection_info(example_obj)
pprint(number_info)
