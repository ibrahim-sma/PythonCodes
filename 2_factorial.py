"""
2) Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""

def recursive_fn(inp_no):
	if inp_no > 1:
		return recursive_fn(inp_no-1) * inp_no
	else:
		return 1

print(recursive_fn(12))
