"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_elem(num_count, n, i=0, num_sum=0):
    if i == num_count:
        print(f'Количество элементов - {num_count}. Их сумма - {num_sum}.')
        return " "
    else:
        i += 1
        num_sum += n
        return sum_elem(num_count, n / 2 * -1, i, num_sum)


try:
    user_input = int(input('Введите количество элементов: '))
    sum_elem(user_input, 1)
except ValueError:
    print('Вы ввели строку а не число, попробуйте снова.')
