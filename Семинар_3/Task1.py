"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
"""

n = int(input('Введите номер месяца: '))

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6:
    'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12:
    'Зима'}
try:
    if n in [1, 2, 12]:
        print(f'Месяц {n} относится к времени года {seasons_list[0]}')
    elif n in [3, 4, 5]:
        print(f'Месяц {n} относится к времени года {seasons_list[1]}')
    elif n in [6, 7, 8]:
        print(f'Месяц {n} относится к времени года {seasons_list[2]}')
    elif n in [9, 10, 11]:
        print(f'Месяц {n} относится к времени года {seasons_list[3]}')

    print(f'Месяц {n} относится к времени года {seasons_dict[n]}')
except KeyError:
    print('Вы ввели некорректное значение. Необходимо ввести значение в виде '
          'целого числа от 1 до 12.')
