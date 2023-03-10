"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def reverse_num(num, check=0, res=''):
    if num == 0:
        return f'Обратное по порядку число: {res}'
    else:
        check = num % 10
        num = num // 10
        res = res + str(check)
        return reverse_num(num, check, res)


try:
    user_input = int(input('Введите число: '))
    print(f'{reverse_num(user_input)}')
except ValueError:
    print('Вы ввели строку а не число, попробуйте снова: ')
