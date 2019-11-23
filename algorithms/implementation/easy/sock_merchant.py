#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
sock-merchant/problem?h_r=next-challenge&h_v=zen&
h_r=next-challenge&h_v=zen&h_r=next-challenge&
h_v=zen&h_r=next-challenge&h_v=zen
'''


def sockMerchant(n, ar):
    sock_color_dict = {}

    for sock_color in ar:
        if sock_color in sock_color_dict:
            sock_color_dict[sock_color] += 1
        else:
            sock_color_dict[sock_color] = 1

    total_pairs = 0
    for sock_color, count in sock_color_dict.items():
        sock_pairs = int(count/2)
        total_pairs += sock_pairs

    return total_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
