# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# (выбрать 3 любые)
#-----------------------------------------------------------
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N включительно.
# Примеры: - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# 1.
# Реализуйте алгоритм перемешивания списка.
import random
# list = []
# for i in range(0, 10):
#     list.append(random.randint(0, 100))
list = [random.randint(0, 100) for i in range(0,10)]
print(list)
random.shuffle(list)
print(list)

# ---------------------------------------------------------
# 2.
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def create_list(nums_amount, min, max):
    # list = []
    # for i in range(0, nums_amount):
    #     list.append(random.randint(min, max))
    list = [random.randint(min, max) for i in range(0, nums_amount)]
    return list

def sum_not_even_index(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum

new_list = create_list(7, 0, 10)
print(new_list)
print(sum_not_even_index(new_list))

# 3.
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

def create_list(nums_amount: int, min: int, max: int):
    # list = []
    # for i in range(0, nums_amount):
    #     list.append(round(random.randint(min, max), 2))
    list = [round(random.randint(min, max), 2) for i in range (0, nums_amount)]
    return list

def not_repeated_elements(list: list):
    new = []
    for i in range(0, len(list)):
        if list[i] not in new:
            new.append(list[i])
    return new

new_list = create_list(10, 0, 3)
print(f'Сгенерированный список: {new_list}')
sorted_list = not_repeated_elements(new_list)
print(f'Отсортированный список: {sorted_list}')
