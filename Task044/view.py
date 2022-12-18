def input_contact_to_find():
    contact = input('Введите имя или номер телефона: ')
    return contact

def input_contact_to_add():
    contact = input("Введите имя и номер телефона через дефис в формате 'Ivanov Ivan - 9289489': ")
    return contact


def print_result(result):
    print(result)

def choose_action():
    choose = int(input('Чтобы найти контакт, нажмите 0. Чтобы добавить контакт, нажмите 1: '))
    return choose
