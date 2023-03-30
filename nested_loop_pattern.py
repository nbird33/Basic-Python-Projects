# Programmer: Noah Bird
# Date: 2/22/21-first coded
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Goal: use a nested loop to display a pattern

# ask user to input the number of rows

rows = int(input('How many rows? '))

# use a nested loop to display pattern

for r in range(rows):
	print('#', end='')
	for c in range(r):
		print(' ', end='')
	print('#')