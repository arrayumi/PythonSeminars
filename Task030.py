# Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415
import math

d = list(map(str, input('Задайте точность d в формате 0.001: ')))
digits = len(d)

pi = list(str(2 * math.acos(0.0)))
for i in range (0, digits):
    print(pi[i], end ='')