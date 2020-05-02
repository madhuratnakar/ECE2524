#!/usr/bin/python3
# Hangman game

import random

def selectWord():
    return words[random.randint(0, len(words) - 1)]

words = 'key virginia technology'.split()

selects = []

print('Welcome to Hangman !')

userLevel = 0

userInput = input('Enter Level -> (e)asy (m)edium (h)ard e(X)it  -> ')[0]

if userInput == "e":
    userLevel = 8
    print ('Easy Level Chosen')
elif userInput == "m":
    userLevel = 6
    print ('Medium Level Chosen')
elif userInput == "h":
    userLevel = 4
    print ('Hard Level Chosen')
elif userInput == "x":
    userLevel = 4
    print ('Exit Chosen')
else:
    print ('Wrong Choice Chosen')
    exit (0)
word = list(selectWord())

result = list('_' * len(word))

print('The word is: ', result)
