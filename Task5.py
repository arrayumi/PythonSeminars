#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

num = float(input('Введите дробь: '))

first_digit_after_comma = int((num * 10)%10)

if first_digit_after_comma == 0:
    print('нет')
else:
    print(first_digit_after_comma)



