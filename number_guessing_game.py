#Guessing Game

#Rules
"""User choose level easy or hard. Level easy has 7 attempts to guess and level hard has 5 attempts.
User writes a number and app gives hint if the number is lower,higher or the user guessed it."""

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")


#level = input("Choose a difficulty.Type 'easy' or 'hard':")


#print(number)
play_again=True

while(play_again):
    number = random.randint(1, 100)
    level = input("Choose a difficulty.Type 'easy' or 'hard':")
    if level == "easy":
        print("You have 7 attempts remaining to guess the number")
        #guess = int(input("Make a guess:"))
        attempts = 7
        while(attempts>0):
            #print("You have 7 attempts remaining to guess the number")
            guess = int(input("Make a guess:"))
            if guess > number:
                print("Too high")
                print("Guess again")
                attempts = attempts - 1
                print(f"You have {attempts} attempts left")
            elif guess < number:
                print("Too low")
                print("Guess again")
                attempts = attempts - 1
                print(f"You have {attempts} attempts left")
            else:
                print(f"You have guessed correctly that the number is {number}")
                attempts = 0
                again = input("If you want to play again type 'y', if you want to end type 'n': ")
                if again == "y":
                    play_again = True
                else:
                    print("Thank you for the game. Goodbye!")
                    play_again = False
                    break;
        if attempts == 0 and guess != number:
            print("You lost because you have used all your attempts")
            again=input("If you want to play again type 'y', if you want to end type 'n': ")
            if again == "y":
                play_again=True
            else:
                print("Thank you for the game. Goodbye!")
                play_again=False
    elif level == "hard":
        print("You have 5 attempts remaining to guess the number")
        #guess = int(input("Make a guess:"))
        attempts = 5
        while (attempts > 0):
            #print("You have 5 attempts remaining to guess the number")
            guess = int(input("Make a guess:"))
            if guess > number:
                print("Too high")
                print("Guess again")
                attempts = attempts - 1
                print(f"You have {attempts} attempts left")
            elif guess < number:
                print("Too low")
                print("Guess again")
                attempts = attempts - 1
                print(f"You have {attempts} attempts left")
            else:
                print(f"You have guessed correctly that the number is {number}")
                attempts = 0
                again = input("If you want to play again type 'y', if you want to end type 'n': ")
                if again == "y":
                    play_again = True
                else:
                    print("Thank you for the game. Goodbye!")
                    play_again = False
                    break;
        if attempts == 0 and guess != number:
            print("You lost because you have used all your attempts")
            again=input("If you want to play again type 'y', if you want to end type 'n': ")
            if again == "y":
                play_again=True
            else:
                print("Thank you for the game. Goodbye!")
                play_again=False
    else:
        print("You typed wrong level")
        break;