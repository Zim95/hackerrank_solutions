#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/divisible-sum-pairs/problem
'''


def divisibleSumPairs(n, k, ar):
    selected_list = []
    for i, itemi in enumerate(ar):
        for j, itemj in enumerate(ar):
            if i == j:
                continue
            if (itemi + itemj) % k == 0:
                selected_pair = sorted([i, j])
                selected_tuple = (selected_pair[0], selected_pair[1])
                if selected_tuple not in selected_list:
                    selected_list.append(selected_tuple)
    return len(selected_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
