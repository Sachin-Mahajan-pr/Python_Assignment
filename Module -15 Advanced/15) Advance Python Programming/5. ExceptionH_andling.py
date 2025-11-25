# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
# input).

# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     op = input("Enter operator (+, -, *, /): ")

#     if op == "+":
#         print(a + b)
#     elif op == "-":
#         print(a - b)
#     elif op == "*":
#         print(a * b)
#     elif op == "/":
#         try:
#             print(a / b)
#         except ZeroDivisionError:
#             print("Error: Cannot divide by zero")
#     else:
#         print("Invalid operator")

# except ValueError:
#     print("Invalid input. Please enter numbers only.")

# Write a Python program to demonstrate handling multiple exceptions.

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a / b)

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# except ValueError:
#     print("Error: Please enter only numbers.")

# except Exception as e:
#     print("Some other error occurred:", e)

# Practical Example
# Write a Python program to handle exceptions in a calculator

# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     op = input("Enter operator (+, -, *, /): ")

#     if op == "+":
#         print(a + b)
#     elif op == "-":
#         print(a - b)
#     elif op == "*":
#         print(a * b)
#     elif op == "/":
#         try:
#             print(a / b)
#         except ZeroDivisionError:
#             print("Error: Cannot divide by zero.")
#     else:
#         print("Invalid operator.")

# except ValueError:
#     print("Error: Please enter valid numbers.")

# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

# try:
#     f = open("data.txt", "r")
#     print(f.read())
#     f.close()

#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a / b)

# except FileNotFoundError:
#     print("Error: File not found.")

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# except ValueError:
#     print("Error: Please enter valid numbers.")

# except Exception as e:
#     print("Some other error occurred:", e)

# Write a Python program to handle file exceptions and use the finally block for closing
# the file

# try:
#     f = open("info.txt", "r")
#     data = f.read()
#     print(data)

# except FileNotFoundError:
#     print("Error: The file does not exist.")

# except Exception as e:
#     print("Some error occurred:", e)

# finally:
#     try:
#         f.close()
#         print("File closed successfully.")
#     except:
#         print("File was never opened.")

#  Write a Python program to print custom exceptions.

class MyError(Exception):
    pass

try:
    value = int(input("Enter a positive number: "))
    if value < 0:
        raise MyError("This is a custom exception: Number cannot be negative.")
    print("You entered:", value)

except MyError as e:
    print(e)

except ValueError:
    print("Please enter a valid number.")


