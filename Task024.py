# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

# т.к. мне не нравится идея решать задачи исключительно через строки и принт,
# то эту задачу решила через списки, чтобы данные можно было в дальнейшем использовать

def create_list(nums_amount, min, max):
    list = []
    for i in range(0, nums_amount):
        list.append(round(random.uniform(min, max), 2))
    return list

def float_to_string (list_float):
    list_string = list(map(str, list_float))
    return list_string

def fract_part_separate(list_string):
    digits_list = []
    for i in range(0, len(list_string)):
        temp_list = list(map(int, list_string[i].split('.')))
        digits_list.append(temp_list[1])
    return digits_list

new_list = create_list(7, 0, 10)
print(f'Сгенерировали список: {new_list}')
string_list = float_to_string(new_list)
print(f'Преобразовали в строчный: {string_list}')
digits = fract_part_separate(string_list)
print(f'Отделили дробную часть: {digits}')
print(f'Ответ: {max(digits)-min(digits)}')