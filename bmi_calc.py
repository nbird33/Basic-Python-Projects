# Programmer: Noah Bird
# Date: 2/16/21-first coded
# Output : Calculate users BMI or body mass index

# get users weight
weight = float(input('Please enter your weight in pounds: '))

# get users height
height = float(input('Please enter your height in inches: '))

# display the users BMI and displays whether person has optimal weight
# or is underweight or overweight

bmi = ((weight*703) / (height**2))
print('Your BMI is', format(bmi))

if bmi > 18.5 and bmi < 25:
	print('Your weight is considered optimal.')

elif bmi < 18.5:
	print('Your weight is considered underweight...')

elif bmi > 25:
	print('Your weight is considered overweight...')

print('Thank you, have a good day!')
