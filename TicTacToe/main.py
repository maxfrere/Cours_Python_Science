#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe Game (Morpion in French)

@Name : T-T-T Game
@Desc : Basic Tic-tac-Toe game

@Author : FRERE Maxime

@Version : A-0.01

@Date : 08-02-2023
"""

import numpy as np

def add_element_on_array(array_2d, coord, value):
    """Will simply add the value argument on the array_2d with the specified coord.

    :param array_2d: The board matrix where the game is.
    :param coord: The coordinate (x,y) where to place value param, will erase old data with no check-up.
    :param value: The value corresponding to the player/bot number.
    :return: The board with the new element added
    """
    array_2d[coord[0],coord[1]]=value
    return array_2d

def ask_for_coordinate(array_2d):
    """Processus to get coordinate frome human
    """
    checker = True
    while checker:
        try:
            str_coord = input("Please give the coordinate in the following format : x,y\n")
            str_coord_x, str_coord_y = str_coord.split(",")
            coord_x, coord_y = int(eval(str_coord_x)),  int(eval(str_coord_y))
            if (coord_x < array_2d.shape[0] and coord_y < array_2d.shape[1]) and array_2d[coord_x,coord_y]==0:
                checker = False
                coord = (coord_x, coord_y)
                print(f"You choose : x={coord[0]} and y={coord[1]} as coordinate.")
            elif (coord_x > array_2d.shape[0] and coord_y > array_2d.shape[1]):
                print(f"Your coordinate are out of bound for a board of {array_2d.shape}")
            elif array_2d[coord_x,coord_y]==0:
                print("This place is already taken !")
                print(array_2d)
            else:
                print("Unknown error")
        except:
            print("!!! An error occurred, please make sure of the format : x,y !!! ")
    return coord

def win_checker(array_2d,value_to_check):
    """Basic boolean check if victory condition is met

    :param array_2d:
    :param value_to_check:
    :return:
    """
    ligne_patern=np.ones(array_2d.shape[0],dtype=np.int8)
    ligne_patern=ligne_patern*value_to_check

    # Cheking for diagonal patern
    if np.array_equal(np.diag(array_2d),ligne_patern) or np.array_equal(np.diag(np.rot90(array_2d)),ligne_patern):
        return True

    # Checking for horizontal and vertical patern
    for idx in range(array_2d.shape[0]):
        if np.array_equal(array_2d[idx,:],ligne_patern):
            return True
        elif np.array_equal(array_2d[:,idx],ligne_patern):
            return True

    return False

def empty_space_checker(array_2d):
    """Boolean checker is empty space are on the array

    :param array_2d:
    :return:
    """
    if 0 in array_2d:
        return True

    return False

def pick_random_coord(array_2d):
    """Choose coordinate between available spot on the array, "Basic IA"

    :param array_2d:
    :return:
    """

    list_coord = np.where(array_2d==0)
    rdm_number = np.random.randint(0,len(list_coord[0]))
    return (list_coord[0][rdm_number],list_coord[1][rdm_number])

def game_loop(nb_player=2,size=3,nb_bot=0):
    """Main loop where all our tool are assembled, set for player vs human, human vs human, IA vs IA (infinite number)

    The array can take all dimension wished

    :param nb_player:
    :param size:
    :param nb_bot:
    :return:
    """
    matrix_game = np.zeros((size,size),dtype=np.int8)
    turn_count = 0
    win_statut = False
    if nb_bot==1 and nb_player==1:
        entity_array = np.arange(2, dtype=np.int8) + int(1)
        if np.random.randint(0,2) == 1 :
            entity_array[0]=2
            entity_array[1]=1
        actual_entity = entity_array[turn_count]
    elif nb_player ==2:
        player_array = np.arange(nb_player,dtype=np.int8)+int(1)
        actual_player = player_array[turn_count]
    elif nb_bot>0:
        bot_array = np.arange(nb_bot, dtype=np.int8) + int(1)
        actual_bot = bot_array[turn_count]


    while not(win_statut):
        # Human vs Human
        if nb_player==2:
            print(f"<=== Round {turn_count} ===>")
            print(f"===> Player {actual_player} <===")
            print(matrix_game)
            if empty_space_checker(matrix_game):
                coord = ask_for_coordinate(matrix_game)
                matrix_game = add_element_on_array(matrix_game, coord, actual_player)
                if win_checker(matrix_game,actual_player):
                    turn_count += 1
                    print(matrix_game)
                    print(f"Player {actual_player} wins at round {turn_count} !")
                    win_statut = True
                else:
                    actual_player = player_array[(turn_count+1)%len(player_array)]
            else:
                print(matrix_game)
                print("It's a draw !")
                win_statut = True
        # IA vs IA
        elif nb_player == 0:
            print(f"<=== Round {turn_count} ===>")
            print(f"===> Player {actual_bot} <===")
            print(matrix_game)
            if empty_space_checker(matrix_game):
                coord = pick_random_coord(matrix_game)
                matrix_game = add_element_on_array(matrix_game, coord, actual_bot)
                if win_checker(matrix_game, actual_bot):
                    turn_count += 1
                    print(matrix_game)
                    print(f"Bot {actual_bot} wins at round {turn_count} !")
                    win_statut = True
                else:
                    actual_bot = bot_array[(turn_count + 1) % len(bot_array)]
            else:
                print(matrix_game)
                print("It's a draw !")
                win_statut = True
        # Human Vs IA
        elif nb_player == 1 and nb_bot==1:
            if actual_entity == 1:
                print(f"<=== Round {turn_count} ===>")
                print(f"===> Player {actual_entity} <===")
                print(matrix_game)
                if empty_space_checker(matrix_game):
                    coord = ask_for_coordinate(matrix_game)
                    matrix_game = add_element_on_array(matrix_game, coord, actual_entity)
                    if win_checker(matrix_game, actual_entity):
                        turn_count += 1
                        print(matrix_game)
                        print(f"Player {actual_entity} wins at round {turn_count} !")
                        win_statut = True
                    else:
                        actual_entity = entity_array[(turn_count+1) % len(entity_array)]
            elif actual_entity == 2:
                print(f"<=== Round {turn_count} ===>")
                print(f"===> Bot {actual_entity} <===")
                print(matrix_game)
                if empty_space_checker(matrix_game):
                    coord = pick_random_coord(matrix_game)
                    matrix_game = add_element_on_array(matrix_game, coord, actual_entity)
                    if win_checker(matrix_game, actual_entity):
                        turn_count += 1
                        print(matrix_game)
                        print(f"Bot {actual_entity} wins at round {turn_count} !")
                        win_statut = True
                    else:
                        actual_entity = entity_array[(turn_count+1) % len(entity_array)]
        else :
            print("This configuration is not yet developed !")
        turn_count+=1

if __name__ == "__main__":
    """Space where we run our algorythm
    """
    game_loop(nb_player=1, size=3, nb_bot=1)