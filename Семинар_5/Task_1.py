"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calculations():
    operation = input("Введите операцию: '+', '-', '*', '/' или 0 для выхода:")
    if operation == "0":
        return "Процесс завершен."
    elif operation in "+-*/":
        try:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
            if operation == '+':
                res = num1 + num2
                print(f"Сумма {num1} и {num2} равна: {res}")
                return calculations()
            elif operation == '-':
                res = num1 - num2
                print(f"Разница {num1} и {num2} равна: {res}")
                return calculations()
            elif operation == '*':
                res = num1 * num2
                print(f"Результат умножения {num1} и {num2} равен: {res}")
                return calculations()
            elif operation == '/':
                if num2 == 0:
                    print(
                        "На 0 делить нельзя! выберите другое число. ")
                    return calculations()
                else:
                    res = num1 / num2
                    print(f"Результат деления {num1} и {num2} равен: {res}")
                    return calculations()
        except ValueError():
            print("Вы ввели строку а не число, попробуйте снова. ")
            return calculations()
    else:
        print("Операция не верна. Попробуйте снова")
        return calculations()


calculations()
