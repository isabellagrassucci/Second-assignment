#10- time conversion

#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    clock= s[-2:]
    s=s[:-2]
    lst= s.split(":")
    if clock=="PM" and lst[0]!="12":
        lst[0]= str(int(lst[0])+12)
    elif clock=="AM" and lst[0]=="12":
        lst[0]="00"
    string= ":".join(lst)
    return string

s = input().strip()
result = timeConversion(s)
print(result)