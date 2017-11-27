#!/bin/python3

import sys
from collections import defaultdict

n = int(input().strip())
dic = defaultdict(list)

for _ in range(n):
    el = input().strip()
    dic[len(el)].append(el)

for key in sorted(dic):
    for value in sorted(dic[key]):
        print(value)