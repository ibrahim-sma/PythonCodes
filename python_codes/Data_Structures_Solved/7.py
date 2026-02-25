# """
# Find Second Largest Element in a List
# Without using sort().
# """

# a = [1, 4, 2, 1, 3, 4, 1, 2, 8, 3, 5, 6, 3, 6, 5, 7, 9, 8, 10]
# print(a)


# def testing_type_safety(a: int, b: int) -> int:
#     return a + b
# print(testing_type_safety(5, 10))
# print(testing_type_safety("5", "10"))  # This will raise a type error in static type checkers

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)
