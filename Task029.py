# Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Пример:
# 4, 5 -> 20
# 4,6 -> 12

import math

def find_nod (a,b):
    if a> b:
        max = a
        min = b
    else:
        max = b
        min = a

    while max !=0 and min !=0:
        ost = max%min
        max = min
        min = ost
    return max

# встроенная функция
num_a, num_b = 4, 6
nok = (num_a*num_b)//math.gcd(num_a, num_b)
print(nok)

# моя функция
nok2 = (num_a*num_b)//find_nod(num_a,num_b)
print(nok2)
