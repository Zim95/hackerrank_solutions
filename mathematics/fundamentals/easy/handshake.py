#!/bin/python3

import os
import sys


'''
Problem - https://www.hackerrank.com/
challenges/handshake/problem
'''


cache = {}
sys.setrecursionlimit(10**6)


def handshake(n):
    if n == 1:
        return 0
    if (n - 1) in cache:
        return cache[n - 1]
    else:
        result = (n - 1) + handshake(n - 1)
        cache[n - 1] = result
        return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
