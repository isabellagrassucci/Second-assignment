#8-mini-max sum

#!/bin/python3

import sys

minsum=0
maxsum=0
arr = list(map(int, input().strip().split(' ')))
arr.sort()
for i in range(4):
    minsum+= arr[i]
    maxsum+= arr[-(i+1)]
print (minsum,maxsum)