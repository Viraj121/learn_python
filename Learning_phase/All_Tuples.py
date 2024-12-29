# Creating a tuple with different data types
my_tuple = ("apple", 42, 3.14, True)

# Accessing elements by index
print(my_tuple[0])  # Output: apple
print(my_tuple[-1])  # Output: True (negative index)

# Slicing a tuple to get a sub-tuple
sub_tuple = my_tuple[1:3]
print(sub_tuple)  # Output: (42, 3.14)

# Counting occurrences of an item in the tuple
count = my_tuple.count("apple")
print(count)  # Output: 1

# Finding the index of an item
index = my_tuple.index(42)
print(index)  # Output: 1 (index of the first occurrence of 42)

# Concatenating two tuples
another_tuple = ("banana", 100)
combined_tuple = my_tuple + another_tuple
print(combined_tuple)  # Output: ('apple', 42, 3.14, True, 'banana', 100)

# Repeating a tuple
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: ('apple', 42, 3.14, True, 'apple', 42, 3.14, True)
