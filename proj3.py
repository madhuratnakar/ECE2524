#!/usr/bin/python3
# Hangman game

import random

def pickWord():
    return words[random.randint(0, len(words) - 1)]


words = '''key virginia technology'''.split()

print('Welcome to Hangman !')

word = list(pickWord())

result = list('_' * len(word))

print('The word is: ', result)
