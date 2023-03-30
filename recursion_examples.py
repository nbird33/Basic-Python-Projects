# Programmer: Noah Bird
# Date: 5/4/21-first coded
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Goal: Write a recursive function that accepts an integer argument, n. 
# The function should display n lines of asterisks on the screen, with the first line showing 1 asterisk
# the second line showing 2 asterisks, up to the nth line which shows n asterisks.

def printLine(n):
	if n>0:
		print("*",end="")
		printLine(n-1)
	else:
		print()
        
def printPattern(n):
	if n>0:
		printPattern(n-1)
		printLine(n)

# ask user how many lines they want to display with asterisks
n = int(input('How many lines to display? '))
printPattern(n)

# another recursive function that displays nth number in the fibinacci sequence
def fibonacci(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci(m-1) + fibonacci(m-2)
    
m = int(input("Enter selected place/index in fibinacci sequence to display its corresponding number: "))
answer = fibonacci(m)
print(f"The {m}th number in the fibonacci sequence = {answer}")
