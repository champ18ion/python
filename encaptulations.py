# In object-oriented programming (OOP), encapsulation is a fundamental concept that describes wrapping variables and methods in one unit.

# A popular example of encapsulation is a class, as it “encapsulates” members such as variables and methods in one single unit. 
# In this article, we’ll explore different members of a class.

# Class Variables
# A class can contain variables that can only be accessed by an object of the class. 
# The example below shows the class UserInfo with a constructor that takes in variables username and email_address:

class UserInfo:
   def __init__(self, username, email_address):
       self.username = username
       self.email_address = email_address
user = UserInfo('user123', 'abc@edf.ghi')
 
user.username
user.email_address

# The data saved in the object can be accessed using the variables. 
# For example, calling user.username will return ’user123’, and calling user.email_address will return ’abc@efd.ghi’.

# Class Methods
# A class can also contain methods that can be accessed by objects of the class. 
# The example below shows the class UserInfo with the method check_username that checks whether a username is saved in the object or not:

class UserInfo:
   def __init__(self, username, email_address):
      self.username = username
      self.email_address = email_address
 
   def check_username(self, username_to_check):
       if username_to_check == self.username:
           return True
       else:
           return False

# We can call the method check_username on our object to run the method:

user = UserInfo('user123', 'abc@edf.ghi')
 
user.check_username('user123') # returns True
user.check_username('user456') # returns False