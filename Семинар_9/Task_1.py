"""
Задание 1.

Реализовать базовый класс Worker (работник),
Реализовать дескриптор
"""


class NonNegative:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    wage = NonNegative()
    bonus = NonNegative()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus

    def __str__(self):
        return str(f'Доход {self.wage} Бонус {self.bonus}')


class Position(Worker):

    def get_full_name(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")


obj = Position("Антон", "Сергеев", "Разработчик", 25000, 10000)
obj.get_full_name()
print(obj)
