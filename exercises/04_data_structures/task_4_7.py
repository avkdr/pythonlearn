# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

mac = "AAAA:BBBB:CCCC"
a = mac.split(':')
b = int(a[0], 16)
c = int(a[1], 16)
d = int(a[2], 16)
result = '{:b}{:b}{:b}'.format(b, c, d)
print(result)