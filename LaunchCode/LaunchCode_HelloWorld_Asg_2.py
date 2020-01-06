#  ---------------------- Even Steven -------------------------
# INSTRUCTIONS
# For each number between 1 and 100...
# 	If the number is odd, then simply print it out.
# 	BUT if the number is even, then print the word "Steven" instead.
# When I run your program, I should see the following output:
# 	1
# 	Steven
# 	3
# 	Steven
#	5
# 	...
#	97
#	Steven
#	99
#	Steven
# Note that you should start at 1 (not 0), and that the 100 must be INCLUDED.
# In other words, the last number should be 100, not 99.
# --------------------------------------------------------------------
# Put your Python code here:
## Create list of numbers
numbers = range(1, 101)

for number in numbers:
    if number % 2 == 0:
        print("Steven")
    else:
        print(number)