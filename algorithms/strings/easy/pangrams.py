#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/pangrams/problem?
h_r=next-challenge&h_v=zen&
h_r=next-challenge&h_v=zen&
h_r=next-challenge&h_v=zen
'''


def pangrams(s):
    all_alphabets = {
        'c', 'w', 'm',
        'l', 'g', 'x',
        'z', 't', 'u',
        'v', 'k', 'i',
        'h', 'y', 'p',
        's', 'd', 'a',
        'o', 'r', 'b',
        'f', 'n', 'j',
        'e', 'q'
    }

    s_set = set(s.lower())
    diff_set = all_alphabets - s_set
    if diff_set:
        return 'not pangram'
    else:
        return 'pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
