wage=float(input("Hourly wage: "))
hours=int(input("Hours worked: "))
Day_of_the_week=input("Day of the week: ")
if Day_of_the_week == "Sunday":
    print(f"Daily wages: {(2*wage)*hours} euros")
else:
    print(f"Daily wages: {wage*hours} euros")