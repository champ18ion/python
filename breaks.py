# pass braek and continue


# pass
# The pass keyword is mostly used as a placeholder in a loop. Nothing gets executed when pass is placed under a condition.
scores = [23,75,91,39,119,47,78]
for score in scores:
    if score in range(60):
        print('aise to nahi hoga bro',score)
    elif score<=80:
        pass
    else:
        print('jalwa hai humara yahan',score)

# Break
# The break keyword terminates a loop. break statements are typically found within conditional statements.
# If a certain condition is met, the loop stops iterating and breaks at that point.

marks = [20,66,54,98,73,83,38,75]
for mark in marks:
    if mark<=50:
        print('way to go')
    elif mark>=90:
        print('meri selection ho gayi')
        break
    else:
        print('Binod')

# Continue
# The continue keyword skips over an iteration if the condition is met and goes onto the next iteration. 
# The difference between the continue keyword and pass is that continue goes onto the next iteration while pass simply does not do anything.

scores = [23,75,91,39,119,47,78]
for score in scores:
    if score in range(60):
        print('aise to nahi hoga bro',score)
    elif score<=80:
        continue
    else:
        print('jalwa hai humara yahan',score)

        