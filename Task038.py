# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота

import random

def player_vs_player ():
    print('Выбран режим "Игрок против игрока". Введите имена игроков: ')
    player1 = input('Игрок 1: ')
    player2 = input('Игрок 2: ')
    print ('-----')
    player_move = random.choice([player1, player2])
    print(f'Первым ходит {player_move}')
    counter = 117
    while counter > 0:
        number = int(input('Введите число от 1 до 28: '))
        print ('-----')
        if number < 1 or number > 28 or number > counter:
            print(f'Ошибка. {player_move}, попробуй еще раз)')
        else:
            counter -= number
            if counter > 0:
                if player_move == player1:
                    player_move = player2
                else:
                    player_move = player1
                print(f'Осталось конфет: {counter}. Теперь ход {player_move}!')
            else:
                print(f'{player_move} win! Поздравляем!)')

def player_vs_bot():
    counter = 117
    print('Выбран режим "Игрок против компьютера. Ваш ход: ')
    while counter > 0:
        number = int(input('Введите число от 1 до 28: '))
        print ('-----')
        if number < 1 or number > 28 or number > counter:
            print(f'Ошибка. Попробуй еще раз)')
        else:
            counter -= number

        if counter < 0:
            print ('Ура, вы одержали победу над компьютером!')
        else:    
            if counter%29 != 0:
                move = counter%29
                counter -= move
            else:
                move = 1
            if counter > 0:
                print(f'Компьютер взял {move} конфет. Осталось: {counter}.')
                print ('-----')
            else:
                print(f'Компьютер взял {move} конфет и одержал победу!')


mode = input('Выберите режим игры: 1 - игрок против игрока, 2 - игрок против компьютера. :')
print ('-----')
if mode == '1':
    player_vs_player()
else:
    player_vs_bot()