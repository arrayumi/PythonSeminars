# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def increased_sequence (list: list):
    res = []
    res.append(list[0])
    temp = list[0]
    for i in range(1, len(list)-1):
        if list[i] > temp and list[i] < list[i+1]: 
            res.append(list[i])                    
            temp = list[i]                           
    if list[-1] > res[-1]:
        res.append(list[-1])
    return res

lst = [1, 5, 2, 3, 4, 6, 1, 7]
print(increased_sequence(lst))