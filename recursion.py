# The word recursion in Python describes the process of repeatedly calling a function within itself. 
# In this article, we’ll cover how to use recursion with functions and why we use them.

# A Recursive Function
# Let’s take a look at what a recursive function looks like:

def factorial(num):
   if num == 1:
       return 1
   else:
       return num * factorial(num-1)
   
#  Taking the function factorial from above,
#  let’s do a slight modification to implement a call stack that will help to visualize the recursion.
#  Take a look at what happens if we call factorial(5):

def factorial(num):
   call_stack = []
   if num == 1:
       print('base case reached! Num is 1.')
       return 1
   else:
       call_stack.append({'input': num})
       print('call stack: ', call_stack)
       return num * factorial(num-1)
 
factorial(5)
 
# call stack:  [{'input': 5}]
# call stack:  [{'input': 4}]
# call stack:  [{'input': 3}]
# call stack:  [{'input': 2}]
# base case reached! Num is 1.
# 120
