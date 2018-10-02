##Definitions of calculations

from Force_Integer import *

Calculator = True


def add():
    print("Addition")

    A = (Input("Type value for A:  "))
    B = (Input("Type Value for B:  "))

    result = A + B
    print(A, "+", B, "=", result)


def sub():
    print("Subtraction")

    A = (Input("Type value for A:  "))
    B = (Input("Type Value for B:  "))

    result = A - B
    print(A, "-", B, "=", result)


def mul():
    print("Multiplication")

    A = (Input("Type value for A:  "))
    B = (Input("Type Value for B:  "))

    result = A * B

    print(A, "*", B, "=", result)


def div():
    print("Division")

    A = (Input("Type value for A:  "))
    B = (Input("Type Value for B:  "))

    result = A / B
    print(A, "/", B, "=", result)


def quit():
    print("Quit!")


