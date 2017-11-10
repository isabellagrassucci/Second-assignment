#5-diagonal difference

#!/bin/python3

import sys


n = int(input().strip())
a = []
prim=0
sec=0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for i in range(len(a)):
    prim+= a[i][i]
    sec-= a[i][-(i+1)]
print (abs(prim+sec)) #The element is already negative, so if we do the difference, it actually do the sum. Otherwise, in this case the sum is the actual difference