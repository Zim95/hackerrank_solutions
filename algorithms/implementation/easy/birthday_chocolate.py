#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/the-birthday-bar/problem
'''


def birthday(s, d, m):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        if s[0] == d:
            return 1
        else:
            return 0

    window_range = len(s) - m
    count = 0
    for i in range(0, window_range+1):
        window = s[i:i+m]
        print(i, i+m)
        print(window)
        window_sum = sum(window)
        if window_sum == d:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
