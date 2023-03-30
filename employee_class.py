# Programmer: Noah Bird
# Date: 4/20/21-first coded
# Goal: Write a class named Employee that holds the following data about an employee in attributes: Name, ID number, Department, Job title.
# Include accessor and mutator methods for each attribute
# Then, write a program that presents a menu to let the user perform the following actions until user slects quit
# aka Add a new employee to the directory, look up an employee in the dictionary, change an existing employees name, department, and job title in dictionary
# delete an employee from the directory and to quit the program

class Employee:
	def __init__(self, name, id_number,department,job_title):
		self.name = name
		self.id_number = id_number
		self.department=department
		self.job_title=job_title

	def set_name(self,val):
		self.name=val

	def set_id_number(self,val):
		self.id_number=val

	def set_department(self,val):
		self.department=val

	def set_job_title(self,val):
		self.job_title=val

	def __str__(self):
		return "Name:"+self.name+"\n"+"Department:"+self.department+"\n"+"Job title:"+self.job_title+"\n"

data=dict()
def Add():
	n=input("Name: ")
	i=input("ID number: ")
	d=input("Department: ")
	j=input("Job title: ")
	obj=Employee(n,i,d,j)
	if i in data.keys():
		print("ID already exists!!")
	else:
		data[i]=obj

def Look():
	i=input("ID number: ")
	if i in data.keys():
		print(data[i])
	else:
		print("ID not found!")

def Change():
	i=input("ID number: ")
	if i in data.keys():
		print("Enter values to update")
		n=input("Name: ")
		data[i].set_name(n)
		d=input("Department: ")
		data[i].set_department(d)
		j=input("Job title: ")
		data[i].set_job_title(j)
	else:
		print("ID not found!")

def Del():
	i=input("ID number: ")
	if i in data.keys():
		del data[i]
	else:
		print("ID not found!")
while True:
	print("\nEnter A to Add a new employee\nEnter L to Look up a new employee\nEnter C to change employee's details\nEnter D to Delete a new employee\nEnter Q to Quit the program\n")
	ch=input("~ ")
	if ch=='a'or ch=='A':
		Add()
		print()
	if ch=='l'or ch=='L':
		Look()
		print()
	if ch=='c'or ch=='C':
		Change()
		print()
	if ch=='d' or ch=='D':
		Del()
	if ch=='q' or ch=='Q':
		print("Goodbye!!")
		break