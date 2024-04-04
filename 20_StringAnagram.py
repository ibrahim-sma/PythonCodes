"""
20) Python Program to Check If Two Strings are Anagram. Two strings are said to be anagram 
if we can form one string by arranging the characters of another string. For example, 
Race and Care. Here, we can form Race by arranging the characters of Care.
"""

inp_str1 = input("Enter input string1: ")
inp_str2 = input("Enter input string2: ")

if sorted(inp_str1) == sorted(inp_str2):
    print(f"{inp_str1}, {inp_str2},  are anagrams")
else:
    print(f"{inp_str1}, {inp_str2},  are not anagrams")

