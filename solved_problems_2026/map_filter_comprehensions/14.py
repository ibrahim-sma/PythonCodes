"""
14. Find Maximum Using Reduce
Concepts: reduce, lambda
📌 Task:
Without using max(), find the maximum number in a list using reduce().
"""

from functools import reduce
inp_list= [84, 38, 92, 63, 88]
max_no = reduce(lambda x,y: x if x>y else y, inp_list, 0)
print(max_no)


# Chatgpt Score - 8.5/10 & Chatgpt Improved code

from functools import reduce

def find_max(numbers: list[int]) -> int:
    """
    Finds the maximum number using reduce and lambda.
    """
    return reduce(lambda x, y: x if x > y else y, numbers)


if __name__ == "__main__":
    numbers = [84, 38, 92, 63, 88]
    print(find_max(numbers))
