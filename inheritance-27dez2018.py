class Parent():
	def __init__(self, last_name, eye_color):
		print("parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("last name - " + self.last_name)
		print("eye color - " + self.eye_color)

class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print("child constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	def show_info(self):
		print("last name -" + self.last_name)
		print("eye color -" + self.eye_color)
		print("number of toys -" + str(self.number_of_toys))

billy_cyrus = Parent("curys", "blue")
#billy_cyrus.show_info()

miley_cyrus = Child("cyrus", "blue", 5)
miley_cyrus.show_info()