#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
circular-array-rotation/problem
'''


def circularArrayRotation(a, k, queries):
    if len(a) < k:
        new_k = k % len(a)
        first_half = a[-new_k:]
        second_half = a[:len(a) - new_k]
        final_list = first_half + second_half
    else:
        first_half = a[-k:]
        second_half = a[:len(a) - k]
        final_list = first_half + second_half
    result = []
    for query in queries:
        if len(final_list) > query:
            result.append(final_list[query])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
