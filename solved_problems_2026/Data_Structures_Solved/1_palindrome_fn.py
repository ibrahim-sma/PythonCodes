"""
Check Palindrome
Write a program to check whether a given string or number is a palindrome.
"""

# Chatgpt Score - 8 / 10
def is_palindrome(user_input: int|str) -> bool:
    """
    Returns True if the given string or number is a palindrome.
    """

    if str(user_input).lower() == str(user_input)[::-1].lower():
        return True
    return False

if __name__ == "__main__()":
    user_input_list = [1001, 1101, 110, 10101, "madam", "teen", "deed", "need", "mam"]
    palindrome_list = list(filter(is_palindrome, user_input_list))
    print(palindrome_list)


# ChatGPT Suggestions:

def is_palindrome(user_input: int | str) -> bool:
    return str(user_input).lower() == str(user_input)[::-1].lower()

def is_palindrome(value: int | str) -> bool:
    normalized = "".join(
        char.lower() for char in str(value) if char.isalnum()
    )
    return normalized == normalized[::-1]

