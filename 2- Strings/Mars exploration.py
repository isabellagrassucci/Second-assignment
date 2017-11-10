#Mars exploration (easy)
#first page, fifth exercise

#!/bin/python3

import sys


S = input().strip()
wrong=0
for i in range(0,len(S),3):
    if S[i]!="S":
        wrong+=1
    if S[i+1]!="O":
        wrong+=1
    if S[i+2]!="S":
        wrong+=1
print (wrong)