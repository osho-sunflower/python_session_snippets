# import arithmetic
#
# content = dir(arithmetic)
# print(content)
#
# print('1 + 2 = ', arithmetic.add(1, 2))
# print('5 - 2 = ', arithmetic.subtract(5, 2))
# print('13 * 9 = ', arithmetic.multiply(13, 9))
# print('6 / 2 = ', arithmetic.divide(6, 2))

# from arithmetic import NumberOperations
#
# number_operation = NumberOperations(4, 2)
# print('4 + 2 = ', number_operation.add())
# print('4 - 2 = ', number_operation.subtract())
# print('4 * 2 = ', number_operation.multiply())
# print('4 / 2 = ', number_operation.divide())

# Creates a 1 GB TXT
input_file = open('SampleTextFile.txt', 'r')
repeat_content = input_file.read()
input_file.close()

output_file = open('output.txt', 'w')
for i in range(100000):
	print(i)
	output_file.write(repeat_content + '\n')
output_file.close()

# file = open('output.txt', 'r', 10)
# print(file.read(10))
