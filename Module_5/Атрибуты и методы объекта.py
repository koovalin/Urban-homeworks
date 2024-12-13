class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.full_name = f"{self.first_name} {self.second_name}"
        self.is_adult = self.age >= 18
        self.all_info = self

    def update_age(self, new_age):
        self.age = new_age
        self.is_adult = self.age >= 18


max = Person("Max", "Milner", 17)
print(max.full_name)
print(max.is_adult)

max.update_age(20)
print(max.is_adult)
