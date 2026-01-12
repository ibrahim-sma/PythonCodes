"""
Concepts: dictionary comprehension
📌 Task:
Given a dictionary of employees and salaries, increase salary by:
10% if salary < 50,000
5% otherwise
Return a new updated dictionary.
"""

emp_salary_dict = {'Arun': 22000, 'Ankit': 68000, 'Bala': 92000, 'Vinay': 44000, 'Ibrahim': 37000}
# increased_salary_dict = {emp:salary * 1.10 for emp,salary in emp_salary_dict.items() if salary < 50000 else emp: salary * 1.05 }
increased_salary_dict = {map for emp,salary in emp_salary_dict.items()}
print(increased_salary_dict)
