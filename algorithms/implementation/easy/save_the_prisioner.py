#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
save-the-prisoner/problem?h_r=next-challenge&h_v=zen
'''


def saveThePrisoner(n, m, s):
    final_number = (s-1) + m
    if final_number <= n:
        return final_number

    remainder = final_number % n

    if remainder == 0:
        return n
    else:
        return remainder


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
