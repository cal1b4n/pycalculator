# Calculator v2.0
# It's going to cycle through options unless you input ---> 0
import math


def options():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("0. Exit")


options()

while True:
    x = float(input("Input your choice: \n"))
    if x == 1:
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        print("\n")
        print(a, "+", b, "=", a+b)
        print("\n")
        options()
    elif x == 2:
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        print("\n")
        print(a, "-", b, "=", a-b)
        print("\n")
        options()
    elif x == 3:
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        print("\n")
        print(a, "x", b, "=", a*b)
        print("\n")
        options()
    elif x == 4:
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        print("\n")
        print(a, "/", b, "=", a//b)
        print("\n")
        options()
    elif x == 5:
        try:  # Try to calculate square root --->
            a = float(input("Input the number: "))
            print("\n")
            print("Square root of", a, "Is: ", math.sqrt(a))
            print("\n")
            options()
        except ValueError:  # In case of error, print this --->
            print("Not possible for negative numbers unfortunately...\n")
    elif x == 0:
        print("Exiting...")
        break
    else:
        print("Option not found... Please use existing one!\n")
        options()
