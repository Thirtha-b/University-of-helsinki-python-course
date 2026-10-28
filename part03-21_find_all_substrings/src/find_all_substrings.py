word = input("Please type in a word: ")
char = input("Please type in a character: ")
for i in range(len(word)):
    if word[i] == char and i + 3 <= len(word):
        print(word[i:i+3])