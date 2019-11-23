#!/bin/python3

import os
import sys


'''
Problem - https://www.hackerrank.com/
challenges/electronics-shop/problem
'''


def getMoneySpent(keyboards, drives, b):
    sum_list = []
    for keyboard in keyboards:
        for drive in drives:
            sum_list.append(keyboard+drive)

    sum_list = sorted(sum_list)

    filtered_sum_list = []
    for sum_value in sum_list:
        if sum_value <= b:
            filtered_sum_list.append(sum_value)
        else:
            break

    if len(filtered_sum_list):
        return max(filtered_sum_list)
    else:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
