# Programmer: Noah Bird
# Date: 2/16/21-first coded
# Output : make user use change to create a dollar

# change counting game to make 1 dollar
print('Enter correct amount of change to equal one dollar... ')

# get number of quarters from user
total_quarters = float(input('Enter a number of quarters: '))

# get number of dimes
total_dimes = float(input('Enter a number of dimes: '))

# get number of nickels
total_nickels = float(input('Enter a number of nickels: '))

# get number of pennies
total_pennies = float(input('Enter a number of pennies: '))

# get price of quarters and other coins
quarters = total_quarters * 0.25
dimes = total_dimes * 0.10
nickels = total_nickels * 0.05
pennies = total_pennies * 0.01

# total price
total = quarters + dimes + nickels + pennies

# if total value is less than or greater than 1 dollar, tell the user and they lost
# if total value is equal to 1 dollar congratulate user on winning game 
dollar = 1.00

if total == dollar:
	print('Congratulations, your value equal one dollar, You Won!!')

elif total > dollar:
	print('Your total is greater than one dollar, you lost :( ')

else:
	print('Your total is less than one dollar, you lost :( ')

print('Goodbye!')




