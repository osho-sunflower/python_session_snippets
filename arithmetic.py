def add(num1, num2):
	return num1 + num2


def subtract(num1, num2):
	return num1 - num2


def multiply(num1, num2):
	return num1 * num2


def divide(num1, num2):
	if num2 == 0:
		return 'undefined'
	else:
		return num1 / num2

class NumberOperations:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def add(self):
		return self.num1 + self.num2

	def subtract(self):
		return self.num1 - self.num2

	def multiply(self):
		return self.num1 * self.num2

	def divide(self):
		if self.num2 == 0:
			return 'undefined'
		else:
			return self.num1 / self.num2


# If this file is executed, following code block will be executed
if __name__ == '__main__':
	print('welcome to arithmetic module')
	print('resources: ', dir())