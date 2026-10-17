user_input = input("Enter a string: ")
if len(user_input) < 20:
    output = '*' * (20 - len(user_input))+ user_input
else:
    output = user_input[-20]
print(output)