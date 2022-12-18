def find_contact (contact: str):
    file_csv = open('Task044/t_dir.csv', 'r')
    list_csv = file_csv.readlines()
    list_csv = [i.translate({ord(i): None for i in '\n'}) for i in list_csv]
    list_csv = list(tuple(i.split(' - ')) for i in list_csv)
    for i in range (0, len(list_csv)):
        if contact in list_csv[i]:
            file_csv.close()
            return list_csv[i]
    file_csv.close()

    file_txt = open('Task044/t_dir.txt', 'r')
    list_txt = file_txt.readlines()
    list_txt = [i.translate({ord(i): None for i in '\n'}) for i in list_txt]
    list_txt = list(tuple(i.split(' - ')) for i in list_txt)
    for i in range (0, len(list_txt)):
        if contact in list_txt[i]:
            file_txt.close()
            return list_txt[i]
    file_txt.close()

def add_contact(contact):
    with open('Task044/t_dir.txt', 'a+') as file_txt:
        file_txt.write(f'{contact}\n')
    with open('Task044/t_dir.csv', 'a+') as file_csv:
        file_csv.write(f'{contact}\n')
