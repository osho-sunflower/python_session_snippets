class Person:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def name(self):
		print(self.first_name + ' ' + self.last_name)


person = Person('Dummy', 'Person')
person.name()
