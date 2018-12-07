## Numbers
print('Numbers -------------------------------------------------------------------------------------------------------')
# int
number = 5
print(number, 'is of type', type(number))

# float
number = 2.56
print(number, 'is of type', type(number))

# complex
number = 2 + 3j
print(number, 'is of type', type(number))

print('\n')

## Strings - Immutable with characters
print('Strings -------------------------------------------------------------------------------------------------------')

string = 'Hello world!'
print(string, 'is of type', type(string))
'''
	H   e   l   l   o       w   o   r   l   d   !
	0   1   2   3   4   5   6   7   8   9   10  11
	-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
'''
print('s[4] =', string[4])
print('s[-5] =', string[-5])
print('s[-8:-3] =', string[-8:-3])
print('s[2:7] =', string[2:7])
print('s[:5] =', string[:5])
print('s[6:] =', string[6:])

try:
	string[11] = '?'
except TypeError as type_error:
	print(type_error)

print('\n')

## Lists - Ordered, Mutable
print('Lists ---------------------------------------------------------------------------------------------------------')
list_similar = [1, 2, 3, 4, 5]
list_mixed = [1, 2.3, 1 + 3j, 'text']

print(list_similar, 'is of type', type(list_similar))
print(list_mixed, 'is of type', type(list_mixed))

print('list_similar[4] =', list_similar[4])
print('list_similar[1:3] =', list_similar[1:3])
print('list_similar[:2] =', list_similar[:2])
print('list_similar[3:] =', list_similar[3:])

print('list_mixed[2] =', list_mixed[2])
print('list_mixed[1:3] =', list_mixed[1:3])
print('list_mixed[:2] =', list_mixed[:2])
print('list_mixed[2:] =', list_mixed[2:])

list_similar[0] = 6
print('updated list_similar[0] =', list_similar[0])

print('\n')

## Tuples - Ordered, Immutable
print('Tuples --------------------------------------------------------------------------------------------------------')
tuple = (23, 'text', 5.78, 4 + 2j)
print(tuple, 'is of type', type(tuple))

print('tuple[2] =', tuple[2])
print('tuple[1:3] =', tuple[1:3])
print('tuple[:2] =', tuple[:2])
print('tuple[2:] =', tuple[2:])

try:
	tuple[1] = 'new text'
except TypeError as type_error:
	print(type_error)

print('\n')

## Sets - Unordered
print('Sets ----------------------------------------------------------------------------------------------------------')
set = {23, 'text', 5.78, 4 + 2j, 23}
print(set, 'is of type', type(set))
print('set =', set)

print('\n')

## Dictionary - Mutable
print('Dictionary ----------------------------------------------------------------------------------------------------')
dictionary = {1: 'value', 'two': 5}
print(dictionary, 'is of type', type(dictionary))

print('dictionary[1] = ', dictionary[1])
print("dictionary['two'] = ", dictionary['two'])

dictionary[1] = 'new value'
print('updated dictionary[1] = ', dictionary[1])
