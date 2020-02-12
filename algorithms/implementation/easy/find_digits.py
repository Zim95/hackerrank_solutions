#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/find-digits/
problem?h_r=next-challenge&h_v=zen
'''


def findDigits(n):
    counter = n
    divisor_count = 0
    while counter > 0:
        number = counter % 10
        if number != 0:
            if n % number == 0:
                divisor_count += 1
        counter = int(counter/10)
    return divisor_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
