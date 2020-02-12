#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
permutation-equation/problem
'''


def permutationEquation(n, p):
    result = []
    for x in range(1, n+1):
        first_index = p.index(x) + 1
        second_index = p.index(first_index) + 1
        result.append(second_index)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(n, p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
