def writing1():
    f = open("holidays.txt", "w")
    f.write("I like to go on holidays by the sea.")
    f.close()


writing1()


def writing2():
    f = open("holidays.txt", "w")
    f.write("I like to go on holidays by the sea.\n")
    f.write("Oh yes I do.\n")
    f.write("It is great fun splashing in the waves.\n")
    f.write("But best of all I like to build sandcastles.\n")
    f.close()

writing2()

def reading1():
    f = open("holidays.txt")
    print(f.read())

reading1()

def reading2():
    f = open("holidays.txt")
    for line in f:
        print(line)

reading2()