def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        print("Thanks and bye!")
        break
    else:
        print(f"The factorial of the number {num} is {factorial(num)}")