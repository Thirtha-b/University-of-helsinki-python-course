sentence=""
previous = ""
while True:
    word = input("Please type in a word:")
    if word == "end" or word ==  previous:
      break
    sentence = sentence + word + " "
    previous = word
print(sentence)