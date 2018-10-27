# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 09:04:19 2018

@author: JC
"""

import random

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 
         'otter', 'plane']
secret_word = random.choice(words)
clue = list('?????')
words = ['king', 'fair', 'trip', 'pack', 
         'ruby', 'book']
words2 = ['pizza', 'otter', 'quick', 'apple', 
         'taser', 'plane']
words3 = ['prince', 'topaz', 'pencil', 'market', 
         'sheild', 'island']


heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    clue[index] = guessed_letter
    index = index + 1
        
difficulty = input('Choose difficulty (type 1, 2, 3) : \n 1 Easy\n 2 Normal\n 3 Hard\n')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 15

    secret_word = random.choice(words)


elif difficulty == 2:
    lives = 12
    
    secret_word = random.choice(words2)

else:
    lives = 9
    
    secret_word = random.choice(words3)

clue = list('?' * len(secret_word))



while lives > 0:
    print(clue)
    print('Lives left' + heart_symbol * lives)
    print('Lives left :' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word:  ')
    
    if guess == secret_word:
        guessed_word_correcctly = True
        guessed_word_correctly = True
        break
