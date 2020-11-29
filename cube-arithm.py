#!/usr/bin/env python3

import sys
import operator

if sys.argv[1] == '-h':
	print(
		'''
		Cube-Arithm: A script for transforming the scalar fields in cube-files

		It can perform all kinds of operations on cube-files with numbers or
		other cube-files.

		Usage:

		./Cube-Arithm.py <Cube-File1> plus 5 (Add 5 to all entries)

		./Cube-Arithm.py <Cube-File1> times <Cube-File2>
		(Multiply all entries of the first file with the corresponding entry in the second file)

		Operations:
		plus  (+)
		minus (-)
		times (*)
		over  (/)
		pow   (**)
		fdiv  (floordiv)
		mod   (modulo)

		Note:

		If two cube-files are used, the fields have to be exactly the same and the header of
		the first file is used for the resulting cube-file.


		''')
	quit()


arg_1_string = sys.argv[1]
op_string = sys.argv[2]
arg_2_string = sys.argv[3]

operations = {
	'plus': operator.add,
	'minus': operator.sub,
	'times': operator.mul,
	'over': operator.truediv,
	'pow': operator.pow,
	'fdiv': operator.floordiv,
	'mod': operator.mod
}

def operate(string,num1,num2):
	op = operations.get(string)
	return op(num1,num2)

def get_header(file_string):
	header = []
	for _ in range(6):
		header.append(file_string.readline())
	num_at = int(header[2].split()[0])
	for _ in range(num_at):
		header.append(file_string.readline())

	return header

def write_result(is_file,op,file1,arg2,res):

	while True:
		line1 = file1.readline().split()
		if line1 == []:
			break
		# Possible to take if-statement out of loop?
		if is_file:
			line2 = arg2.readline().split()
		else:
			line2 = []
			for _ in range(len(line1)):
				line2.append(arg2)

		line3 = []
		for number1, number2 in zip(line1,line2):
			line3.append(operate(op,float(number1),float(number2)))
		for entry in line3:
			res.write("{0:13.5E}".format(entry))
		res.write("\n")

	return

if __name__ == "__main__":

	arg_1 = open(arg_1_string,'r')

	header_1 = get_header(arg_1)
	cube_field1 = header_1[3:6]

	try:
		arg_2 = open(arg_2_string,'r')
	except:
		arg_2 = arg_2_string
		arg_2_is_file = False
	else:
		header_2 = get_header(arg_2)
		cube_field2 = header_2[3:6]
		arg_2_is_file = True
	
	assert op_string in operations.keys(), "Operator not known!\nUse: plus (+), minus (-), times (*), over (/), pow (**), mod (%), fdiv (//)"
	
	if arg_2_is_file:
		assert cube_field1 == cube_field2,"The cube fields need to have the same size!"

	result = open('Result.cube','w')

	for line in header_1:
		result.write(line)

	write_result(arg_2_is_file, op_string, arg_1, arg_2, result)
