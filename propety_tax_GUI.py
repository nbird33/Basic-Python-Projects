# Programmer: Noah Bird
# Date: 4/27/21-first coded
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Output: write a GUI program that displays the assessment value and property tax when a user enters the market value of a property

# Future update plans: assessment value and propetry tax values must be changed in code 
# an update to the code could be asking user if they know what the local property tax rates are / the how they are judging the assessment value

import tkinter

class taxConverterGUI:
	def __init__(self):

		# create the main window
		self.main_window = tkinter.Tk()

		# create three frames to group widgets
		self.top_frame = tkinter.Frame()
		self.mid_frame = tkinter.Frame()
		self.bottom_frame = tkinter.Frame()

		# create the widgets for the top frame
		self.prompt_label = tkinter.Label(self.top_frame,
										  text='Enter the property value: $')
		self.value_entry = tkinter.Entry(self.top_frame,
									     width=10)

		# pack the top frames widgets
		self.prompt_label.pack(side='left')
		self.value_entry.pack(side='left')

		# create the widgets for the middle frame
		self.assessment_label = tkinter.Label(self.mid_frame,
											  text='Assessment Value: ')
		self.proptax_label = tkinter.Label(self.mid_frame,
											  text='Property Tax: ')

		self.value1 = tkinter.StringVar()
		self.value2 = tkinter.StringVar()
		self.answer1_label = tkinter.Label(self.mid_frame,
										  textvariable=self.value1)
		self.answer2_label = tkinter.Label(self.mid_frame,
										  textvariable=self.value2)

		# pack the middle frames widgets
		self.assessment_label.pack(side='left')
		self.answer1_label.pack(side='left')
		self.proptax_label.pack(side='left')
		self.answer2_label.pack(side='left')


		# create the button widgets for the bottom frame
		self.calc_button = tkinter.Button(self.bottom_frame,
										  text='Calculate',
										  command=self.calculate)
		self.quit_button = tkinter.Button(self.bottom_frame,
										  text='Quit',
										  command=self.main_window.destroy)

		# pack the buttons
		self.calc_button.pack(side='left')
		self.quit_button.pack(side='left')

		# pack the frames
		self.top_frame.pack()
		self.mid_frame.pack()
		self.bottom_frame.pack()

		# enter the tkinter main loop
		tkinter.mainloop()

		# the calculate method is a callback function for calcuate button
	def calculate(self):
		# get the value entered by the user in the value_entry widget
		prop_value = float(self.value_entry.get())

		assessment_value = prop_value * 0.60

		prop_tax = ((assessment_value / 100.00) * .75)

		self.value1.set(assessment_value)
		self.value2.set(prop_tax)

myGui = taxConverterGUI()






