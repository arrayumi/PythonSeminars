# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def to_bin(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * (to_bin(num // 2))

num = 45
print(f'Встроенная функция: {bin(num)}')
print(f'Решение по примеру: {to_bin(num)}')
