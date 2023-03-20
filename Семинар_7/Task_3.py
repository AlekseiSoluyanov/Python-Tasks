"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
str
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
"""


class Worker:
    name = "Антон"
    surname = "Сергеев"
    position = "Разработчик"
    wage = 25000
    bonus = 10000
    _income = {"Оклад": wage, "Премия": bonus}
    profit = 0


class Position(Worker):
    def get_full_name(self):
        return f"Работник: {self.name} {self.surname}"

    def get_full_profit(self):
        self.profit = self.wage + self.bonus
        return f"Доход с учётом премии: {self.profit}"


w = Worker()
print(w.name)
print(w.surname)
print(w.position)

p = Position()
print(str(p.get_full_profit()) + " " + str(w._income))
