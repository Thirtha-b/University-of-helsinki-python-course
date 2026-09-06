# Write your solution here
# Let's take the square root of math-module in use
from cmath import sqrt
a=int(input("enter value"))
b=int(input("enter value"))
c=int(input("enter value"))
root1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
root2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
print(f"The roots are {root1} and {root2}")

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5