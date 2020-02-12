#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
strange-advertising/problem
'''


def viralAdvertising(n):
    if n == 0:
        return 0
    if n == 1:
        return 2

    base_value = 5
    cumulative = 0
    liked = 0
    for _ in range(0, n):
        liked = math.floor(base_value/2)
        cumulative += liked
        base_value = liked * 3
    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
