"""
7) Write a program to print 
i) Increasing Triangle pattern
* 
* *
* * *
* * * *
* * * * *
ii) Decreasing Triangle pattern
* * * * * 
* * * * 
* * * 
* * 
*
"""

print("\ni) Increasing Triangle pattern")
n=5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

print("\nii) Decreasing Triangle pattern")
n=5
for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    print()
