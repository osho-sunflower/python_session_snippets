class A:
	def __str__(self):
		return 'printing from A'


class B:
	def __str__(self):
		return 'printing from B'


class C(A, B):
	pass


a = A()
print(a)

b = B()
print(b)

c = C()
print(c)
