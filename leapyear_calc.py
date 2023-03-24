# Programmer: Noah Bird
# Date: 2/23/21-first coded
# Output: Create a program to display number of days in February based on the year

# ask user to enter a year
year = int(input('Please enter any year of your choice: '))

# calculate if that year would be considered a leap year
# then display number of days in February for that year 

if (year % 100) == 0:
	if(year % 400) == 0:
		print(format(year),' is a leap year')
		print('February in ', format(year), ' has 29 days.')
	else:
		print(format(year),' is not a leap year')
		print('February in ', format(year), ' has 28 days.')

elif (year % 100) != 0:
	if(year % 4) == 0:
		print(format(year),' is a leap year')
		print('February in ', format(year), ' has 29 days.')
	else:
		print(format(year),' is not a leap year')
		print('February in ', format(year), ' has 28 days.')