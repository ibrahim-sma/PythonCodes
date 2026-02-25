"""
6. Sum of All Positive Numbers
Concepts: filter, reduce, lambda
📌 Task:
From a list of integers, filter positive numbers and calculate their sum.
"""
from functools import reduce

input_list = [-36, 101, 43, 11, -39, 66, 204]
positive_list = list(filter(lambda x: x > 0, input_list))
print(positive_list)
sum_of_input_list = reduce(lambda x,y: x+y, positive_list)
print(sum_of_input_list)


# chatgpt score - 9/10 & Chatgpt Improved code

from functools import reduce

def sum_of_positives(numbers: list[int]) -> int:
    """
    Filters positive numbers and returns their sum using filter and reduce.
    """
    positives = filter(lambda x: x > 0, numbers)
    return reduce(lambda x, y: x + y, positives, 0)


if __name__ == "__main__":
    input_list = [-36, 101, 43, 11, -39, 66, 204]
    print(list(filter(lambda x: x > 0, input_list)))
    print(sum_of_positives(input_list))
