# Guess The Number Game

import random

guesses_taken = 0  #initialized to zero and this store the number of guesses from the player
name = input("Hey there!, What is your name :") # input ask players for their name

number = random.randint(1, 40) # random numbers between the integers(a, b) and converted to integer by randint
print('Welcome ' + name + ', You know I am thinking of a number between 1 and 40.')

for guesses_taken in range(6): # iteration of the guess taking in set range
    print('Can you guess the number? : ')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high.')
    if guess ==number:
        break

if guess == number: #checking if the palyer won
    guesses_taken = str(guesses_taken + 1)
    print("Great " + name + '! you guessed my number in ' + guesses_taken + ' guesses')
if guess != number: #checking if the lost
    number = str(number)
    print("Nope. The number I was thinking of was " + number + '.')