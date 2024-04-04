"""
18) Python program to validate a string and find the consecutive letters frequency.
For eg. "Pyyyyyttthhhoonnnhhhhh" Frequency here is p=1 y=4 t=3 h=3 o=2 n=3 h=5
Here h is seen twice but highest value should be considered. Output should return
letter with higher frequency
"""

test_str = "geekksfffffoooorpyyyyyytttthhooonngggeeeeks"

curr_str = ""
str_dict = {}
curr_str_count = 0
max_str = ""
max_str_val = 0

for i in test_str:
    if curr_str == "":
        curr_str = i
        curr_str_count += 1
        continue

    if i != curr_str:
        if curr_str not in str_dict or str_dict[curr_str] < curr_str_count:
            str_dict[curr_str] = curr_str_count
        
        if curr_str_count > max_str_val:
            max_str_val = curr_str_count
            max_str = curr_str

        curr_str = i
        curr_str_count = 1
    else:
        curr_str_count += 1

print(str_dict)
print(max_str, max_str_val)
