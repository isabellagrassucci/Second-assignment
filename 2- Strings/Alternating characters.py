#Alternatig characters (easy)
#second page, second exercise

#!/bin/python3

import sys

def alternatingCharacters(s):
    # Complete this function
    change=0
    lst=[]
    for el in s:
        lst.append(el)
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            s=s[:i+1]+s[i+2:]
            change+=1
    return change

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)