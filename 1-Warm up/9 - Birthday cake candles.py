#9-birthday cake candles

#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    ar.sort()
    return ar.count(ar[-1])

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)