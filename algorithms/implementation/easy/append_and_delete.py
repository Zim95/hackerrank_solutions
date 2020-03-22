#!/bin/python3

import os


'''
Problem - https://www.hackerrank.com/challenges/
append-and-delete/problem
'''


def appendAndDelete(s, t, k):
    # first case is when the strings are equal.
    # Here you need atleast twice the length of the whole string
    if s == t:
        return 'Yes'

    if len(s) < len(t):
        if len(set(s)) == 1 and len(s) > 1:
            return 'Yes'
        if k >= (len(s) + len(t)):
            return 'Yes'
        else:
            return 'No'
    # for everything else, we need to check upto where the match happen
    max_len = max([len(s), len(t)])

    mismatch_point = -1
    for i in range(0, max_len):
        if i >= len(s) or i >= len(t):
            mismatch_point = i
            break
        sitem = s[i]
        titem = t[i]
        if sitem == titem:
            continue
        else:
            mismatch_point = i
            break

    number_of_ops = (
        len(s) - mismatch_point
    ) + (len(t) - mismatch_point)
    if k >= number_of_ops:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
