'''
for i in reversed(range(1, 6)):
	for j in range(i):
		print('*', end='')
	for j in range(5 - i):
		print(' ', end='')
	for j in range(i):
		print('*', end='')
	print()
for i in range(1, 6):
	for j in range(i):
		print('*', end='')
	for j in range(5 - i):
		print(' ', end='')
	for j in range(i):
		print('*', end='')
	print()
'''

for i in reversed(range(1, 11)):
	half = i // 2
	for j in range(i):
		print('*', end='')
	for j in range(5 - i):
		print(' ', end='')
	for j in range(i):
		print('*', end='')
	print()