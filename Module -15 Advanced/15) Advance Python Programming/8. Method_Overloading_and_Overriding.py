
# Write Python programs to demonstrate method overloading and method overriding
# class Calculator:

#     # Overloaded method using *args
#     def add(self, *nums):
#         result = 0
#         for n in nums:
#             result += n
#         return result


# # Object creation
# c = Calculator()

# print("Add 2 numbers:", c.add(5, 10))
# print("Add 3 numbers:", c.add(5, 10, 20))
# print("Add 5 numbers:", c.add(1, 2, 3, 4, 5))

# class Animal:
#     def sound(self):
#         print("Animals make different sounds")

# class Dog(Animal):
#     # Overriding the parent method
#     def sound(self):
#         print("Dog barks")

# # Object creation
# a = Animal()
# d = Dog()

# a.sound()   # Parent class method
# d.sound()   # Overridden method

# Method Overridding
# class Animal:
#     def sound(self):
#         print("Animals make different sounds")

# class Dog(Animal):
#     # Overriding the parent method
#     def sound(self):
#         print("Dog barks")

# # Object creation
# a = Animal()
# d = Dog()

# a.sound()   # Parent class method
# d.sound()   # Overridden method



# Practical Example
# Write a Python program to show method overloading
# class MathOperations:
#     # Single method that behaves like overloaded method
#     def add(self, *numbers):
#         total = 0
#         for n in numbers:
#             total += n
#         return total

# # Creating object
# m = MathOperations()

# # Calling the same method with different number of arguments
# print("Add 2 numbers:", m.add(10, 20))
# print("Add 3 numbers:", m.add(10, 20, 30))
# print("Add 5 numbers:", m.add(1, 2, 3, 4, 5))

# Write a
# Python program to show method overriding
# class Animal:
#     def sound(self):
#         print("Animals make different sounds")

# class Dog(Animal):
#     # Overriding the parent class method
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     # Overriding again
#     def sound(self):
#         print("Cat meows")


# # Creating objects
# a = Animal()
# d = Dog()
# c = Cat()

# a.sound()   # Parent class method
# d.sound()   # Overridden method (Dog)
# c.sound()   # Overridden method (Cat)



