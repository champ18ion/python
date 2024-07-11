
# try and except
# The clause try attempts to execute a block of code and except executes another block of code if try fails.

nums = [0, 1, 2, '3']

try:
    print(sum(nums))
except:
    print('Cannot print the sum! Your variables are not numbers.')

# finally
# The finally clause executes a block of code regardless of which clause, try or except, was executed. 
# The finally clause is useful in cases where both of your try and except might fail.

ints = [1,2,'s', 9]
try:
    print(sum(ints))
except:
    print('Kuch to gadbad hai')
finally:
    print('itne me itna ich milega')