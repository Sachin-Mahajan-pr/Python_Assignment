# Write a Python program that demonstrates the correct use of indentation, comments, and
# variables following PEP 8 guidelines

# List of numbers
numbers = [10, 20, 30, 40, 50]

# Variable to store sum of numbers
total_sum = 0  

# Loop through each number in the list
for num in numbers:
    total_sum += num   # add current number to total

# Calculate average
average = total_sum / len(numbers)

# Display results
print("Numbers:", numbers)
print("Total Sum:", total_sum)
print("Average:", average)