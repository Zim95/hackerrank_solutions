#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/the-hurdle-race/
problem?h_r=next-challenge&h_v=zen
'''


def hurdleRace(k, height):
    max_height = max(height)
    if k >= max_height:
        return 0
    else:
        return (max_height - k)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
