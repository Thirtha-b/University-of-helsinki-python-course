main_string = input("Please type in a string: ")
sub_string = input("Please type in a substring: ")
first_index = main_string.find(sub_string)
if first_index == -1:
    print("The substring does not occur twice in the string.")
else:
    second_index = main_string.find(sub_string, first_index + len(sub_string))
    if second_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")