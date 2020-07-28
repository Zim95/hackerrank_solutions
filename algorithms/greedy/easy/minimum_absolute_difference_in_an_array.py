#!/bin/python3

import os

'''
Problem - https://www.hackerrank.com/
challenges/minimum-absolute-difference-in-an-array/problem
'''


def minimumAbsoluteDifference(arr):
    # greedy approach here is to pick the smallest number pairs
    arr.sort()
    diff = []
    for i in range(1, len(arr)):
        diff.append(abs(arr[i] - arr[i-1]))
    return min(diff)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
