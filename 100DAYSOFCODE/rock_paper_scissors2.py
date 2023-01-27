import random
from enum import Enum


class Winner(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3


options = ['ROCK', 'PAPER', 'SCISSORS']


def decide_winner(player1, player2):
    status = 0
    if player1 in options and player2 in options:
        print(f'Player1 choice is {player1}')
        print(f'player2 choice is {player2}')
        if player1 == player2:
            player1 = Winner.DRAW
            player2 = Winner.DRAW
            print("Game ends in draw")
        elif player1 == 'ROCK' and player2 == 'PAPER':
            player2 = Winner.WIN
            print('player 2 wins')
        elif player1 == 'PAPER' and player2 == 'ROCK':
            player1 = Winner.WIN
            print('player 1 wins')
        elif player1 == 'SCISSORS' and player2 == 'ROCK':
            player2 = Winner.WIN
            print('player 2 wins')
        elif player1 == 'ROCK' and player2 == 'SCISSORS':
            player1 = Winner.WIN
            print('player 1 wins')
        elif player1 == 'PAPER' and player2 == 'SCISSORS':
            player2 = Winner.WIN
            print('player 2 wins')
        elif player1 == 'SCISSORS' and player2 == 'PAPER':
            player1 = Winner.WIN
            print('player 1 wins')
        else:
            print('Enter rock, paper or scissors')


if __name__ == '__main__':
    count1 = 0
    count2 = 0
    while True:
        player1_choice = input('Pick rock, paper, or scissors: ')
        player1_choice = player1_choice.upper()
        count1 += 1
        player2_choice = input('Pick rock, paper, or scissors:')
        player2_choice = player2_choice.upper()
        decide_winner(player1_choice, player2_choice)
        count2 += 1
        if count1 > count2:
            print('player 1 wins')
        elif count2 > count1:
            print('player 2 wins')
        elif count1 and count2 > 3:
            break

