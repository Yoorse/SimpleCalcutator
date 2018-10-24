##This forces the user to use numbers


def Input(message):

    while True:
        try:
            UserInput = int(input(message))
        except ValueError:
            print("Please type a number")
            continue
        else:
            return UserInput
            break


def choose(message):
    while True:
        try:
            UserInput = int(input(message))
        except ValueError:
            print("Please type a number between 1-5")
            continue
        else:
            return UserInput
            break





