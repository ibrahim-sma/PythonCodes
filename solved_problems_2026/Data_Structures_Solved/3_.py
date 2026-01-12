"""
Count Vowels in a String
Write a program to count the number of vowels in a given string.
"""

inp_str = """
Count Vowels in a String Write a program to count the number of vowels in a given string.
""".lower()

from functools import reduce
vowels_list = ["a", "e", "i", "o", "u"]
reduce_result = reduce(
    lambda acc, char: acc + 1 if char in vowels_list else acc,
    inp_str,
    0
)
print(reduce_result)

# Solution without Inbuilt function
vowels_count = 0
for i in inp_str:
    if i in vowels_list:
        vowels_count += 1
print(vowels_count)

# Solution using Python Inbuilt function
vowels_list = ["a", "e", "i", "o", "u"]
vowels_count = 0
for i in vowels_list:
    vowels_count += inp_str.count(i)
print(vowels_count)

# Chatgpt Suggesstion:


# Improved Version (Best Practice, Still Beginner-Friendly)
def count_vowels(text: str) -> int:
    """
    Returns the number of vowels in the given string.
    """
    vowels = {"a", "e", "i", "o", "u"}
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


if __name__ == "__main__":
    inp_str = """
    Count Vowels in a String Write a program to count
    the number of vowels in a given string.
    """
    print(count_vowels(inp_str))