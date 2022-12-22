def choose_mode():
    mode = input('Выберите режим:\n' +
                 '1 - найти контакт\n' +
                 '2 - добавить контакт\n' +
                 '3 - удалить контакт\n' +
                 '4 - редактировать контакт\n')
    return mode

def input_contact_to_find():
    find = input('Введите любые данные пользователя: ')
    return find

def contact_not_found():
    print('Пользователь не найден')

def input_contact_to_add():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    number = input('Введите номер телефона: ')
    position = input('Введите должность: ')
    email = input('Введите email: ')
    contact = [name + ' ' + surname, number, position, email]
    return ' - '.join(contact)

def contact_added ():
    print('\nКонтакт добавлен')

def print_result(result):
    print(f'\nНайдены пользователи:\n{result}')

def delete_request():
    request = input('\nУдалить пользователя? (да/нет)')
    return request

def input_contact_to_delete ():
    find = input('\nЧтобы удалить сотрудника из базы, введите его имя: ')
    return find

def contact_deleted ():
    print('\nДанные сотрудника удалены')

def input_contact_to_edit():
    edit = input('\nЧтобы внести изменения в данные сотрудника, введите его имя: ')
    return edit

def edit_request():
    request = input('\nВнести изменения? (да/нет)')
    return request

def contact_edited():
    print('\nДанные сотрудника изменены')

def mode_error():
    print('Ошибка. Вводимое число должно быть от 1 до 4.')