class Person:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def introduction(self):
		print(self.first_name + ' ' + self.last_name)


class Employee(Person):
	def __init__(self, first_name, last_name, role):
		super(Employee, self).__init__(first_name, last_name)
		self.first_name = first_name
		self.last_name = last_name
		self.role = role

	def introduction(self):
		print(self.first_name + ' ' + self.last_name + ' as ' + self.role)


person = Person('Dummy', 'Person')
person.introduction()

employee = Employee('Dummy', 'Person', 'Software Engineer')
employee.introduction()
