# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['ssss', 'sngujn556', 56] -> Yes ['56', 'sgnbsb'] -> No

list = ['ssss', 'sngujn556', 56]

checker = False
for i in range(0, len(list)):
    if type(list[i]) == int:
        checker = True
        break

print(checker)

# решение преподавателя:

# mass = ['ssss', 'sngujn556', '44']
# types = [str(type(i)) for i in mass]
# if "<class 'int'>" in types or "<class 'float'>" in types:
# print('Yes')
# else:
# print('No')