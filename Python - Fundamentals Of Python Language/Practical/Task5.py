# Practical Example 1: Write a Python program to print each fruit in a list using a simple for
# loop. List1 = ['apple', 'banana', 'mango']/
# List1 = ['apple', 'banana', 'mango']
# for i in List1:
#     print(i)
# Practical Example 2: Write a Python program to find the length of each string in List1.
# List1 = ['apple', 'banana', 'mango']
# for i in List1:
#     print(len(i))
# Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition
# List1 = ['apple', 'banana', 'mango']
# search = 'banana'

# for i in List1:
#     if i == search:
#         print("Found:", i)
# Practial Example 4:Practical Example 4: Print this pattern using nested for loop:
# markdown
# Copy code
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

