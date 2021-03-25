#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:50:05 2021

@author: ummarahmed
"""

"Guessing Game One"
"Exercise # 9"
import random


def randomGame():
    rnum = random.randint(1, 9)

    unum = int(input("Guess the number: "))

    if unum > rnum:
        if (unum - rnum) < 3:
            print("You are very close.")
        elif (unum - rnum) > 3:
            print("You are too high")
    elif rnum > unum:
        if (rnum - unum) < 3:
            print("You are very close.")
        elif (rnum - unum) > 3:
            print("You are too low")
    elif rnum == unum:
        print("Right: Exactly")

        
play_again = "yes"
while play_again == "yes":
    randomGame()
    
    play_again = input("Do you want to play again? yes/no:").lower()
    if play_again != "yes":
        break
        
        
        
        
        