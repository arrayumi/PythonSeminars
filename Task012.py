# 1'. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

n = int(input('Введите число: '))

res = 1
for i in range(1, n+1):
    print(res, end=' ')
    res = res*(-3)

print()
# решение лучше
for i in range(n):
    print((-3)**i, end=' ')

print()
# еще решение
print([(-3)**n for n in range(n)])