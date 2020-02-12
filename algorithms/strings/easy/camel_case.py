#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges
/camelcase/problem?h_r=next-challenge&h_v=zen
'''


def camelcase(s):
    items = re.split("[A-Z]", s)
    return len(items)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
