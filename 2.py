import Levenshtein
import numpy as np
import sys
import os

def soundex_func(token):
   
    token = token.upper()
 
    soundex = ""
 
    soundex += token[0]
 
    dictionary = {"BFPV": "1", "CGJKQSXZ": "2","DT": "3","L": "4", "MN": "5", "R": "6","AEIOUHWY": "."}
 
    for char in token[1:]:
        for key in dictionary.keys():
            if char in key:
                code = dictionary[key]
                if code != '.':
                    if code != soundex[-1]:
                        soundex += code
 
    soundex = soundex[:7].ljust(7, "0")
 
    return soundex



string = input("Enter string to search for: ")

file_loc = input("Enter file location: ")

# soundex = fuzzy.Soundex(4)
str = soundex_func(string)
# print(f)
with open(file_loc) as f:
    lines = f.readlines()

# print(len(lines))\

list = []

for i in lines:
    # print(i)
    splitted = i.split(' ')
    for j in splitted:
        str2 = soundex_func(j)
        num = Levenshtein.distance(str, str2)
        # print(num)
        if(num < 2):
            list.append(j)
    # print('\n')
# print(lines)
# print(j)
for i in list:
    print(i)
f.close()