"""
5. Uppercase All Strings
Concepts: list comprehension
📌 Task:
Given a list of names, return a new list with all names in uppercase.
"""

students_list = ["Arun", "Ankit", "Bala", "Vinay", "Ibrahim"]
upper_case_list = [student.upper() for student in students_list]
print(upper_case_list)


# chatgpt Score 9.5/10 and optimized code
def uppercase_names(names: list[str]) -> list[str]:
    """
    Returns a list of names converted to uppercase using list comprehension.
    """
    return [name.upper() for name in names]


if __name__ == "__main__":
    students_list = ["Arun", "Ankit", "Bala", "Vinay", "Ibrahim"]
    print(uppercase_names(students_list))
