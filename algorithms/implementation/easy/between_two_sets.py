#!/bin/python3

import math
import os
import random
import re
import sys

'''
Problem - https://www.hackerrank.com/challenges/
between-two-sets/problem
'''


def divide_by_a(a, number):
    for item in a:
        if number % item != 0:
            return False
    return True


def divide_b(b, number):
    for item in b:
        if item % number != 0:
            return False
    return True


def getTotalX(a, b):
    # Write your code here
    lower = min(a)
    upper = max(b)

    numbers = [i for i in range(lower, upper + 1)]

    count = 0
    for number in numbers:
        if divide_by_a(a, number) and divide_b(b, number):
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
