# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

n = int(input('Введите число: '))

# простой вариант решения:

# list = []
# for i in range(-n, n+1):
#     list.append(i)

# print(list)

# a_index = int(input('Введите позицию 1-го числа: '))
# b_index = int(input('Введите позицию 2-го числа: '))
# res = list[a_index] * list[b_index]
# print(res)

# -------------------------------------------

with open('Task18.txt', 'w') as file:
    for i in range(-n, n+1):
        file.write(f'{i}\n')

with open('Task18.txt', 'r') as file:
    index_list = file.read().split('\n')
    index_list.remove('')
    index_list = list(map(int, index_list))
print(index_list)

a_index = int(input('Введите позицию 1-го числа: '))
b_index = int(input('Введите позицию 2-го числа: '))

res = index_list[a_index] * index_list[b_index]
print(res)