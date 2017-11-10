#ex-funny string (easy)
#first page, last exercise

# !/bin/python3

import sys
from string import ascii_lowercase as ass


def funnyString(s):
    # Complete this function
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ass.find(s[i]) - ass.find(s[i - 1])) != abs((ass.find(r[i]) - ass.find(r[i - 1]))):
            return "Not Funny"
    return "Funny"


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)