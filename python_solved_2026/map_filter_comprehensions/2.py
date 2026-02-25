"""
2. Filter Even Numbers
Concepts: filter, lambda
📌 Task:
From a list of integers, filter out only the even numbers.
"""

input_list = [i for i in range(1, 15)]
filtered_list = list(filter(lambda x: x%2==0, input_list))
print(input_list)
print(filtered_list)


# Chatgpt Score - 9/10 & Chatgpt Improved code

def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a list of even numbers using filter() and lambda.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))


if __name__ == "__main__":
    input_list = list(range(1, 15))
    filtered_list = filter_even_numbers(input_list)

    print(input_list)
    print(filtered_list)