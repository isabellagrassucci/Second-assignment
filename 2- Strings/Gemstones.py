#Gemstones (easy)
#second page,first exercise

# !/bin/python3

import sys


def gemstones(arr):
    # Complete this function
    gem_element = 0
    setarr = set(arr[0])
    for i in setarr:
        for k in range(1, len(arr)):
            if i in arr[k]:
                if k == (len(arr) - 1):
                    gem_element += 1
            else:
                break
    return gem_element


n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
    arr_t = str(input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)