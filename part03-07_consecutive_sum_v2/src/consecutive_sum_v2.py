limit = int(input("Limit: "))
current_sum = 0
number = 1
calculation_str = ""
while current_sum < limit:
    current_sum += number
    if calculation_str == "":
        calculation_str += str(number)
    else:
        calculation_str += f" + {number}"
        
    number += 1
print(f"The consecutive sum: {calculation_str} = {current_sum}")