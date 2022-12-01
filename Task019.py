# Реализуйте алгоритм перемешивания списка.
import random

list = []
for i in range(0, 10):
    list.append(random.randint(0, 100))
print(list)

random.shuffle(list)
print(list)