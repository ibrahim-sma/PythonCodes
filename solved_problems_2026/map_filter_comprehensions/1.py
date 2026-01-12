"""
1. Square Numbers
Concepts: map, lambda
📌 Task:
Given a list of numbers, use map() and lambda to return a list of their squares.
"""

input_list = [i for i in range(1, 10)]
squared_list = list(map(lambda x: x**2, input_list))
print(input_list)
print(squared_list)


# Chatgpt Score - 9/10 & Chatgpt improved code

def square_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a list of squares using map() and lambda.
    """
    return list(map(lambda x: x ** 2, numbers))


if __name__ == "__main__":
    input_list = list(range(1, 10))
    squared_list = square_numbers(input_list)

    print(input_list)
    print(squared_list)
