import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count or not all(isinstance(x, int) for x in sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def __str__(self):
        return self.__about()

    def __len__(self):
        return sum(self.__sides)

    def __about(self):
        return f"Фигура с {self.sides_count} сторонами, цвет {self.__color}, заполнена: {self.filled}"


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_radius(self):
        return self.__radius()

    def get_square(self):
        return math.pi * self.get_radius()**2

    def __about(self):
        return f"Круг с радиусом {self.get_radius()}, площадью {self.get_square()} см², цвет {self.get_color()}, заполнен: {self.filled}"

    def __str__(self):
        return self.__about()


class Triangle(Figure):
    sides_count = 3

    def __is_valid_triangle(self):
        a, b, c = self.get_sides()
        return a + b > c and a + c > b and b + c > a

    def get_square(self):
        if self.__is_valid_triangle():
            a, b, c = self.get_sides()
            p = (a + b + c) / 2
            return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def __about(self):
        return f"Треугольник с площадью {self.get_square()} см², цвет {self.get_color()}, заполнен: {self.filled}"

    def __str__(self):
        return self.__about()


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *(sides * self.sides_count))

    def __side_length(self):
        return self.get_sides()[0]

    def get_square(self):
        return self.__side_length()**2

    def get_volume(self):
        return self.__side_length()**3

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = [new_sides[0]] * self.sides_count
            super().set_sides(*new_sides)

    def __about(self):
        return f"Куб с площадью {self.get_square()} см², объемом {self.get_volume()} см², заполнен: {self.filled}"

    def __str__(self):
        return self.__about()


if __name__ == "__main__":
    # Urban tests
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
