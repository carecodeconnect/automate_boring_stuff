# Guess the number game

import random
import sys

num_start = 1
num_end = 20

computer_guess = random.randint(num_start, num_end)
computer_guess

guesses = 1

print("Welcome to the GUESS THE NUMBER game!")
print("What's your name?")
username = input('>')
print(f"Nice to meet you {username}")
print("...")

while True:
    print(f"I am thinking of a number between {num_start} and {num_end}")
    print(f"Take a guess")

    user_guess = int(input('>'))
    user_guess

    if user_guess > computer_guess:
        print("Your guess is too high")
        guesses += 1
        continue
    elif user_guess < computer_guess:
        print("Your guess is too low")
        guesses +=1
        continue
    elif user_guess == computer_guess:
        print(f"Good job! You got it in {guesses} guesses!")
        sys.exit()
