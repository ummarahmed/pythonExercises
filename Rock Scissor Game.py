#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:14:24 2021

@author: ummarahmed
"""

"Exercise # 8"
"Rock Scissors Game"
"""
def playGame():
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")

    p1num = int(input("Player 1 turn: "))
    p2num = int(input("Player 2 turn: "))

    if p1num > p2num:
        print(f"Congratulations {player1}! You Won")
    else:
        print(f"Congratulations {player2}! You Won")


stillWant_to_play = 'y'
while stillWant_to_play == 'y':
    playGame()
    
    stillWant_to_play = input("\n\n Do You want to play again?")


"""

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))

