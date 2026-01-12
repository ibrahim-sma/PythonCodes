"""
4. Create a Dictionary from Two Lists
Concepts: zip, dictionary comprehension
📌 Task:
Given two lists (students, marks), create a dictionary mapping student → marks.
"""

students_list = ["Arun", "Ankit", "Bala", "Vinay", "Ibrahim"]
marks_list = [84, 38, 92, 63, 88]
mapped_dict = {student:mark for student,mark in zip(students_list, marks_list)}
print(mapped_dict)


# chatgpt Score 9.5/10 and optimized code
def map_students_to_marks(students: list[str], marks: list[int]) -> dict[str, int]:
    """
    Maps students to their marks using zip and dictionary comprehension.
    """
    return {student: mark for student, mark in zip(students, marks)}


if __name__ == "__main__":
    students_list = ["Arun", "Ankit", "Bala", "Vinay", "Ibrahim"]
    marks_list = [84, 38, 92, 63, 88]

    print(map_students_to_marks(students_list, marks_list))

