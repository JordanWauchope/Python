useInputs = False


def groups(cpg, g):
    total = cpg*g

    return total

if useInputs:
    children = int(input("How many children are in each group? "))
    group = int(input("How many groups are in the class? "))
else:
    children = 6
    group = 5

print(groups(children, group))


def groups2():
    return "There are %s children in the class" % (groups(children, group))

print(groups2())


def yeargroup(n, yg):
    return "%s! You'll be in year %s next year!" % (n, yg+1)

if useInputs:
    name = input("What is your name? ")
    year = int(input("What year are you in? "))
else:
    name = "Bob"
    year = 8

print(yeargroup(name, year))


def birthdays(n, dub):
    sub = dub * 24 * 60 * 60

    return "Congratulations %s! There are %s seconds until your birthday!" % (n, sub)

if useInputs:
    name = input("What is your name? ")
    daysUntilBirthday = int(input("How many days are left until your next birthday? "))
else:
    name = "Bob"
    daysUntilBirthday = 143

print(birthdays(name, daysUntilBirthday))
