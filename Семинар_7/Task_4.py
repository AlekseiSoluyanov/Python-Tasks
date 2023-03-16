"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в
виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде. Далее реализовать перегрузку метода add() для реализации
операции сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""

a = [[4, 5, 6], [3, 2, 1], [8, 3, 7]]
b = [[4, 51, 61], [31, 2, 1], [8, 13, 71]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return "\n".join(
            "\t".join([str(itm) for itm in line]) for line in self.lists)

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[i])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return "\n".join(map(str, c))


mtrxA = Matrix(a)
mtrxB = Matrix(b)
print(mtrxA)
print()
print(mtrxB)
print("Сумма матриц:")
print(mtrxA + mtrxB)
