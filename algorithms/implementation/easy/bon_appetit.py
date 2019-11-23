#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
bon-appetit/problem?h_r=next-challenge&
h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''


def bonAppetit(bill, k, b):
    del bill[k]
    b_actual = sum(bill)/2
    if b - b_actual == 0:
        print('Bon Appetit')
    else:
        print(int(b - b_actual))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
