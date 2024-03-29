"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = (('Красный', 5), ('Жёлтый', 2), ('Зеленый', 4))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(Ждите {} секунд)'.format(sec))
            sleep(sec)


traffic_light = TrafficLight()
traffic_light.running()
