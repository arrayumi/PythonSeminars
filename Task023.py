# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])

import random

def create_list(nums_amount, min, max):
    list = []
    for i in range(0, nums_amount):
        list.append(random.randint(min, max))
    return list

def sum_of_corresponding_elements(list):
    sums_list = []

    if len(list)%2 ==0:
        length = int((len(list)/2))
    else:
        length = int((len(list)/2)+0.5)

    for i in range(0, length):
        sums_list.append(list[i]+list[len(list)-1-i])
    
    return sums_list

new_list = create_list(7, 0, 10)
print(new_list)
print(sum_of_corresponding_elements(new_list))