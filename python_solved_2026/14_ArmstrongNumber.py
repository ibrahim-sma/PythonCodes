"""
14) Program to check Armstrong numbers in a certain interval from 100 to 2000
Armstrong number is 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
"""

def armstrong_no(n):
    
    cube_sum = 0
    for j in str(n):
        cube_sum += (int(j))**3
    
    if cube_sum == n:
        return True
    else:
        return False

for i in range(100, 2000):
    if armstrong_no(i):
        print(f"{i} is an armstrong number")
