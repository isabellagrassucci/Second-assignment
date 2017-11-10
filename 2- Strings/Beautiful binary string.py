#Beautiful binary string (easy)
#second page, third exercise

#!/bin/python3

import sys

def minSteps(n, B):
    # Complete this function
    lst=[]
    change=0
    for el in B:
        lst.append(el)
    for i in range(len(lst)-2):
        if lst[i:i+3]==["0","1","0"]:
            lst[i+2]="1"
            change+=1
    return change

n = int(input().strip())
B = input().strip()
result = minSteps(n, B)
print(result)