# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def create_list(nums_amount, min, max):
    list = []
    for i in range(0, nums_amount):
        list.append(random.randint(min, max))
    return list

def sum_not_even_index(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum

new_list = create_list(7, 0, 10)
print(new_list)
print(sum_not_even_index(new_list))