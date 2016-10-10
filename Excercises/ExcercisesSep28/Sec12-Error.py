from random import randint
import sys
useInputs = False


def float_number(x):
    if isinstance(x, float):
        return x
    else:
        return ""
if useInputs:
    number = float(input("Please enter a number: "))
else:
    number = 5.0

print(float_number(number))


def big_number(x):
    if x > 100:
        return "Number is a big number."
    else:
        return x

number = randint(0,150)
print(big_number(number))


def file_opening():
    try:
        f = open("holidays1.txt")
        print(f.read())
    except FileNotFoundError:
        print("File not found.")

file_opening()
