# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
print('Введите координаты точки A')
ax = int(input('X: '))
ay = int(input('Y: '))

print('Введите координаты точки B')
bx = int(input('X: '))
by = int(input('Y: '))

result = math.sqrt((bx-ax)**2 + (by-ay)**2)
print(result)


res = ((ax - bx)**2 + (ay - by)**2)**0.5
print(res)