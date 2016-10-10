useInputs = False


def buffering():
    for x in range(0, 24):
        dot = ""
        for y in range(0, x % 3):
            dot = dot + "."
        print("Buffering." + dot)

#buffering()


def looping():
    for x in range(0, 12):
        print("%s Looping" % (x+1))

#looping()


def letters(l, t):
    for x in range(0, t+1):
        print(l.upper())

if useInputs:
    letter = "Please enter a letter: "
    times = "Please enter a number: "
else:
    letter = "t"
    times = 6

#letters(letter, times)


def timestables(n):
    for x in range(0, 10):
        print("%s times %s is %s" % ((x+1), n, ((x+1)*7)))

if useInputs:
    number = "Please enter a number: "
else:
    number = 7

#timestables(number)