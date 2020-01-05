#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
utopian-tree/problem?h_r=next-challenge&h_v=zen
'''


def utopianTree(n):
    if n == 0:
        return 1

    height = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            height += 1
        else:
            height += height
    return height


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
