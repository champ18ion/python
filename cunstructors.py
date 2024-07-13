# In object-oriented programming (OOP), constructors are functions that are called when an object of a class is created and destructors are called to delete an object. 

# Constructors
# Constructors are special functions that are executed when an object is instantiated. 
# In Python, the __init__() function is used as the constructor and is called when creating an object.

# init()
# It is common practice for classes to contain Python’s built-in __init__() method as the constructor. 
# In the example below, the __init__() method would be called every time the ClassSchedule class is instantiated, and used to initialize a newly created object:
 
class Car:
    def __init__(self,door) -> None:
        self.door = door
        pass

# Instance Variables
# The self parameter in the __init__() method refers to the current instance and the instance variable course allows for input to assign a value. 
# We can create a class instance by calling the class and inputting the value for door. Let’s create an instance with the instance variable 4 and assign it to an object named myCar:

myCar = Car(4)
print(myCar.door)

# Destructors
# Destructors are special functions that are called when an object gets deleted. 
# In Python, the __del__() method is commonly used as the destructor and is called when an object is deleted.
# 
# del()
# Python’s built-in __del__() method represents the destructor in a class. 
# In the example below, the __del__() method would be called every time an object initiated from the Car class is deleted.

class Car:
    def __init__(self,door) -> None:
        self.door = door
        pass

    def __del__(self) -> None:
        print('Car deleted successfully')
        pass

# The self parameter in the __del__() method refers to the current object. 
# Triggering this method by deleting the object will execute the print() statement. So, if we use del to delete the lambo object as such:

lambo = Car(4)
del lambo