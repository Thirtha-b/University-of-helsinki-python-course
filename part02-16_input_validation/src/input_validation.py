from math import sqrt

while True:
    num = int(input("Enter an integer: "))

    if num < 0:
        print("Invalid number")
    elif num == 0:
        print("Exiting...")
        break
    else:
        print(sqrt(num))