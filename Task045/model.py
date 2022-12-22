import csv

def find_contact (find):
    with open('Task045/base.csv', 'r') as base:
        list_base = base.readlines()
        list_base = [i.translate({ord(i): None for i in '\n'}) for i in list_base]
        list_base = list(i.split(';') for i in list_base)
        result = []
        check = False
        for i in range (0, len(list_base)):
            for j in list_base[i]:
                if (j.find(find)) !=-1:
                    check = True
                    result.append (' | '.join(list_base[i]))
        return ['\n'.join(result), check]

def add_contact(contact):
    with open('Task045/base.csv', 'a+') as base:
        writer = csv.writer(base, delimiter=';')
        writer.writerows([contact.split(' - ')])

def delete_contact(find):
    with open('Task045/base.csv', 'r') as base:
        old = base.read()
    
    c = find_contact(find)
    c[0] = c[0].replace(' | ', ';')
    new = old.replace(c[0], '')

    with open('Task045/base.csv', 'w') as base:
        base.write(new)

def edit_contact(find, edit):
    with open('Task045/base.csv', 'r') as base:
        old = base.read()
    
    c = find_contact(find)
    c[0] = c[0].replace(' | ', ';')
    new = old.replace(c[0], edit.replace(' - ', ';'))

    with open('Task045/base.csv', 'w') as base:
        base.write(new)


