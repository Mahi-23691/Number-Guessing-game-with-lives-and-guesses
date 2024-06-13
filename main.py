"""

#Number Guessing Game With Lives

import random

true_num = random.randint(1, 100)

print('\nWelcome to the Number Guessing Game!')
print('\nThe computer is thinking of a number between 1 and 100.')
print('\nYou have 10 lives')

lives = 10

while True:
  guess = int(input('\nYour Guess: '))
  if guess == true_num:
    print('\nCongratulation!!! You guessed the number!')
    print(f'\nYou had to use {10 - lives} lives to guess the correct number.')
    break
  elif guess > true_num:
    print('\nYour guess was too high.')
    lives = lives - 1
    print(f'\nYou have {lives} lives left.')
  elif guess < true_num:
    print('\nYour guess was too low.')
    lives = lives - 1
    print(f'\nYou have {lives} lives left.')
  else: 
    print('\nInvalid input.')
    continue
  if lives == 0:
    print('\nYou ran out of lives.')
    break

"""

"""

#Number Guessing Game Guesses

import random

true_num = random.randint(1, 100)

print('\nWelcome to the Number Guessing Game!')
print('\nThe computer is thinking of a number between 1 and 100.')
print('\nTry to guess the number in as few guesses as possible.')

guesses = 0

while True:
  guess = int(input('\nYour Guess: '))
  if guess == true_num:
    print('\nCongratulation!!! You guessed the number!')
    print(f'\nYou had to take {guesses} gusses to guess the correct number.')
    break
  elif guess > true_num:
    print('\nYour guess was too high.')
    guesses = guesses + 1
  elif guess < true_num:
    print('\nYour guess was too low.')
    guesses = guesses + 1
  else: 
    print('\nInvalid input.')
    continue

"""



