#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def n_multiply(n):
    list = []
    n_multiply = 1
    for i in range(1, n+1):
        n_multiply *= i
        list.append(n_multiply)
    return list

def print_operation(n):
     list = []
     string = '1'
     list.append(string)
     print(f'({list[0]}, ', end = '')

     for i in range(1, n):
        string += f'*{i+1}'
        list.append(string)
        if i < n-1:
            print(list[i], end = ', ')
        else: 
            print(list[i], end = '')

     print(')')

num = int(input('Введите число: '))
print(n_multiply(num))
print_operation(num)