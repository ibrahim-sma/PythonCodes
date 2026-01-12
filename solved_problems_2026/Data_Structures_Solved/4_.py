"""
Reverse a List Without Using Built‑in Reverse
Reverse a list using loops.
"""

a = list(range(1, 21))
b = [a[len(a)-i-1] for i in range(len(a))]
print(a)
print(b)


# Other Solutions
# Reversing a list using inbuilt-functions
print(a[::-1])

# Reversing a list without using inbuilt-functions
for i in range(-1, -(len(a))-1, -1):
    print(a[i])



# Chatgpt Solution
def reverse_list(values: list) -> list:
    """
    Reverses a list using a loop without built-in reverse methods.
    """
    reversed_list = []
    for i in range(len(values) - 1, -1, -1):
        reversed_list.append(values[i])
    return reversed_list


if __name__ == "__main__":
    original = list(range(1, 21))
    result = reverse_list(original)

    print("Original:", original)
    print("Reversed:", result)

