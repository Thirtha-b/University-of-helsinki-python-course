year=int(input("Enter year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
elif (year % 4 != 0 and year % 100 == 0) or (year % 400 != 0):
    print("That year is not a leap year.")
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")