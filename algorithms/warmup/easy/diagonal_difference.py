#!/bin/python3

import math
import os
import random
import re
import sys

'''
Problem - https://www.hackerrank.com/challenges/
diagonal-difference/problem?h_r=next-challenge&h_v=zen
'''


def diagonalDifference(arr):
    first_diagonal = []
    second_diagonal = []
    for i in range(0, len(arr)):
        first = arr[i][i]
        last = arr[i][-i-1]
        first_diagonal.append(first)
        second_diagonal.append(last)
    sum_first = sum(first_diagonal)
    sum_second = sum(second_diagonal)
    return abs(sum_first-sum_second)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
