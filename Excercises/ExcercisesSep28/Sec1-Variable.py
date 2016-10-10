def cakes():
    cpperson = 2
    person = 25

    total = cpperson*person

    return total

print(cakes())


def housepoints():
    c1 = 23
    c2 = 47
    c3 = 56
    c4 = 73

    total = c1+c2+c3+c4

    return total

print(housepoints())


def enterprise():
    revenue = 620
    cost = 400

    profit = revenue-cost

    return profit

print(enterprise())


def enterprise2(profit):
    return "The profit made is %s" % profit

print(enterprise2(enterprise()))