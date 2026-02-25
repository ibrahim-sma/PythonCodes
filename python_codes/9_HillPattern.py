"""
9) Write a program to print 

i) Hill Pattern
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

ii) Inverted Hill Pattern
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        *
"""

print("\ni) Program to print Hill Pattern\n")
n=5
for i in range(n):
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

print("\nii) Program to print Inverted Hill Pattern\n")
n=5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()
