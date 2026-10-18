text = input("Please type in a string: ")

# Loop through the string and print substrings
for i in range(1, len(text) + 1):
    print(text[:i])