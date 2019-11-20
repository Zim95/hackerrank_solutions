#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
mini-max-sum/problem?h_r=next-challenge&
h_v=zen&h_r=next-challenge&h_v=zen
'''


def miniMaxSum(arr):
    sum_list = []
    for i in range(0, len(arr)):
        if i == 0:
            sum_list.append(
                sum(arr[1:])
            )
        elif i == len(arr) - 1:
            sum_list.append(
                sum(arr[:-1])
            )
        else:
            first_half = arr[:i]
            second_half = arr[i+1:]
            total = first_half + second_half
            sum_list.append(
                sum(total)
            )
    print(min(sum_list), max(sum_list))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
