#!/bin/python3

import os
import sys


'''
Problem - https://www.hackerrank.com/challenges/
simple-array-sum/submissions/code/131277819
'''


def simpleArraySum(ar):
    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
