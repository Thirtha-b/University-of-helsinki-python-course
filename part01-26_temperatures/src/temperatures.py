temp=int(input("Please type in a temperature (F):"))
if temp >0:
    print(f"{temp} degrees Fahrenheit equals {(temp-32)*5/9} degrees Celsius")
else: 
    print(f"{temp} degrees Fahrenheit equals {(temp-32)*5/9} degrees Celsius")
    print("Brr! It's cold in here!")