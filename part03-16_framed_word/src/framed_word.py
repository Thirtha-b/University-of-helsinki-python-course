word = input("Enter a word: ")
width = 30
total_spaces = width - 2 - len(word)
left_spaces = total_spaces // 2
right_spaces = total_spaces - left_spaces
print("*" * width)
print("*" + " " * left_spaces + word + " " * right_spaces + "*")
print("*" * width)