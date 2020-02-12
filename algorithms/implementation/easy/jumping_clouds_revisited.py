#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
jumping-on-the-clouds-revisited/problem
'''


def jumpingOnClouds(c, k):
    i = 0
    e = 100
    n = len(c)
    while i < n:
        if c[i] == 1:
            e -= 2
        i = (i + k) % n
        e -= 1
        if i == 0:
            break
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
