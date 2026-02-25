"""
8. Flatten a Nested List
Concepts: list comprehension (nested loops)
📌 Task:
Flatten a list of lists into a single list.
"""

nested_input_list = [1, 4, [21, [36, 48]]]
flattened_list = [x for y in nested_input_list for x in (y if isinstance(y, list) else [y])]
