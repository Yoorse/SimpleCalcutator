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

