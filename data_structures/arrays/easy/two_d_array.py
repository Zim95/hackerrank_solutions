#!/bin/python3

import math
import os
import random
import re
import sys

'''
Problem - https://www.hackerrank.com/challenges/2d-array/problem
'''


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hour_glass_sum_list = []
    for i in range(0, 4):
        for j in range(0, 4):
            hour_glass = [
                arr[i][j], arr[i][j+1], arr[i][j+2],
                arr[i+1][j+1],
                arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]
            ]
            hour_glass_sum_list.append(sum(hour_glass))
    return max(hour_glass_sum_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
