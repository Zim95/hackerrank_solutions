#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/hackerrank-in-a-string/
problem?h_r=next-challenge&h_v=zen&
h_r=next-challenge&h_v=zen
'''


def hackerrankInString(s):
    final_string = ''
    if 'h' in s:
        final_string += 'h'
        h_index = s.index('h') + 1
        if h_index < len(s):
            s = s[h_index:]
        else:
            return 'NO'
    else:
        return 'NO'
    if 'a' in s:
        final_string += 'a'
        a_index = s.index('a') + 1
        if h_index < len(s):
            s = s[a_index:]
        else:
            return 'NO'
    else:
        return 'NO'
    if 'c' in s:
        final_string += 'c'
        c_index = s.index('c') + 1
        if c_index < len(s):
            s = s[c_index:]
        else:
            return 'NO'
    else:
        return 'NO'
    if 'k' in s:
        final_string += 'k'
        k_index = s.index('k') + 1
        if k_index < len(s):
            s = s[k_index:]
        else:
            return 'NO'
    else:
        return 'NO'
    if 'e' in s:
        final_string += 'e'
        e_index = s.index('e') + 1
        if e_index < len(s):
            s = s[e_index:]
        else:
            return 'NO'
    else:
        return 'NO'
    if 'r' in s:
        final_string += 'r'
        r_index = s.index('r') + 1
        if r_index < len(s):
            s = s[r_index:]
        else:
            return 'NO'
    else:
        return 'NO'
    if 'r' in s:
        final_string += 'r'
        r_index = s.index('r') + 1
        if r_index < len(s):
            s = s[r_index:]
        else:
            return 'NO'
    else:
        return 'NO'
    if 'a' in s:
        final_string += 'a'
        a_index = s.index('a') + 1
        if a_index < len(s):
            s = s[a_index:]
        else:
            return 'NO'
    else:
        return 'NO'
    if 'n' in s:
        final_string += 'n'
        n_index = s.index('n') + 1
        if n_index < len(s):
            s = s[n_index:]
        else:
            return 'NO'
    else:
        return 'NO'
    if 'k' in s:
        final_string += 'k'
        k_index = s.index('k') + 1
        if k_index < len(s):
            s = s[k_index:]
    else:
        return 'NO'
    if final_string == 'hackerrank':
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
