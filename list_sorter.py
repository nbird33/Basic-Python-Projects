# Programmer: Noah Bird
# Date: 3/30/21-first coded
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Goal: write a program with a function that acccepts a list as an arguement
# then returns a list containing only the unique values in sorted order
# call the function with a list of numbers and a list of strings
# print original lists and lists returned by function

def main():

	# create list of numbers and list of strings
	numList = ['9', '9', '7', '7', '7', '2', '2', '4', '5', '5']
	strList = ['red', 'blue', 'blue', 'yellow', 'purple', 'purple', 'green', 'green', 'green']
	
	print('Original Numbers: ', numList)
	print('Unique Numbers Sorted: ', list_sorter1(numList))
	print(' ')
	print('Original Colors: ', strList)
	print('Unique Colors Sorted: ', list_sorter2(strList))

def list_sorter1(numList):
	return sorted(set(numList))

def list_sorter2(strList):
	return sorted(set(strList))


main()
