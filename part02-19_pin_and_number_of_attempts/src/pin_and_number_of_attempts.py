attempts = 0

while True:
    PIN = int(input("Enter pin: "))
    attempts += 1
    
    if PIN == 4321:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")