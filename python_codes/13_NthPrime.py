"""
13) Write a function to evaluate if the given number is prime or not
"""

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    for i in range(2, int(n/2)+1):
        if n%i == 0:
            return False
    else:
        return True

for i in range (1, 30):
    print(f"{i}", is_prime(i))
