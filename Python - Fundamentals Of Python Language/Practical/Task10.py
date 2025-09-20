#  Write a Python program to apply the map() function to square a list of numbers
# numbers = [1, 2, 3, 4, 5]

# squared = list(map(lambda x: x**2, numbers))

# print(squared)

# Write a Python program that uses reduce() to find the product of a list of numbers.
# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# product = reduce(lambda x, y: x * y, numbers)

# print(product)

# Write a Python program that filters out even numbers using the filter() function

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# print(even_numbers)

# Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# system.

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input(f"Enter marks for {name}: "))
    grade = calculate_grade(marks)
    students[name] = {"marks": marks, "grade": grade}

print("\nStudent Grades:")
for name, info in students.items():
    print(f"{name}: Marks = {info['marks']}, Grade = {info['grade']}")

