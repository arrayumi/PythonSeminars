# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

str_list = list(input('Введите числа через пробел: ').split())
num_list = list(map(int, str_list))
print(num_list)
print(f'{max(num_list)} - большее число, {min(num_list)} - меньшее число')