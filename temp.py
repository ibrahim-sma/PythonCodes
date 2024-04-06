import re      
# The string of text where regular expression will be searched.   
string_1 = """Here are some student's ID, student A: 676  
            student B: 564  
            student C: 567  
            student D: 112  
            student E: 234"""      
# Setting the regular expression for finding digits in the string.   
regex_1 = "\w+\s\w\:\s\d+"                  
match_1 = re.findall(regex_1, string_1)   
print(match_1)
