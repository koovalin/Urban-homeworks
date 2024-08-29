from module_6_hard import *


def circle1_test():
    # Тестирование классов
    circle1 = Circle((200, 200, 100), 10)
    print("\n------- ", circle1)
    print(circle1.get_sides())
    print(len(circle1))
    print(circle1.get_color(), "Текущий цвет")

    # Тест изменения
    circle1.set_sides(15)
    circle1.set_color(55, 66, 77)
    print("\n------- Новые данные\n-------", circle1)
    print(circle1.get_sides())
    print(len(circle1))
    print(circle1.get_color(), "Новый цвет")


def cube_test():
    cube1 = Cube((222, 35, 130), 6)
    print("\n------- ", cube1)
    print(cube1.get_sides())
    print(len(cube1))
    print(cube1.get_volume(), "Объем куба")
    print(cube1.get_color(), "Текущий цвет")

    # Тест изменения
    cube1.set_sides(5)
    cube1.set_color(250, 70, 15)
    print("\n------- Новые данные\n------- ", cube1)
    print(cube1.get_sides())
    print(len(cube1))
    print(cube1.get_volume(), "Объем куба")
    print(cube1.get_color())


def triangle_test():
    triangle1 = Triangle((0, 0, 0), 3, 4, 5)
    print("\n------- ", triangle1)
    print(triangle1.get_sides())
    print(len(triangle1))
    print(triangle1.get_color())

    triangle1.set_sides(4, 5, 6)
    triangle1.set_color(10, 243, 128)
    print("\n------- Новые данные\n------- ", triangle1)
    print(triangle1.get_sides())
    print(len(triangle1))
    print(triangle1.get_color())



if __name__ == '__main__':
    circle1_test()
    print()
    cube_test()
    print()
    triangle_test()
    print()
