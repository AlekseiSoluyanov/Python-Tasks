"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input('Введите число n: '))
temp = str(n)
n2 = temp + temp
n3 = temp + temp + temp
result = n + int(n2) + int(n3)
print('Результат равен: ', result)