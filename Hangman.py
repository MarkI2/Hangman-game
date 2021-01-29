# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 21:39:22 2021

@author: BiMar
"""


import random

def pick_word():
    words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks'] 
    #count = random.randint(0,len(words))
    #return(words[count])
    return(random.choice(words))

# Two more features to add
 # Ensure that only lowercase letters are accepted and if upper then turn to lowercase
 # Ensure that the length of the input is only 1 letter.
 
def game():
    Fail = False
    Win = False
    word = pick_word()
    counter = 0
    hangman = 0
    print('This is a {} letter word'.format(len(word)))
    while Fail == False or Win == False:
        player = input('Please pick a letter: ')
        while len(player) > 1 or player.isdigit():
            player = input('Please type one letter only and no numbers are included: ')
        if player.isupper():
           player = player.lower()
        if player in word:
            counter += 1
        else:
            hangman += 1
            print("You have {} guesses left".format(10-hangman))
        
        if counter == len(word):
            print("You win")
            Win = True
            break
        elif hangman == 10:
            print("You lost")
            Fail = True
            break

keepPlay = True

while keepPlay == True:
    game()
    answer = input("Do you wish to keep play?")
    if answer == "yes":
        game()
    else:
        keepPlay = False
        break
