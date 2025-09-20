# Write a Python program to demonstrate the creation of variables and different data types.
# Integer
# age = 25
# print("Age:", age, "| Data type:", type(age))

# # Float
# price = 19.99
# print("Price:", price, "| Data type:", type(price))

# # String
# name = "Alice"
# print("Name:", name, "| Data type:", type(name))

# # Boolean
# is_student = True
# print("Is Student:", is_student, "| Data type:", type(is_student))

# # List (ordered, mutable)
# fruits = ["apple", "banana", "cherry"]
# print("Fruits:", fruits, "| Data type:", type(fruits))

# # Tuple (ordered, immutable)
# coordinates = (10.5, 20.3)
# print("Coordinates:", coordinates, "| Data type:", type(coordinates))

# # Set (unordered, unique values)
# unique_numbers = {1, 2, 3, 3, 2}
# print("Unique Numbers:", unique_numbers, "| Data type:", type(unique_numbers))

# # Dictionary (key-value pairs)
# student = {"name": "Alice", "age": 25, "grade": "A"}
# print("Student Info:", student, "| Data type:", type(student))

# Practical Example 1: How does the Python code structure work?

"""
Program: Add Two Numbers
This program shows a simple Python code structure with:
- Comments
- Variables
- Input/Output
- Indentation
"""

# Step 1: Create variables and take input
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # Step 2: Process (calculate sum)
# total = num1 + num2

# # Step 3: Output result
# print("The sum of", num1, "and", num2, "is:", total)

# Practical Example 2: How to create variables in Python?


# # Integer variable
# age = 20
# print("Age:", age)

# Practical Example 3: How to take user input using the input() function.


# Take string input
# name = input("Enter your name: ")
# print("Hello,", name)

# # Take integer input
# age = int(input("Enter your age: "))  # convert input string to integer
# print("You are", age, "years old.")

# # Take float input
# height = float(input("Enter your height in meters: "))  # convert to float
# print("Your height is", height, "meters.")


# Practical Example 4: How to check the type of a variable dynamically using type()
name = "Alice"       # string
age = 20             # integer
height = 5.8         # float
is_student = True    # boolean

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))