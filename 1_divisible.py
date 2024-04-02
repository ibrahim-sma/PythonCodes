"""
1) Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

def div_by7_not5():

	div_list = []
	for i in range(2000, 3201):
	# for i in range(100):
		if i%7==0 and i%5!=0:
			div_list.append(str(i))
	return div_list

div_list = div_by7_not5()
div_nos = ", ".join(div_list)
print(div_nos)

# Sample Output: 2002, 2009, 2016, 2023, 2037,..., 3171, 3178, 3192, 3199
