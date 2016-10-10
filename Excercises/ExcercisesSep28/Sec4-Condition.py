import random

useInputs = True


def homeworktime(h):
    if h < 2:
        return "%s hour(s)? That's about right!" % h
    else:
        return "%s hours? That's too long!" %h

if useInputs:
    hoursSpent = int(input("How many hours do you spend doing your homework each night? "))
else:
    hoursSpent = random.randint(0, 5)

print(homeworktime(hoursSpent))


def tv(h):
    if h < 3:
        return "%s hour(s)? That's ok!" % h
    else:
        return "%s hours? That's a lot!" % h

if useInputs:
    hoursSpent = int(input("How many hours do you spend watching TV each day? "))
else:
    hoursSpent = random.randint(0, 5)

print(tv(hoursSpent))


def favSubject(s):

    if s == 1:
        return "That's great."
    if s == 2:
        return "Maths is cool."
    if s == 3:
        return "Science is fun."
    if s == 4:
        return "Me too."

if useInputs:
    subject = int(input("""What is your favourite subject?
    Enter 1 for English,
          2 for Maths,
          3 for Science and
          4 for ICT
          """))
else:
    subject = random.randint(1, 4)

print("Subject chosen: %s, %s" % (subject, favSubject(subject)))


def french(w):
    if w.lower() == "dog":
        return "Dog in French is le chien."
    elif w.lower() == "cat":
        return "Cat in French is le chat."
    elif w.lower() == "hamster":
        return "Hamster in French is le hamster."
    elif w.lower() == "fish":
        return "Fish in French is le poisson."
    elif w.lower() == "rabbit":
        return "Rabbit in French is le lapin."
    else:
        return "I'm sorry, I don't know how to translate that."

if useInputs:
    word = input("""Please choose a word from the following to translate into french:
           Dog
           Cat
           Hamster
           Fish
           Rabbit
           """)
else:
    list = ("Dog", "Cat", "Hamster", "Fish", "Rabbit")
    word = random.choice(list)

print(french(word))
