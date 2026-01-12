"""
Find Largest of Three Numbers
Given three numbers, find the largest using conditional statements.
"""

import random
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
print(a, b, c)

# Solution without Inbuilt function
max_no = a if a > b else b
max_no = c if c > max_no else max_no
print(max_no)

# Other Solutions
# Solution using Python Inbuilt function
print(max([a,b,c]))

# Solution without Inbuilt function
max = 0
for i in [a, b, c]:
    if i > max:
        max = i
print(max)

# Chatgpt suggesstion:

import random

def largest_of_three(a: int, b: int, c: int) -> int:
    """
    Returns the largest of three numbers without using built-in functions.
    """
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


# if __name__ == "__main__":
#     a = random.randint(1, 100)
#     b = random.randint(1, 100)
#     c = random.randint(1, 100)

#     print(a, b, c)
#     print(largest_of_three(a, b, c))

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
d = random.randint(1, 100)
e = random.randint(1, 100)
f = random.randint(1, 100)

print(a, b, c, d, e, f)

from functools import reduce
inp_list = [a, b, c, d, e, f]
largest = reduce(lambda x, y: x if x > y else y, inp_list)
print(largest)

max_no = 0
for i in inp_list:
    if i > max_no:
        max_no = i
print(max_no)


a = [1, 2, 3, 4]
b = [5, 6, 7]

zip_result = zip(a, b)
print(list(zip_result))
