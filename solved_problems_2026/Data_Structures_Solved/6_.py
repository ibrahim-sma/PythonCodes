"""
Remove Duplicates While Preserving Order
Given a list, remove duplicates but maintain the original order.
"""

a = [1, 4, 2, 1, 3, 4, 1, 2, 8, 3, 5, 6, 3, 6, 5, 7, 9, 8, 10]
print(a)

unique_list = []
for i in a:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
