#!/bin/python3

import math
import os
import random
import re
import sys

'''
Problem - https://www.hackerrank.com/challenges/
plus-minus/problem
'''


def plusMinus(arr):
    positives = []
    negatives = []
    zeroes = []
    for item in arr:
        if item < 0:
            negatives.append(item)
        elif item == 0:
            zeroes.append(item)
        else:
            positives.append(item)
    positive_ratio = round(len(positives)/len(arr), 6)
    negative_ratio = round(len(negatives)/len(arr), 6)
    zeroes_ratio = round(len(zeroes)/len(arr), 6)
    print(positive_ratio)
    print(negative_ratio)
    print(zeroes_ratio)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
