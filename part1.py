# -*- coding: utf-8 -*-
#"""
#Created on Sun Sep 22 17:55:43 2019
#
#@author: Yvonne
#"""
import random

x = int(random.random() * 10 + 1) 
number_of_guesses = 5
while number_of_guesses > 0 and number_of_guesses<= 5:
    
    player_move = int(input("Please guess a number:>>>"))
    
    if player_move > x:
        hint = player_move - x
    else:
        hint = x - player_move
    
    if player_move == x:
        print ("Computer chose", x, ". You win. Game over.")
        break
    
    while player_move != x and number_of_guesses > 1:        
        
        if hint > 5:
            print ("Not even close")
        elif hint >=3 and hint <=5:
            print ("Close")
        elif hint < 3:
            print ("Almost there")
       
        print ("Guess again.")
        break
    
    number_of_guesses = number_of_guesses - 1
    
if number_of_guesses == 0: 
    print ("Computer chose", x, ". You lose. Game over.")
 


