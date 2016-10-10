end = "N"
correctUnit = False

lengths = ["cm", "m", "km", "in", "ft", "yd", "mi"]
times = ["seconds", "minutes", "hours", "days"]

unitsGroups = ["Lengths", "Times", "Speed"]
units = [lengths, times, (lengths, times)]


def convertlengths(iu, iv):
    metric = ["cm", "m", "km"]
    iv = float(iv)
    if iu in metric:
        if iu == "cm":
            vcm = iv
        elif iu == "m":
            vcm = iv * 100
        elif iu == "km":
            vcm = (iv * 1000 * 100)
        vin = vcm / 2.54
    else:
        if iu == "in":
            vin = iv
        elif iu == "ft":
            vin = iv * 12
        elif iu == "yd":
            vin = (iv * 12) * 3
        elif iu == "mi":
            vin = ((iv * 12) * 3) * 1760
        vcm = vin * 2.54

    return iv, iu, vcm, vcm / 100, (vcm / 100) / 1000, vin, vin / 12, (vin / 12) / 3, ((vin / 12) / 3) / 1760


def converttimes(iu, iv):
    if iu == "seconds":
        vs = iv
    elif iu == "minutes":
        vs = iv * 60
    elif iu == "hours":
        vs = (iv * 60) * 60
    elif iu == "days":
        vs = ((iv * 60) * 60) * 24

    return iv, iu, vs, vs / 60, (vs / 60) / 60, ((vs / 60) / 60) / 24


def convertspeed(iu1, iv1, iu2, iv2, ou1, ou2):
    returnedLengths = convertlengths(iu1, iv1)[2:8]
    if ou1 == "cm":
        vc1 = returnedLengths[0]
    elif ou1 == "m":
        vc1 = returnedLengths[1]
    elif ou1 == "km":
        vc1 = returnedLengths[2]
    elif ou1 == "in":
        vc1 = returnedLengths[3]
    elif ou1 == "ft":
        vc1 = returnedLengths[4]
    elif ou1 == "yd":
        vc1 = returnedLengths[5]
    elif ou1 == "mi":
        vc1 = returnedLengths[6]

    returnedTimes = converttimes(iu2, iv2)[2:5]

    if ou2 == "seconds":
        vc2 = returnedTimes[0]
    elif ou2 == "minutes":
        vc2 = returnedTimes[1]
    elif ou2 == "hours":
        vc2 = returnedTimes[2]
    elif ou2 == "days":
        vc2 = returnedTimes[3]

    print(iv1, iu1, iv2, iu2, vc1, vc2)
    return iv1, iu1, iv2, iu2, vc1, vc2


def convert(iu1, iv1, iu2, iv2, ou1, ou2):
    if unitGroup == "Lengths":
        return convertlengths(iu1, iv1)
    if unitGroup == "Times":
        return converttimes(iu1, iv1)
    if unitGroup == "Speed":
        return convertspeed(iu1, iv1, iu2, iv2, ou1, ou2)


while end == "N":
    try:
        unitGroup = None
        correctUnit = False

        while not correctUnit:
            unitGroup = input(
                "What set of units would you like to convert from?\n%s:%s\n%s:%s\nSpeed:[Lengths, Times]\n"
                % (unitsGroups[0], units[0], unitsGroups[1], units[1])).capitalize()

            initialUnit1 = None
            initialUnit2 = None
            outputUnit1 = None
            outputUnit2 = None

            initialValue1 = 0
            initialValue2 = 0

            if unitGroup != "Speed":
                initialUnit1 = input("What unit of measurement are you converting from?\n").lower()
                initialValue1 = int(input("Please enter a value:\n"))
                if unitGroup == "Lengths":
                    if initialUnit1 in units[0]:
                        correctUnit = True
                elif unitGroup == "Times":
                    if initialUnit1 in units[1]:
                        correctUnit = True
            else:
                initialUnit1 = input("What measurement of length are you converting from?\n").lower()
                outputUnit1 = input("What measurement of length are you converting to?\n").lower()
                initialUnit2 = input("What measurement of time are you converting from?\n").lower()
                outputUnit2 = input("What measurement of time are you converting to?\n").lower()
                if (initialUnit1 in units[0] and outputUnit1 in units[0] and
                        initialUnit2 in units[1] and outputUnit2 in units[1]):
                    initialValue2 = input("Please enter a value for the length:\n")
                    initialValue2 = int(input("Please enter a value for the time:\n"))
                    correctUnit = True
    except Exception:
        print("An error occurred. Ending Program.")
        break

    returned = convert(initialUnit1, initialValue1, initialUnit2, initialValue2, outputUnit1, outputUnit2)

    if unitGroup == "Lengths":
        print("%s %s is equal to:\n\n%s cm\n%s m\n%s km\n%s inches\n%s ft\n%s yd\n%s mi" % returned)
    if unitGroup == "Times":
        print("%s %s is equal to:\n\n%s seconds\n%s minutes\n%s hours\n%s days" % returned)
    if unitGroup == "Speed":
        print("%s %s over %s %s is equal to:\n%s over %s" % returned)

    end = input("Do you want to end the program? Y/N.\n").upper()
