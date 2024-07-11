# # Variables in python
# - Variables are containers for storing data values
# - Variables can be used to store multiple data values in one single variable

# You can declare a variable using the following syntax:

# variable_name = value
# Here, variable_name is the name of the variable and value is the value of the variable.
name = 'grace'
temperature = 98.6
sum = 1 + 2

# casting
# You may sometimes want to specify the type of the variable using built-in data types in Python.
# For example, I may want to store a numerical value as a string, which can be done by using the constructor function str() like this:

temperature = str(temperature)

# The function str() takes a value and converts it into a string. 
# There are other functions such as int(), float() and bool() which we will cover in our next article.

# If you need to access the data type of a variable, you can simply use the built-in function type() to print the variable’s type.
type(temperature) # prints <class 'str'>