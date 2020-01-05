#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/picking-numbers/problem
'''


def pickingNumbers(a):
    string = ''
    sorted_a = sorted(a)
    start_val = None

    for item in sorted_a:
        if start_val is None:
            start_val = item
            string = string + str(start_val) + ","
            continue
        if abs(start_val - item) <= 1:
            string = string + str(item) + ","
        else:
            string = string + "\n" + str(item) + ","
            start_val = item

    string_list = string.split("\n")

    max_list_value = 0

    for string_value in string_list:
        string_len = len(string_value.rstrip(',').split(","))
        if string_len > max_list_value:
            max_list_value = string_len

    return max_list_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
