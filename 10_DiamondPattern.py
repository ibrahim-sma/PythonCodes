"""
10) Write a program to print Diamond Pattern
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        *
"""

print("\nProgram to print Diamond Pattern\n")
n=5
for i in range(n-1):
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()
