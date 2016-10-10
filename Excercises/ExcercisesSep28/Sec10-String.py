useInputs = False


def sentence1():
    sentence = "I like to go on holiday by the sea."
    for x in sentence:
        print(x)

# sentence1()


def sentence2():
    sentence = "I like to go on holiday by the sea"

    print(len(sentence))

    for x in sentence:
        if 7 <= x < 24:
            print(sentence[x])

# sentence2()


def sentence3(s):
    y = 0
    for x in s:
        if x == "a":
            y += 1
    return y

if useInputs:
    sentence = input("Please enter a sentence: ")
else:
    sentence = "I like to eat icecream on a sunny day."

print(sentence3(sentence))


def sentence4(s):
    if s[::-1].lower() == s.lower():
        print("%s is a palindrome." % s)

if useInputs:
    word = input("Please enter a word: ")
else:
    word = "Noon"

sentence4(word)