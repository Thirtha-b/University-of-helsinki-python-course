sentence = input("Please type in a sentence: ")


print(sentence[0])

index = 0
while index < len(sentence):
    if sentence[index] == " ":
        print(sentence[index + 1])
    
    
    index += 1