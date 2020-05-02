#!/usr/bin/python3
# Hangman game

import random

INPUT_FILE1 = "easywords.txt"
INPUT_FILE2 = "mediumwords.txt"
INPUT_FILE3 = "hardwords.txt"

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

selects = []

print('Welcome to Hangman !')

userLevel = 0

while True:
    userInput = input('Enter Level -> (e)asy (m)edium (h)ard e(X)it  -> ')[0]

    if userInput == "e":
        userLevel = 8
        inFile = open(INPUT_FILE1,'r')
        print ('Easy Level Chosen')
        break
    elif userInput == "m":
        userLevel = 6
        inFile = open(INPUT_FILE2,'r')
        print ('Medium Level Chosen')
        break
    elif userInput == "h":
        userLevel = 4
        inFile = open(INPUT_FILE3,'r')
        print ('Hard Level Chosen')
        break
    elif userInput == "x":
        userLevel = 4
        print ('Exit Chosen')
        exit (0)
    else:
        print ('Wrong Choice Chosen')

line = inFile.readline()
words = line.split()

word = list(random.choice(words))
#print (word)

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
        print('Good job!!.. You guessed it... !')
        success = True
        break
    if not correct:
        notGuessed.append(guess)
        i+=1
    print('incorrect guesses so far -> ', notGuessed)
    print ('Remaining Lives -> ' + str(userLevel-i-1) )

if not success:
    #print('Word is - '.join(word))
   print('Ran out of lives.. Game Over.. Word is \''+''.join(word)+'\'')
