# Write Python programs to demonstrate different types of inheritance (single, multiple,
# multilevel, etc.).
# 1. Single Inheritance
# class A:
#     def showA(self):
#         print("This is class A")

# class B(A):
#     def showB(self):
#         print("This is class B")

# obj = B()
# obj.showA()
# obj.showB()

# 2. Multilevel Inheritance
# class A:
#     def showA(self):
#         print("This is class A")

# class B(A):
#     def showB(self):
#         print("This is class B")

# class C(B):
#     def showC(self):
#         print("This is class C")

# obj = C()
# obj.showA()
# obj.showB()
# obj.showC()

# 3. Multiple Inheritance
# class A:
#     def showA(self):
#         print("This is class A")

# class B:
#     def showB(self):
#         print("This is class B")

# class C(A, B):
#     def showC(self):
#         print("This is class C")

# obj = C()
# obj.showA()
# obj.showB()
# obj.showC()

# 4. Hierarchical Inheritance
# class A:
#     def showA(self):
#         print("This is class A")

# class B(A):
#     def showB(self):
#         print("This is class B")

# class C(A):
#     def showC(self):
#         print("This is class C")

# obj1 = B()
# obj2 = C()

# obj1.showA()
# obj2.showA()

# 5. Hybrid Inheritance

# Hybrid = Combination of more than one type (example: hierarchical + multiple)

# class A:
#     def showA(self):
#         print("This is class A")

# class B(A):
#     def showB(self):
#         print("This is class B")

# class C(A):
#     def showC(self):
#         print("This is class C")

# class D(B, C):
#     def showD(self):
#         print("This is class D")

# obj = D()
# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()

# Practical Example

# Write a Python program to show single inheritance
# class Parent:
#     def displayParent(self):
#         print("This is the parent class")

# class Child(Parent):
#     def displayChild(self):
#         print("This is the child class")

# obj = Child()
# obj.displayParent()
# obj.displayChild()

# Write a
# Python program to show multilevel inheritance. 

# class A:
#     def showA(self):
#         print("This is class A")

# class B(A):
#     def showB(self):
#         print("This is class B")

# class C(B):
#     def showC(self):
#         print("This is class C")

# obj = C()
# obj.showA()
# obj.showB()
# obj.showC()

# Write a Python program to show multiple
# inheritance

# Parent Class 1
# class Father:
#     def father_info(self):
#         print("Father: Works in an IT Company")

# # Parent Class 2
# class Mother:
#     def mother_info(self):
#         print("Mother: She is a Doctor")

# # Child Class inheriting from both Father and Mother
# class Child(Father, Mother):
#     def child_info(self):
#         print("Child: Studying in School")

# # Creating object of Child Class
# obj = Child()

# obj.father_info()   # From Father class
# obj.mother_info()   # From Mother class
# obj.child_info()    # From Child class

# Write a Python program to show hierarchical inheritance
# Parent Class
# class Animal:
#     def sound(self):
#         print("Animals make different sounds")

# # Child Class 1
# class Dog(Animal):
#     def dog_sound(self):
#         print("Dog: Woof Woof")

# # Child Class 2
# class Cat(Animal):
#     def cat_sound(self):
#         print("Cat: Meow Meow")

# # Creating objects of child classes
# d = Dog()
# c = Cat()

# print("Dog Object Output:")
# d.sound()       # From Animal
# d.dog_sound()   # From Dog

# print("\nCat Object Output:")
# c.sound()       # From Animal
# c.cat_sound()   # From Cat 

#  Write a Python
# program to show hybrid inheritance
# Parent Class
# class A:
#     def showA(self):
#         print("This is class A")

# # Class B inherits from A (Single Inheritance)
# class B(A):
#     def showB(self):
#         print("This is class B")

# # Class C inherits from A (Single Inheritance)
# class C(A):
#     def showC(self):
#         print("This is class C")

# # Class D inherits from both B and C (Multiple Inheritance)
# class D(B, C):
#     def showD(self):
#         print("This is class D")


# # Creating object of class D
# obj = D()

# obj.showA()   # From class A
# obj.showB()   # From class B
# obj.showC()   # From class C
# obj.showD()   # From class D

# Write a Python program to demonstrate the use of
# super() in inheritance.

# class Parent:
#     def display(self):
#         print("This is the Parent class")

# class Child(Parent):
#     def display(self):
#         super().display()       # Calling Parent class method
#         print("This is the Child class")


# # Creating object of Child class
# obj = Child()
# obj.display()


