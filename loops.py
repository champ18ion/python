# for loops
# The for loop is used to iterate over items and execute code on each item. 
# It has two keywords, for and in, which are used to describe the element and the object that is being iterated over, respectively. 
# The indentation after : starts the body of the loop.

# In the example below, the for loop is iterating over the list nums. For each item in num, it is printing the output of num + 1.

nums = [1,2,3,4,5]

for num in nums:
    print(num + 1)

# for loops with range()
# The range() function can be used with the for loop to execute a block of code multiple times.
# The code below iterates between numbers 0 to 2 and prints each number.

for num in range(3):
    print(num)

# Nested for loops
# A for loop can have nested for loops. This is particularly useful if the items you are iterating over contain subitems. 
# In the example below, we have a list of lists called teams and we can use a nested for loop to print each name in the lists.

teams = ['Real Madrid', 'Barcelona', ['fc goa','mumbai city fc'], 'Liverpool', 'Chelsea']

for team in teams:
    for player in team:
        print(player)


# while loop
# The while loop is used to execute code while its condition evaluates to be True.
# It has two keywords, while and if, which are used to describe the condition and the code that will be executed, respectively.
# In the example below, the while loop will run and print i as long as the value of i is less than 6.

i=1
while i<= 5:
    print('tere to L lag gaye')
    i+=1