# Creating a Function
# The following example shows the structure of a function in Python:

def add_three(num1, num2, num3):
   sum_three = num1 + num2 + num3
   return sum_three

# Here is a breakdown of this function:

# def is the built-in keyword in Python that is used to declare functions.
# add_three is the name of the function.
# (num1, num2, num3) is the list of parameters needed for the function.
# : indicates the start of the function body.
# sum_three = num1 + num2 + num3’ is the code in the function body followed by the indentation.
# return is the built-in keyword that exits the function and returns the output sum_three.

# Functions can be used by calling the function name with parentheses.
# Let’s try to call the function add_three that we defined above, and assign it to the variable sum_output:

sum_output = add_three(2, 4, 6)
