"""
Задание 2.
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def type_check(arr):
    for word in arr:
        print(f'Содержимое: {word}')
        print(f'Тип: {type(word)}')
        print(f'Длина: {len(word)}')


type_check([b'class', b"function", b"method"])
