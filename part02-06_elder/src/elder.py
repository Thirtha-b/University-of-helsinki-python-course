name1=input("enter name:")
age1=int(input("enter age:"))
name2=input("enter name:")
age2=int(input("enter age:"))
if age1 > age2:
    print(f"The elder is {name1}")
elif age1 < age2:
    print(f"The elder is {name2}")
elif age1==age2:
    print(f"{name1} and {name2} are the same age")