# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def digits_sum(list):
    res = 0
    for i in range(len(list)):
        while list[i] > 0:
            res += list[i] % 10
            list[i] //= 10
    return res


num = input('Введите вещественное число: ')
num_list = list(map(int, num.split('.')))

print(digits_sum(num_list))
