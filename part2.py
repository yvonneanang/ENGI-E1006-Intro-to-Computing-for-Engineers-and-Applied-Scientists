## -*- coding: utf-8 -*-
#"""
#Created on Sun Sep 22 20:02:52 2019
#
#@author: Yvonne
#"""
#

import random

x = int(random.random() * 10 + 1) 
print ("If the number guessed is too big, type 'b', If the number guessed is too small, type 's', If the number guessed is correct, type 'c'")

left = 1
right  = 10
number_of_guesses_used = 1

while number_of_guesses_used < 4:
    print ("Computer guess is", x)
    player_move = input("What is your input?:>>>")
    
    if player_move == "b":
        right = x - 1
    elif player_move == "s":
        left = x + 1
    elif player_move == "c":
        print ("I, the computer, win.")
        break
    elif player_move != "b" and player_move != "s" and player_move != "c":
        print ("Invalid input. If the number guessed is too big, type 'b', If the number guessed is too small, type 's', If the number guessed is correct, type 'c'")
        continue
    
    x = (right + left)//2
    
    
    number_of_guesses_used += 1
    
print ("Game over.") 




