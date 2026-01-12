"""
7. Find Students Who Passed
Concepts: dictionary comprehension
📌 Task:
Given a dictionary of student marks, create a new dictionary containing only students who scored ≥ 40.
"""
students_dict = {'Arun': 22, 'Ankit': 68, 'Bala': 92, 'Vinay': 44, 'Ibrahim': 37}
passed_students_dict = {student:mark for student,mark in students_dict.items() if mark >= 40}
print(passed_students_dict)
print(students_dict)

# chatgpt Score 9.5/10 and optimized code

def get_passed_students(records: dict[str, int]) -> dict[str, int]:
    """
    Returns a dictionary of students who scored >= 40.
    """
    return {student: mark for student, mark in records.items() if mark >= 40}


if __name__ == "__main__":
    students_dict = {
        'Arun': 22, 'Ankit': 68, 'Bala': 92, 'Vinay': 44, 'Ibrahim': 37
    }

    print(get_passed_students(students_dict))
    print(students_dict)
