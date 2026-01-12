"""
10. Pair Names with Scores
Concepts: zip, list comprehension
📌 Task:
Given two lists (names, scores), create a list of strings like
"Alice scored 85".
"""

students_list = ["Arun", "Ankit", "Bala", "Vinay", "Ibrahim"]
marks_list = [84, 38, 92, 63, 88]
score_list = [f"{student} scored {mark}" for student,mark in zip(students_list, marks_list)]
print(score_list)


# chatgpt Score 9.5/10 and optimized code
def pair_names_with_scores(names: list[str], scores: list[int]) -> list[str]:
    """
    Returns a list of formatted score strings using zip and list comprehension.
    """
    return [f"{name} scored {score}" for name, score in zip(names, scores)]


if __name__ == "__main__":
    students_list = ["Arun", "Ankit", "Bala", "Vinay", "Ibrahim"]
    marks_list = [84, 38, 92, 63, 88]

    print(pair_names_with_scores(students_list, marks_list))
