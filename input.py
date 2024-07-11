# this one is about inputs and outputs in python

# How do we ask for user input as a part of our program? Python has a built-in function called input() that takes in the user’s input. 
# In the example below, we use the input() function to ask the user for their name:

input('what is your favourite anime')
anime = input('what is your favourite anime')
print(anime)

# using multiple variables in a print statement
name = 'champ18ion'
waifu = 'honami ichinose'

print(name,'likes',waifu,'as her waifu')

# You can also use + to concatenate variables and strings in the print() statement as long as your variables are strings:

print('My name is ' + name + ' and my favorite waifu is ' + waifu)

# Formatted String Literals
# You could also use formatted string literals by starting the print argument with f and inserting a Python expression between { and }.

print(f'Very nice to meet you, {name}!')

# This example would print the name in all uppercase:

print(f'Very nice to meet you, {name.upper()}!')

# str.format()
# Python also has a built-in function called str.format() that can be used with the print() function.

print('My name is {} and my favorite waifu is {}'.format(name,waifu))