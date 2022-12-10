# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# *' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

def remove_words(string, word):
    string_list = list(map(str, (string).split()))
    length = len(string_list)
    i = 0
    while i < length:
        if word in string_list[i]:
            string_list.remove(string_list[i])
            length -= 1
        else:
            i += 1
    return ' '.join(string_list)

# или

def remove_words2(string, word):
    string_list = list(map(str, (string).split()))
    for i in string_list:
        if (i.find(word)) !=-1:
            string_list.remove(i)
    return ' '.join(string_list)

strng = 'абвгд гдежз жзе абв ыопыпт'
wrd = 'абв'
print(remove_words(strng, wrd))
print(remove_words2(strng, wrd))

# или
del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])
print(del_st('абвгд гдежз жзе абв ыопыпт', 'абв'))