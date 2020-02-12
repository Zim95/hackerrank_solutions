#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/beautiful-days-at-the-movies/
problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''


def beautifulDays(i, j, k):
    count = 0
    for num in range(i, j+1):
        reverse_numb = int(str(num)[::-1])
        diff = abs(num - reverse_numb)
        if diff % k == 0:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
