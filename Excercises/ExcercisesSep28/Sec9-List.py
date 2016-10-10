from random import choice

def colours():
    colour_list = ["red", "green", "blue"]
    print(colour_list)

    colour_list.append("yellow")
    print(colour_list)

    colour_list.remove("blue")
    print(len(colour_list))

colours()


def months():
    month_list = ["January", "February", "March"]
    print(month_list)

    month_list.append("April")
    print(month_list)

    month_list.pop(1)
    print(month_list, len(month_list))

months()


def name_generator():
    entered = None
    name_list = []

    while entered != "End":
        entered = input("Please enter a name: ").capitalize()
        if entered != "End":
            name_list.append(entered)

    print(name_list, len(name_list))

name_generator()


def name_chooser():
    name_list = []
    for x in range(0, 5):
        entered = input("Please enter a name: ").capitalize()
        name_list.append(entered)

    return choice(name_list)

print("Well done %s, you are the winner!" % name_chooser())
