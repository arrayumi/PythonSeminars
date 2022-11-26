# Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.

# max = int(input())

# for i in range(4):
#     num = int(input())
#     if num > max:
#        max = num
# print(max)

#решение через сплит

a = list(map(int, input().split()))
print(max(a))
