from Choose_Calculation import *

##change so you only can choose 1-5 integers!
while Calculator:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    cmd = int(choose("Enter Your Choice from 1 to 5:  "))

    if cmd == 1:
        add()

    elif cmd == 2:
        sub()

    elif cmd == 3:
        mul()

    elif cmd == 4:
        div()

    elif cmd == 5:
        quit()
        break





