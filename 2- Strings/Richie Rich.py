#!/bin/python3

import sys


def richieRich(s, n, k):
    lst = []
    left = []
    right = []
    original = []
    number = []
    center = int()
    for el in s:
        lst.append(el)
        original.append(el)
    for el in lst[:len(lst) // 2]:
        left.append(el)
    if n % 2 == 1:
        center = lst[len(lst) // 2]
        for el in lst[len(lst) // 2 + 1:]:
            right.append(el)
    if n % 2 == 0:
        for el in lst[len(lst) // 2:]:
            right.append(el)
    right = right[::-1]

    differentCount = 0
    for i in range(len(left)):
        if left[i] != right[i]:
            differentCount += 1  # the number of different coupples

    if differentCount > k:
        return '-1'

    for i in range(len(left)):
        if left[i] != right[i] and (int(left[i]) == 9 or int(right[i]) == 9):  # if the are different but one is 9
            if k >= differentCount:  # +1
                left[i] = 9
                right[i] = 9
                k -= 1
                differentCount -= 1

    for i in range(len(left)):
        if left[i] != right[i] and (int(left[i]) != 9 and int(right[i]) != 9):
            if k - 2 >= differentCount - 1:
                left[i] = 9
                right[i] = 9
                k -= 2
                differentCount -= 1
        if left[i] != right[i]:
            if k >= differentCount:
                if left[i] > right[i]:
                    right[i] = left[i]
                    if right[i] > left[i]:
                        left[i] = right[i]
                k -= 1
                differentCount -= 1

    for i in range(len(left)):
        if original[i] == original[-i - 1]:
            if k >= 2 + differentCount and (int(left[i]) != 9 and int(right[
                                                                          i]) != 9):  # if they are the same but both are diffrfent from 9 and there are still changes available
                left[i] = 9
                right[i] = 9
                k -= 2
        if original[i] != original[-i - 1]:
            if k >= 1 + differentCount and (int(left[i]) != 9 and int(right[i]) != 9):
                left[i] = 9
                right[i] = 9
                k -= 1

    if k > 0:
        center = 9
    right = right[::-1]

    if n % 2 == 1:
        left.append(center)
        left += right
        for x in left:
            number.append(str(x))
    if n % 2 == 0:
        left += right
        for x in left:
            number.append(str(x))
    string = "".join(number)
    return string


lst = list(map(int, input().split()))
n = lst[0]
k = lst[1]
s = input().strip()
result = richieRich(s, n, k)
print(result)