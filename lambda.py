# A lambda function in Python is a simple, anonymous function that is defined without a name. 
# In this article, we’ll cover the syntax and characteristics of lambda functions.

# Lambda Function Syntax
# Regular functions in Python are defined with the def keyword and a custom name. In contrast, lambda functions are defined with the lambda keyword without a name. This is the syntax to define lambda functions:

# lambda argument(s): expression

# A lambda function can have multiple arguments but only one expression, and is usually contained within one line of code. 
# Let’s see an example of a lambda function:

add_two = lambda x: x + 2

# In the example above, x is the argument and x + 2 is the expression. Assigning the lambda function to the variable add_two, we can call the function using add_two(). 
# This function is still considered anonymous because it is not defined as a standard function with def:

add_two(5)

sum = lambda y,z: y+z
print(sum(2,13))

# Why Use Lambda Functions?
# Lambda functions are typically used in the following scenarios:

# When we want to write a quick function with one line
# When we want to combine with other built-in functions such as map(), filter(), and apply() to filter for data
