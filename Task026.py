# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def list_pos(num):
    list = []
    list.append(0)
    list.append(1)
    for i in range(2, num+1):
        list.append(list[i-1] + list[i-2])
    return list

def list_neg(num):
    list = []
    list.append(1)
    list.append(-1)
    num1, num2 = list[0], list[1]
    for i in range(2, num):
        num1, num2 = num2, num1 - num2
        list.append(num2)
    list.reverse()
    return list

def final_list (list_neg, list_pos):
    return list_neg + list_pos

k = 8
res = final_list(list_neg(k), list_pos(k))
print(res)