#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem -
https://www.hackerrank.com/challenges/
equality-in-a-array/problem?
h_r=next-challenge&h_v=zen
'''


def equalizeArray(arr):
    distinct_arr = set(arr)
    frequency_dict = {}
    for item in distinct_arr:
        frequency_dict[item] = 0
    for i in arr:
        frequency_dict[i] += 1
    max_freq = 0
    for number, frequency in frequency_dict.items():
        if frequency > max_freq:
            max_freq = frequency
    return len(arr) - max_freq


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
