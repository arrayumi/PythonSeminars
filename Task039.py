# Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)

import random


def print_matrix(matrix):
    for i in range(3):
        print('|', end="")
        for j in range(3):
            print(matrix[i][j], end=" |")
        print()


def xs_and_os():
    print('Введите имена игроков: ')
    player1 = input('Игрок 1: ')
    player2 = input('Игрок 2: ')
    print('-----')
    player_move = random.choice([player1, player2])
    print(f'Первым ходит {player_move}')

    matrix = []
    for i in range(3):
        a = []
        for j in range(3):
            a.append(' ')
        matrix.append(a)

    OMG_is_this_a_check = True
    count = 0
    while count < 9 and OMG_is_this_a_check:
        num = list(map(int, (input('Введите позицию через пробел: ').split())))
        if matrix[num[0]-1][num[1]-1] == 'x' or matrix[num[0]-1][num[1]-1] == 'o':
            print('Ошибка. Это место уже занято')
        else:
            if player_move == player1:
                matrix[num[0]-1][num[1]-1] = 'x'
            else:
                matrix[num[0]-1][num[1]-1] = 'o'
            print_matrix(matrix)
        # да, мне очень стыдно за эту жесть ниже, когда-нибудь я это перепишу
        if (matrix[0][0] == 'o') and (matrix[0][1] == 'o') and (matrix[0][2] == 'o') or\
           (matrix[1][0] == 'o') and (matrix[1][1] == 'o') and (matrix[1][2] == 'o') or\
           (matrix[2][0] == 'o') and (matrix[2][1] == 'o') and (matrix[2][2] == 'o') or\
           (matrix[0][0] == 'o') and (matrix[1][0] == 'o') and (matrix[2][0] == 'o') or\
           (matrix[0][1] == 'o') and (matrix[1][1] == 'o') and (matrix[2][1] == 'o') or\
           (matrix[0][2] == 'o') and (matrix[1][2] == 'o') and (matrix[2][2] == 'o') or\
           (matrix[0][0] == 'o') and (matrix[1][1] == 'o') and (matrix[2][2] == 'o') or\
           (matrix[0][2] == 'o') and (matrix[1][1] == 'o') and (matrix[2][0] == 'o') or\
           (matrix[0][0] == 'x') and (matrix[0][1] == 'x') and (matrix[0][2] == 'x') or\
           (matrix[1][0] == 'x') and (matrix[1][1] == 'x') and (matrix[1][2] == 'x') or\
           (matrix[2][0] == 'x') and (matrix[2][1] == 'x') and (matrix[2][2] == 'x') or\
           (matrix[0][0] == 'x') and (matrix[1][0] == 'x') and (matrix[2][0] == 'x') or\
           (matrix[0][1] == 'x') and (matrix[1][1] == 'x') and (matrix[2][1] == 'x') or\
           (matrix[0][2] == 'x') and (matrix[1][2] == 'x') and (matrix[2][2] == 'x') or\
           (matrix[0][0] == 'x') and (matrix[1][1] == 'x') and (matrix[2][2] == 'x') or\
           (matrix[0][2] == 'x') and (matrix[1][1] == 'x') and (matrix[2][0] == 'x'):
            OMG_is_this_a_check = False
            print(f'{player_move} WIN!')
            break
        else:
            if player_move == player1:
                player_move = player2
            else:
                player_move = player1
            count += 1
            print(f'Следующий ход - {player_move}!')


xs_and_os()
