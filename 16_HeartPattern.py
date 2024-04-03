
"""

  * *       * *   
* * * *   * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        *
"""

n=5
for i in range(2, n, 2):
    for j in range(i, n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
        
n=5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()