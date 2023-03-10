"""
3. Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

products = []
i = 1
while True:
    try:
        name = input('Введите название товара: ')
        price = float(input('Введите цену товара: '))
        amount = float(input('Введите количество товара: '))
        units = input('Введите единицы измерения количества товара: ')
        products.append((i, {'название': name, 'цена': price, 'количество':
            amount, 'eд. измер-я': units}))
        i += 1
    except ValueError:
        print('Допущена ошибка при вводе значений. Повторите ввод данных.')
        continue

    add_item = input('Добавить еще один товар (y/n)?: ')
    if add_item == 'n':
        break

print(f'Список товаров: {products}')

products_dict = dict()
for key in products[0][1].keys():
    temp_list = []
    for i in range(len(products)):
        temp_list.append(products[i][1][key])
    temp_dict = {key: temp_list}
    products_dict.update(temp_dict)

print(f'Справочник по имеющимся товарам: {products_dict}')
