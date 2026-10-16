a1=input("Please type in string 1:")
a2=input("Please type in string 2")
if len(a1)>len(a2):
    print(f"{a1} is longer")
elif len(a2)>len(a1):
    print(f"{a2} is longer")
else:
    print('The strings are equally long')