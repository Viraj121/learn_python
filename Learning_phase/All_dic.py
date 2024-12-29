# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "job": "Engineer"
}

# Accessing values by key
print(person["name"])  # Output: Alice

# Modifying a value
person["age"] = 26  # Changes age to 26

# Adding a new key-value pair
person["city"] = "London"

# Removing an item using pop()
removed_value = person.pop("job")  # Removes 'job' and returns its value
print(removed_value)  # Output: Engineer

# Checking keys and values
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(person.values())  # Output: dict_values(['Alice', 26, 'London'])

# Clearing the dictionary
person.clear()
print(person)  # Output: {}
