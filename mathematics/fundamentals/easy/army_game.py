#!/bin/python3

import os
import sys


'''
Problem - https://www.hackerrank.com/
challenges/game-with-cells/problem
'''


def gameWithCells(n, m):
    row_count = int(n/2) + (n % 2)
    col_count = int(m/2) + (m % 2)
    return row_count * col_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
