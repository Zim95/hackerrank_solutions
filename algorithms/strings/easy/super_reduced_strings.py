#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://hackerrank.com/challenges/
reduced-string/problem
'''


def superReducedString(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
            continue
        if stack[-1] == i:
            x = stack.pop(-1)
        else:
            stack.append(i)
    if not stack:
        return 'Empty String'
    return ''.join(stack)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
