from random import *
from time import sleep
def number():
    return randint(1, 100)

print(number())


def odds():
    x = 0

    while x % 2 == 0:
        x = randint(1, 30)

    return x

print(odds())


def guess():
    x = str(randint(1, 100))

    user_guess = input("I am thinking of a number between 1 and 100.\nWhat is it? ")

    while user_guess != x:
        if user_guess > x:
            user_guess = input("That number is too high, guess again: ")
        else:
            user_guess = input("That number is too low, guess again: ")
    
    return "That is correct!"

print(guess())

def sleep1():
    input("Please enter a question: ")

    for x in range(0, 5):
        print("I am thinking...")
        sleep(4)

    return "I don't know the answer."

print(sleep1())
