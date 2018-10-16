##This forces the user to use numbers


def Input(message):

    while True:
        try:
            UserInput = int(input(message))
        except ValueError:
            print("Type a number!")
            continue
        else:
            return UserInput
            break


def choose(message):

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    while True:
        try:
            calculate = int(input(message))
        except ValueError:
            if calculate > 5:
                print("Choose 1-5")

        else:
            return calculate
            break

