# Python2       ---->       Python3
# input()       ---->       eval(input())
# raw_input()   ---->       input()

# Python3
string = input('Enter a string: ')
print('Got:', string)

number = int(input('Enter a number: '))
print('Got:', number)

expression = eval(input('Enter an expression: '))
print('Evaluated:', expression)


# # Python2
# string = raw_input('Enter a string: ')
# print('Got:', string)
#
# expression = input('Enter an expression: ')
# print('Evaluated:', expression)
