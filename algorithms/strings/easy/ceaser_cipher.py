#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/caesar-cipher-1/problem
'''


def caesarCipher(s, k):
    lowercase = [
        'a', 'b', 'c', 'd',
        'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p',
        'q', 'r', 's', 't',
        'u', 'v', 'w', 'x',
        'y', 'z'
    ]
    uppercase = [
        'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X',
        'Y', 'Z'
    ]

    final_string = ""
    for item in s:
        # detect upper, lower or special char
        if re.match("[A-Z]", item):
            actual_index = uppercase.index(item)
            new_index = actual_index + k
            if new_index > 25:
                while new_index >= 25:
                    new_index -= 26
            final_string += uppercase[new_index]
        elif re.match("[a-z]", item):
            actual_index = lowercase.index(item)
            new_index = actual_index + k
            if new_index > 25:
                while new_index >= 25:
                    new_index -= 26
            final_string += lowercase[new_index]
        else:
            final_string += item
    return final_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
