# ============================
# **Python List Cheat Sheet**
# ============================

# 1. **Creating Lists**
# Empty list
my_list = []  

# List with numbers
numbers = [1, 2, 3, 4, 5]  

# List with mixed data types (numbers, strings, booleans)
mixed = ["apple", 42, True, 3.14]  

# Nested list (list inside a list)
nested = [[1, 2], [3, 4], [5, 6]]  

# ============================
# **Accessing List Items**
# ============================

# Indexing (start from 0, negative indexing starts from the end)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

# Slicing (get sublists)
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # Output: [20, 30, 40]
print(numbers[:3])  # Output: [10, 20, 30]
print(numbers[2:])  # Output: [30, 40, 50]

# ============================
# **Common List Methods**
# ============================

# Add items to list
nums = [1, 2, 3]
nums.append(4)  # Adds 4 to the end of the list: [1, 2, 3, 4]
nums.insert(1, 10)  # Inserts 10 at index 1: [1, 10, 2, 3, 4]

# Remove items from list
nums.remove(2)  # Removes the first occurrence of 2: [1, 3, 4]
nums.pop(1)  # Removes item at index 1: [1, 4]
nums.clear()  # Clears the list: []

# Modify items (update value at a specific index)
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Updates index 1: ["apple", "blueberry", "cherry"]

# Find items in a list
nums = [1, 2, 3, 2]
print(nums.index(2))  # Output: 1 (index of first occurrence of 2)
print(nums.count(2))  # Output: 2 (how many times 2 appears in the list)

# Sort and reverse lists
nums = [3, 1, 4, 2]
nums.sort()  # Sorts the list: [1, 2, 3, 4]
nums.sort(reverse=True)  # Sorts in descending order: [4, 3, 2, 1]
nums.reverse()  # Reverses the list: [1, 2, 4, 3]

# Copy a list
original = [1, 2, 3]
copy_list = original.copy()  # Creates a copy: [1, 2, 3]

# ============================
# **Iterating Through a List**
# ============================

# Using a loop to iterate through list items
for fruit in fruits:
    print(fruit)

# Iterating with index using enumerate()
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# ============================
# **Advanced Features**
# ============================

# List comprehension (create a list in one line)
squares = [x**2 for x in range(1, 6)]  # Output: [1, 4, 9, 16, 25]

# Check if item is in list
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Output: True
print("grape" not in fruits)  # Output: True

# Get the length of a list
nums = [1, 2, 3]
print(len(nums))  # Output: 3

# ============================
# **Useful Built-in Functions**
# ============================

# Built-in functions for lists
nums = [1, 2, 3, 4]
print(len(nums))  # Output: 4 (length of the list)
print(max(nums))  # Output: 4 (largest item)
print(min(nums))  # Output: 1 (smallest item)
print(sum(nums))  # Output: 10 (sum of all items)

# ============================
# **Nested Lists**
# ============================

# List containing other lists (nested list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])  # Output: [1, 2, 3] (access first inner list)
print(matrix[1][2])  # Output: 6 (access element at index [1][2])

# ============================
# **Lists Are Versatile!**
# ============================
# - Store any type of data: numbers, strings, or even other lists.
# - Easily modify, add, or remove items.
# - Manage collections of data efficiently.
