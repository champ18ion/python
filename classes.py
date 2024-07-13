# Object-Oriented Programming (OOP) is a programming paradigm that allows for the organization of code with data states and functionalities. 
# Code with OOP is modular, abstract, and easy to maintain. In this article, we’ll cover classes and objects, which are the backbones of OOP.

# Classes
# A class is a data type that encapsulates information and functions as a blueprint for objects.
# Let’s take a look at the syntax for creating a new class:

class Dog:
   # this is a blank class
   pass

# To create a class, use the class keyword followed by the name of the class and :. 
# A new line with indentation marks the beginning of the class body.

# Objects
# An object is an instance of a class, which means the object contains everything from the class that it’s instantiated from. We can take the above class Dog and create an object named pepper as such:

pepper = Dog()
print(pepper)