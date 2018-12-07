class A:
	def __str__(self):
		return 'printing from A'


class B(A):
	pass


class C(A):
	def __str__(self):
		return 'printing from C'


class D(B, C):
	pass


d = D()
print(d)


# python2 (for old-style class) - depth-first, left-to-right
# python2 (inherits from object) - breadth-first, left-to-right
# python3 - breadth-first, left-to-right
