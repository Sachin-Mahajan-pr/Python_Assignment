# Write a generator function that generates the first 10 even numbers.
# def even_numbers():
#     n = 0
#     for i in range(10):
#         yield n
#         n += 2

# for i in even_numbers():
#     print(i)
# Write a Python program that uses a custom iterator to iterate over a list of integers.
List1 = [10, 20, 30, 40, 50]

it = iter(List1)

for i in it:
    print(i)

