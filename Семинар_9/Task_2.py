"""
Задание 2.

Реализовать метакласс. позволяющий создавать всегда один и тот же объект класса
"""


class TestMeta(type):
    example = None

    def __call__(cls):
        if cls.example is None:
            cls.example = super().__call__()
        return cls.example


class MyClass(metaclass=TestMeta):
    pass


ob_1 = MyClass()
ob_2 = MyClass()
ob_3 = MyClass()

print(ob_1 is ob_2)
print(ob_2 is ob_3)
print(ob_3 is ob_1)
