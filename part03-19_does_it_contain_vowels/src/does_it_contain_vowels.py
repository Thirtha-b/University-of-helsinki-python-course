text = input("Please type in a string: ")
vowels = ['a', 'e', 'o']
for vowel in vowels:
    if vowel in text:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")