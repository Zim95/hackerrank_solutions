#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/two-characters/problem
'''


def alternate(s):
    distinct_letters = set(s)
    selected_ones_cache = []
    for i in range(0, len(s) - 1):
        for j in range(i + 1, len(s)):
            selected_ones = {s[i], s[j]}
            if len(selected_ones) == 2 and \
                    selected_ones not in selected_ones_cache:
                # get selected one
                selected_ones_cache.append(selected_ones)
    max_length = 0
    for selected_one in selected_ones_cache:
        # get remaining ones
        remaining_ones = distinct_letters - selected_one
        # remove remaining ones from main_string
        main_string = s
        for r in remaining_ones:
            main_string = main_string.replace(r, "")
        # validate main string
        p = 0
        q = 1
        invalid = False
        while q < len(main_string):
            if main_string[p] != main_string[q]:
                p += 1
                q += 1
            else:
                invalid = True
                break
        if not invalid:
            main_length = len(main_string)
            if main_length > max_length:
                max_length = main_length
    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lr = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
