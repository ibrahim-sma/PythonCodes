"""
8) Write a program to print Right Sided Triangle pattern
i) Decreasing space & Increasing Star
        * 
      * * 
    * * * 
  * * * * 
* * * * *
ii) Increasing space & Decreasing Star

"""

print("i) Decreasing space & Increasing Star")
n=5
for i in range(n):
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

print("ii) Increasing space & Decreasing Star")
n=5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()
