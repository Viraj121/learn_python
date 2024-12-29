# Python Operator Cheatsheet with Examples

# Logical Operators
# Combine conditional statements
x = 10
y = 5

# AND: Both conditions must be True
print(x > 5 and y < 10)  # True: (10 > 5) AND (5 < 10)

# OR: At least one condition must be True
print(x < 5 or y < 10)   # True: (10 < 5) OR (5 < 10)

# NOT: Reverses the condition
print(not(x > 5))        # False: NOT(True) → False


# Equality Operators
# Compare two values and return True or False
a = 10
b = 20

# Equal to
print(a == b)            # False: 10 is not equal to 20

# Not equal to
print(a != b)            # True: 10 is not equal to 20


# Comparison Operators
# Compare two values
num1 = 15
num2 = 10

# Greater than
print(num1 > num2)       # True: 15 is greater than 10

# Less than
print(num1 < num2)       # False: 15 is not less than 10

# Greater than or equal to
print(num1 >= 15)        # True: 15 is equal to 15

# Less than or equal to
print(num2 <= 15)        # True: 10 is less than 15


# Arithmetic Operators
# Perform mathematical operations
x = 7
y = 3

# Addition
print(x + y)             # 10: Adds 7 and 3

# Subtraction
print(x - y)             # 4: Subtracts 3 from 7

# Multiplication
print(x * y)             # 21: Multiplies 7 and 3

# Division
print(x / y)             # 2.3333: Divides 7 by 3 (float result)

# Floor Division
print(x // y)            # 2: Divides 7 by 3 and removes decimal part

# Modulus
print(x % y)             # 1: Remainder when 7 is divided by 3

# Exponentiation
print(x ** y)            # 343: 7 raised to the power of 3


# Additional Examples to Combine Operators

# Logical + Comparison
age = 25
print(age > 18 and age < 30)  # True: Age is between 18 and 30

# Arithmetic + Equality
num = 15
print((num % 5 == 0) and (num % 3 == 0))  # True: 15 is divisible by both 5 and 3

# Combining Logical, Equality, and Arithmetic Operators
x = 20
y = 5
z = 10

result = (x > y) and (z == y * 2) or (x < 30)
print(result)  # True: Both conditions in AND are true, OR condition makes it true overall
