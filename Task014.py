#  Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример :
# абвгдабвгд -> 2
# абв

string1 = input('Введите 1 строку: ')
string2 = input('Введите 2 строку: ')

start = -1
counter = 0
while True:
    start = string1.find(string2, start+1)
    if start == -1:
        break
    counter+=1

print(counter)

# альтернативное решение

if len(string1)>len(string2):
    print(string1.count(string2))
else:
    print(string2.count(string1))