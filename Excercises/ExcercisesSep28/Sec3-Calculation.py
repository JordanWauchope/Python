useInputs = False


def tablesize(l, w):
    area = l*w

    return area

if useInputs:
    length = input("How long is the table, in centimetres? ")
    width = input("How wide is the table, in centimetres? ")
else:
    length = 180
    width = 120

print(tablesize(length, width))


def tablesize2(n, l, w):
    area = tablesize(l, w)

    return "%s, the area of your table is %s cm squared." % (n, area)

if useInputs:
    name = input("What is your name? ")
    length = int(input("How long is the table, in centimetres? "))
    width = int(input("How wide is the table, in centimetres? "))
else:
    name = "Bob"
    length = 180
    width = 120

print(tablesize2(name, length, width))


def examscore(tsc, tst):
    avgscore = tsc / tst

    return avgscore

if useInputs:
    totalScore = int(input("What is the total score of all students who took the test? "))
    totalStudents = int(input("How many students took the test? "))
else:
    totalScore = 450
    totalStudents = 10

print(examscore(totalScore, totalStudents))


def ages(ta, ts):
    avgage = ta / ts

    return "The average age in this room is %s" % avgage

if useInputs:
    totalAge = int(input("What is the total age of all students in the room? "))
    totalStudents = int(input("How many students are there in the room? "))
else:
    totalAge = 160
    totalStudents = 10

print(ages(totalAge, totalStudents))
