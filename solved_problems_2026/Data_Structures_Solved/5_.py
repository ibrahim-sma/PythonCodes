"""
Check Prime Number
Write a program to check whether a number is prime.
"""

# Chatgpt scored this 7.5/10
def is_prime(inp_no):

    if inp_no < 2:
        return False

    for i in range(2, int(inp_no/2)+1):
        if inp_no%i == 0:
            return False
    else:
        return True

inp_no_list = range(1, 100)
for inp_no in inp_no_list:
    if is_prime(inp_no):
        print(f"{inp_no} is a Prime Number")


# Chatgpt code

def is_prime(n: int) -> bool:
    """
    Returns True if the given number is prime, otherwise False.
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    for number in range(1, 100):
        if is_prime(number):
            print(f"{number} is a Prime Number")


