#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/strong-password/problem
'''


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    additional = 0
    lower_case = re.findall("[a-z]", password)
    if not lower_case:
        print('No lowercase')
        additional += 1
    upper_case = re.findall("[A-Z]", password)
    if not upper_case:
        print('No uppercase')
        additional += 1
    digit = re.findall("[0-9]", password)
    if not digit:
        print('No digit')
        additional += 1
    special = re.findall("[!@#$%^&*()\-+]", password)  # noqa
    if not special:
        print('No special')
        additional += 1

    total = len(password) + additional
    if total >= 6:
        return additional
    else:
        return additional + (6 - total)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
