mark=int(input("How many points [0-100]:"))
if mark < 0:
    print("Grade: impossible!")
elif 0 <= mark <= 49:
    print("Grade: fail")
elif 50 <= mark <= 59:
    print("Grade: 1")
elif 60 <= mark <= 69:
    print("Grade: 2")
elif 70 <= mark <= 79:
    print("Grade: 3")
elif 80 <= mark <= 89:
    print("Grade: 4")
elif 90 <= mark <= 100:
    print("Grade: 5")
elif mark > 100:
    print("Grade: impossible!")