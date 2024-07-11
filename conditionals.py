# if Statements

# An if statement evaluates whether the given expression is evaluated as True. 
# If the condition evaluates to be True, the code is executed. If the condition evaluates to be False, the code does not execute.
# For example, the if statement can be used to evaluate if the expression score >= 80 is True. 
# If the variable score is set as 90, because it is greater than 80, it will execute the following code with the print statement:

score = 90
 
if score >= 80:
   print('You pass the course!')

# Adding an else statement after an if statement allows for another set of code to be ran if the if statement evaluates the expression to be False.
if score >= 80:
   print('You pass the course!')
else:
   print('beta tumse na ho payega!')

# An elif statement, which is short for else if, can be added between an if statement and an else statement to evaluate for another condition.
# The code under the elif statement will only execute if the preceding if statement evaluates to be False.

if(score >= 80):
   print('cha mod diye bhaiya ji!')
elif(score >= 60):
   print('padhai Likhai karo IAS bano!')
else:
   print('beta tumse na ho payega!')