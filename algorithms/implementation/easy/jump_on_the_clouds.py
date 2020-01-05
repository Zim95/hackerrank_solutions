#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
jumping-on-the-clouds/problem
'''


def jumpingOnClouds(c):
    cloud_index = 0
    final_index = len(c) - 1
    path_count = 0
    while cloud_index != final_index:
        if cloud_index + 2 <= final_index:
            if c[cloud_index + 2] == 0:
                cloud_index += 2
                path_count += 1
                continue
        if cloud_index + 1 <= final_index:
            if c[cloud_index + 1] == 0:
                cloud_index += 1
                path_count += 1
                continue
    if cloud_index == final_index:
        return path_count
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
