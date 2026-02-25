"""
Advanced Level (5 Programs)
11. Total Revenue from High-Value Sales
Concepts: filter, map, reduce
📌 Task:
From a list of sales values:
Filter sales above 1000
Apply 18% tax
Calculate total revenue
(All in a single pipeline)
"""

from functools import reduce

sales_list = [1200, 840, 688, 2210, 3000, 10000, 200]
filtered_list = list(filter(lambda x: x > 1000, sales_list))
print(f"sales above 1000 = {filtered_list}")
taxed_list = list(map(lambda x: x * 1.18, filtered_list))
print(f"Applied 18% tax = {taxed_list}")
total_revenue = reduce(lambda x,y: x+y, taxed_list)
print(f"total revenue = {total_revenue}")


# chatgpt Score 8.5/10 and optimized code
from functools import reduce

sales_list = [1200, 840, 688, 2210, 3000, 10000, 200]

total_revenue = reduce(
    lambda acc, x: acc + x,
    map(
        lambda x: x * 1.18,
        filter(lambda x: x > 1000, sales_list)
    ),
    0
)

print(f"Total revenue = {total_revenue}")
