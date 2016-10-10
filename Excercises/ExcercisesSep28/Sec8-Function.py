import math
useInputs = False

def sleeping():
    for x in range(0, 4):
        print("I'm still sleeping!")
    for x in range(0, 7):
        print("I'm awake!")
    print("No I'm not!!!!")

sleeping()


def triple(x):
    return x*3

if useInputs:
    number = input("Please enter a number: ")
else:
    number = 15

print("Triple %s is %s" % (number, triple(number)))


def radius(x):
    return math.pi*(x**2)

if useInputs:
    number = float(input("Please enter a number: "))
else:
    number = 1.0


print(radius(number))


def rectangle(x, y):
    return x*y

if useInputs:
    length = float(input("Please enter the length: "))
    width = float(input("Please enter the width: "))
else:
    length = 5.0
    width = 3.0

print(rectangle(length, width))

