print('Hello, World!')

# variables and data types

x=10
name="alice"
pi=3.14
is_active=True

# type casting

x=int("10")
y=str(123)

#  Dynamic Typing

x = 10       # Initially an integer
x = "Hello"  # Now a string
print(type(x))  # <class 'str'>

# Practical Examples

x = 10
print(f"x is of type {type(x)}")  # <class 'int'>

x = "Now I am a string!"
print(f"x is now of type {type(x)}")  # <class 'str'>


# Conditionals

x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

# Loops

# for loop

for i in range(5):  # range(5) generates 0, 1, 2, 3, 4
    print(i)

# example 2

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)  # Iterates through each element in the list



# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# break

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

# continue

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)


# Nested Control Structures

for i in range(3):
    for j in range(3):
        if i == j:
            print(f"i and j are equal: {i}")
        else:
            print(f"i: {i}, j: {j}")



for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed without break.")  # Won't execute


# function

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))


# Keyword Arguments

greet(age=25, name="Alice")  # Output: Alice is 25 years old.

#  Default Arguments

def greet(name, age=30):  # Default age is 30
    print(f"{name} is {age} years old.")

greet("Alice")  # Output: Alice is 30 years old.

# Variable-length Arguments - *args: For a variable number of positional arguments.

def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3, 4))  # Output: 10

# Nested Functions

def outer_function():
    def inner_function():
        print("This is the inner function.")
    inner_function()

outer_function()


# Lambda (Anonymous) Functions - lambda arguments: expression

add = lambda x, y: x + y
print(add(2, 3))

square = lambda x: x * x
print(square(5))  # Output: 25


# An f-string is prefixed with the letter f or F, and expressions inside curly braces {} are evaluated and included in the string.

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")



