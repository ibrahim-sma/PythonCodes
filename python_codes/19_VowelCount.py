"""
19) From any given passage, count the number of vowels present in the sentence
a,e,i,o,u are the vowels
"""

inp_str = """
Backward iteration in Python refers to the process of iterating through a sequence 
or collection in reverse order, moving from the last element to the first. This is 
often useful when we need to access elements in the opposite order of their 
original arrangement. Python provides various mechanisms for backward iteration, 
such as using negative indexing or employing built-in functions like reversed().
""".lower()

vowel_str = "aeiou"
vowel_dict = {}
for i in inp_str:
    if i in vowel_str:
        if i not in vowel_dict:
            vowel_dict[i] = 1
        else:
            vowel_dict[i] += 1

print(vowel_dict)
