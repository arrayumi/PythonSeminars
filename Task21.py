# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def check_2nd_entering(list, find):
    index = -1
    counter = 0
    for i in range(0, len(list)):
        if list[i] == find:
            counter += 1
        if counter == 2:
            index = i
            break
    return index


list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find1 = 'qwe'
print(list1, find1)
print(check_2nd_entering(list1, find1))

list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
find2 = "йцу"
print(list2, find2)
print(check_2nd_entering(list2, find2))

list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
find3 = "йцу"
print(list3, find3)
print(check_2nd_entering(list3, find3))

# решение преподавателя:

# mass = ["123", "234", 123, "567"]
# a = 123

# try:
# mass.remove(a)
# print((mass.index(a))+1)
# except ValueError:
# print(-1)