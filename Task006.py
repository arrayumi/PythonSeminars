# Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно ((5 и 10) или 15), но не 30.
# 20 -> Ok 45 -> Ok 150 -> Not Ok

num = int(input())

checker = False
if ((num % 5 == 0 and num % 10 == 0) or (num % 15 == 0)) and (num % 30 != 0):
    checker = True

print(checker)
