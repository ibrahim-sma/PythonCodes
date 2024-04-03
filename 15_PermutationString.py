"""
15) Python Program to Find HCF or GCD of any two numbers.
n1 = 1428, n2 = 3724
"""

n1 = 1428
n2 = 3724
smaller = n1 if n1 < n2 else n2

hcf = 1
for i in range(2, smaller+1):
    if n1%i == 0 and n2%i == 0:
        hcf = i
print(hcf)

