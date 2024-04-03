"""
12) A palindromic number reads the same both ways. The largest palindrome made from the 
product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
max_prod = 1
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        prod = i*j
        if prod < max_prod:
            break
        if str(prod) == str(prod)[::-1]:
            if prod > max_prod:
                max_prod = prod
            break
print(max_prod)

# Output: 906609
