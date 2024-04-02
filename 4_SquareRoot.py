"""
4) Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H:  C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example: Let us assume the following comma separated input sequence is given to the program:
100,150,180. 
The output of the program should be: 18,22,24
"""

import math

def square_root(inp_list):

	c = 50
	h = 30
	out_list = []
	for d in inp_list:
		expr_out = math.sqrt((2*c*d)/h)
		# expr_out = ((2*c*d)/h)**0.5
		out_list.append(int(expr_out))

	return out_list

inp_list = [100,150,180]
print(square_root(inp_list))
