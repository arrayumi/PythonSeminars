# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input('Введите цифру дня недели: '))

if num > 5 and num < 8:
    print('да')
elif num < 8:
    print('нет')
else:
    print('ошибка. введите цифру от 1 до 7')
