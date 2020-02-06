# Hangman game

# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable

# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again
import random

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

print(gallows[4])


print("Hello\nWorld")


alphabet = [chr(x) for x in range(65, 65 + 26)]
print(alphabet)

random.shuffle(alphabet)
print(alphabet)


