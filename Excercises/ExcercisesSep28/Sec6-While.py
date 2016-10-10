useInputs = False

def bouncing():
    x = 0
    while x < 8:
        x += 1
        print("bouncing")

# bouncing()


def loops():
    x = 0
    while x < 12:
        x += 1
        print("%s Looping" % x)

# loops()


def letters2(l, n):
    x = 0
    while x < n:
        x += 1
        print(l)

if useInputs:
    letter = input("Please enter a letter: ").upper()
    number = int(input("How many times would you like this repeated? "))
else:
    letter = "T"
    number = 6

# letters2(letter, number)


def squares():
    x = 0
    y = 1
    while y < 5000 and (x+1) ** 2 < 5000:
        x += 1
        y = x ** 2
        print("%s: %s" % (x, y))

# squares()
