#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/counting-valleys/problem
'''


def countingValleys(n, s):
    level = 0
    level_list = [level]
    for i in range(0, n):
        if s[i] == 'U':
            level += 1
        elif s[i] == 'D':
            level -= 1
        level_list.append(level)

    valley_count = 0

    for index, lv in enumerate(level_list):
        if lv == 0:
            if (index - 1) < 0:
                continue
            prev_element = level_list[index-1]
            if prev_element < 0:
                valley_count += 1
    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
