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


class Owner(Employee):
	def __init__(self, first_name, last_name, role, company_name):
		super(Owner, self).__init__(first_name, last_name, role)
		self.first_name = first_name
		self.last_name = last_name
		self.role = role
		self.company_name = company_name

	def introduction(self):
		print(self.first_name + ' ' + self.last_name + ' as ' + self.role + ' owns ' + self.company_name)


person = Person('Dummy', 'Person')
person.introduction()

employee = Employee('Dummy', 'Person', 'Software Engineer')
employee.introduction()

owner = Owner('Dummy', 'Person', 'CEO', 'MyOrganization')
owner.introduction()
