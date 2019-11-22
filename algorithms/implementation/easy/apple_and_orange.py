#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
apple-and-orange/problem?h_r=next-challenge&h_v=zen
'''


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_list = []
    for apple in apples:
        apple_list.append(a + apple)

    orange_list = []
    for orange in oranges:
        orange_list.append(b + orange)

    apple_count = 0
    for app in apple_list:
        if app >= s and app <= t:
            apple_count += 1

    orange_count = 0
    for orr in orange_list:
        if orr >= s and orr <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
