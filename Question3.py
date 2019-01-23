# Author: Ashley Johnson
# Program: Guess the Number

# need to import the random class
import random

# declare a variable to store the randomly generated number between 1-100
aNumber = random.randint(1, 100)

# instructions for the user
print("")
print("Welcome to the Game High/Low!")
print("I'm thinking of a whole number between 1-100")
print("")

# declare a loop control variable with an assigned value of 0. 0 will always be wrong

userAnswer = 0

# while the user input does not match the random number, continue the loop.
while userAnswer != aNumber:
    # get user input
    userAnswer = int(input("Enter your guess: "))

    # test the condition, and output the appropriate statement
    # the loop will continue until the final == condition is met
    if userAnswer > aNumber:
        print("Too high! Try again with a lower number")

    if userAnswer < aNumber:
        print("Too low! Try again with a higher number")

    if userAnswer == aNumber:
        print("Correct! Well done!")

