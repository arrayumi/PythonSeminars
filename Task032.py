# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

def create_list(nums_amount: int, min: int, max: int):
    list = []
    for i in range(0, nums_amount):
        list.append(round(random.randint(min, max), 2))
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