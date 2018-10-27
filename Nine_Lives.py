import random

words = ['king', 'fair', 'trip', 'pack', 
         'ruby', 'book']
words2 = ['pizza', 'otter', 'quick', 'apple', 
         'taser', 'plane']
words3 = ['prince', 'topaz', 'pencil', 'market', 
         'sheild', 'island']


difficulty = input('Choose difficulty (type 1, 2, 3) : \n 1 Easy\n 2 Normal\n 3 Hard\n')
difficulty = int(difficulty)
x = 0
total = [words, words2, words3]
difficulty = difficulty - 1
lives = 15-(difficulty * 3)
difficulty = difficulty + 1
secret_word = ''
while True:
    if x == difficulty:
        x = x-1
        secret = total[x]
        secret_word = random.choice(secret)
        break
    x = x + 1
clue = list('?' * len(secret_word))
        
        


heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secretword, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1
        




    


        




while lives > 0:
    print(clue)
    print('Lives left :' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word:')
    
    if guess == secret_word:
        guessed_word_correctly = True
        break
    
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1
        
if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)