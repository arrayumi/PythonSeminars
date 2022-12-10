# Задано N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.
# *' 1 2 3 4 6 7 -> 5
# *' 1 3 -> 2

def find_missing_num (list):
    for i in range(1,len(list)):
        if list[i] - 1 != list[i-1]:
            return list[i]-1


num_list = list(map(int, ('1 2 3 4 6 7').split()))
print(num_list)
print(find_missing_num(num_list))