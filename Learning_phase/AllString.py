# Python String Cheatsheet

# =============================
# 1. String Basics
# =============================
# Define a string
string = "Hello, World!"
print(string)  # Output: Hello, World!

# Escape characters
escaped_string = "Line 1\nLine 2\tTabbed"
print(escaped_string)  # Output: Line 1 (newline) Line 2    Tabbed

# Raw strings (ignore escape characters)
raw_string = r"C:\\Users\\Name"
print(raw_string)  # Output: C:\Users\Name

# String concatenation and repetition
print("Hello" + " " + "World")  # Output: Hello World
print("Ha" * 3)  # Output: HaHaHa

# =============================
# 2. String Methods
# =============================
# Case conversion
print(string.lower())  # Output: hello, world!
print(string.upper())  # Output: HELLO, WORLD!
print(string.capitalize())  # Output: Hello, world!
print(string.title())  # Output: Hello, World!
print(string.swapcase())  # Output: hELLO, wORLD!

# Searching and replacing
print(string.find("World"))  # Output: 7 (index of "World")
print(string.replace("World", "Universe"))  # Output: Hello, Universe!
print(string.count("l"))  # Output: 3 (number of 'l')

# Checking properties
print("abc123".isalnum())  # Output: True (alphanumeric)
print("123".isdigit())  # Output: True (digits only)
print("abc".isalpha())  # Output: True (alphabets only)
print("   ".isspace())  # Output: True (whitespace only)
print(string.startswith("Hello"))  # Output: True
print(string.endswith("!"))  # Output: True

# Splitting and joining
splitted = string.split(", ")  # Split by ", "
print(splitted)  # Output: ['Hello', 'World!']
print(", ".join(splitted))  # Output: Hello, World!

# Trimming
whitespace_string = "   Hello, World!   "
print(whitespace_string.strip())  # Output: Hello, World!
print(whitespace_string.lstrip())  # Output: Hello, World!   (left trimmed)
print(whitespace_string.rstrip())  # Output:    Hello, World! (right trimmed)

# Formatting
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # Old style
print(f"My name is {name} and I am {age} years old.")  # f-strings (new style)

# Padding
print("42".zfill(5))  # Output: 00042 (pad with zeros)
print("Hello".center(10, "-"))  # Output: --Hello---
print("Hello".ljust(10, "-") + "!")  # Output: Hello-----!
print("Hello".rjust(10, "-") + "!")  # Output: -----Hello!

# Partitioning
print(string.partition(","))  # Output: ('Hello', ',', ' World!')

# =============================
# 3. Slicing and Indexing
# =============================
# Access characters by index
print(string[0])  # Output: H
print(string[-1])  # Output: !

# Slice strings
print(string[0:5])  # Output: Hello
print(string[7:])  # Output: World!
print(string[::-1])  # Output: !dlroW ,olleH (reversed string)

# =============================
# 4. Advanced Techniques
# =============================
# Unicode functions
print(ord("A"))  # Output: 65 (Unicode value of 'A')
print(chr(65))  # Output: A (Character for Unicode 65)

# String encoding and decoding
encoded = string.encode("utf-8")
print(encoded)  # Output: b'Hello, World!' (bytes)
print(encoded.decode("utf-8"))  # Output: Hello, World! (back to string)

# =============================
# 5. Regular Expressions (Optional)
# =============================
import re
pattern = r"\bWorld\b"
match = re.search(pattern, string)
if match:
    print("Match found at index:", match.start())  # Output: Match found at index: 7
