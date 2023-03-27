"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def site_ping(sites):
    for site in sites:
        args = ['ping', site]
        ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in ping.stdout:
            encoding_check = chardet.detect(line)
            print(line.decode(encoding_check['encoding']))


site_ping(['yandex.ru', 'youtube.com'])
