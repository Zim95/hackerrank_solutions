#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
repeated-string/problem?h_r=next-challenge&h_v=zen
'''


def repeatedString(s, n):
    a_count_in_string = s.count('a')
    repitition_count = int(n/len(s))
    total_a_count_so_far = a_count_in_string * repitition_count
    remainder_length = int(n % len(s))
    remainder_length_from_s = s[:remainder_length]
    a_count_in_remainder_string = remainder_length_from_s.count('a')
    total_count = total_a_count_so_far + a_count_in_remainder_string
    return total_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
