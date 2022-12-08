# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

from sympy import symplify

with open('Task034-file1.txt', 'r') as file1:
    pol_1 = file1.read()
with open('Task034-file2.txt', 'r') as file2:
    pol_2 = file2.read()

pol_sum = symplify(pol_1 + '+' + pol_2)
pol_sum = str(pol_sum)

print(pol_1)
print(pol_2)
print (pol_sum)

with open('Task034-file-sum.txt', 'w') as file3:
    file3.write(pol_sum)