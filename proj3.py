#!/usr/bin/python3
# Hangman game

import random

def ask(word, result, notGuessed):
    guess = input()
    if guess == None or len(guess) != 1 or (guess in result) or (guess in notGuessed):
        return None, False
    i = 0
    correct = guess in word
    for c in word:
        if c == guess:
            result[i] = c
        i += 1
    return guess, correct

words = 'foo baa wee mee'.split()

selects = []

print('Welcome to Hangman !')

userLevel = 0

while True:
    userInput = input('Enter Level -> (e)asy (m)edium (h)ard e(X)it  -> ')[0]

    if userInput == "e":
        userLevel = 8
        print ('Easy Level Chosen')
        break
    elif userInput == "m":
        userLevel = 6
        print ('Medium Level Chosen')
        break
    elif userInput == "h":
        userLevel = 4
        print ('Hard Level Chosen')
        break
    elif userInput == "x":
        userLevel = 4
        print ('Exit Chosen')
        exit (0)
    else:
        print ('Wrong Choice Chosen')

word = list(words[random.randint(0, len(words) - 1)])

result = list('_' * len(word))

print('The word is: ', result)

success = False

notGuessed = []

i = 0

while i < userLevel-1:
    print('Please start guessing the word: ')
    guess,correct = ask(word, result, notGuessed)
    if guess == None:
        print('you already guessed this character...')
        continue
    print(''.join(result))
    if result == word:
        print('You guessed it... !')
        success = True
        break
    if not correct:
        notGuessed.append(guess)
        i+=1
    print('incorrect guesses so far -> ', notGuessed)
    #print ('i is ' + str(i) )

if not success:
    #print('Word is - '.join(word))
   print('Ran out of lives.. Game Over.. Word is \''+''.join(word)+'\'')
