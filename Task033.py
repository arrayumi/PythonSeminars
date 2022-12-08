# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0

import random

def koef_list(num: int):
    list = []
    for i in range(0, num+1):
        list.append(random.randint(0, 101))
    return list

def print_polinom(koef_list: list):
    polinom = ''
    if len(koef_list) < 1:
        polinom = 'x = 0'
    else:
        for i in range(len(koef_list)):
            if len(koef_list)-i-1 == 0:
                polinom += f'{koef_list[i]}'
            elif len(koef_list)-i-1 == 1:
                polinom += f'{koef_list[i]}x'
            else:
                polinom += f'{koef_list[i]}x^{len(koef_list)-i-1}'

            if i != len(koef_list)-1:
                polinom += ' + '
        polinom += ' = 0'
    return polinom

def add_to_file (polinom:str):
    with open('Task033.txt', 'w') as file:
        file.write(f'{polinom}')

k = int(input('Введите натуральную степень: '))
k_list = koef_list(k)
pol = print_polinom(k_list)
print(pol)
add_to_file(pol)

