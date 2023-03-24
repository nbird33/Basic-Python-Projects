# Programmer: Noah Bird
# Date: 5/4/21-first coded
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Output: Demonstrate polymorphism in a test program by creating related objects (all three Ship types)
# and passing the objects to a function for printing their details


# Design a Ship class with...
# a field for the name of the ship, a field for the year that the ship was built
# an initializer method that accepts two arguments to initialize the two fields
# and a __str__ method that returns the object's state as a string

class Ship:
	def __init__(self, name, year):
		self.name = name
		self.year = year

	def __str__(self):
		return "Ship Name: regular ship - " + self.name + "\nShip Year: " + str(self.year)

# Design a CruiseShip class that is a subclass of the Ship class...
# it should have a field for the maximum number of passengers
# and an initializer method that accepts three arguments to initialize the three fields
# and a __str__ method that returns the object's state as a string

class CruiseShip(Ship):
	def __init__(self, name, year, passengers):
		super(CruiseShip, self).__init__(name, year)
		self.numberOfPassengers = passengers

	def __str__(self):
		return "Ship Name: cruise ship - " + self.name + "\nShip Year: " + str(self.year) + "\nMax Passengers: " + str(self.numberOfPassengers)

# Design a CargoShip class that is a subclass of the Ship class... it should have
# a field for the cargo capacity in tonnage
# an initializer method that accepts three arguments to initialize the three fields
# and a __str__ method that returns the object's state as a string

class CargoShip(Ship):
	def __init__(self, name, year, capacity):
		super(CargoShip, self).__init__(name, year)
		self.capacity = capacity

	def __str__(self):
		return "Ship Name: cargo ship - " + self.name + "\nShip year : " + str(self.year) + "\nCargo Capacity: " + str(self.capacity)

def testFunction():
	regular = Ship("Ghost ship", 1800)
	cruise = CruiseShip("Harmony", 2010, 1000)
	cargo = CargoShip("USS Antilla", 1904, 2000)

	print('\nShips created...\n')
	print(regular)
	print()
	print(cruise)
	print()
	print(cargo)

testFunction()