#!/bin/python3

import math
import os
import random
import re
import sys

'''
Problem Link - https://www.hackerrank.com/challenges/crush/problem

Understandings:
1. https://www.youtube.com/watch?v=scD312I7kkE - Why learn the prefix sum
                                                algorithm
2. https://www.youtube.com/watch?v=pVS3yhlzrlQ - Prefix Sum Algorithm
3. https://www.youtube.com/watch?v=hDhf04AJIRs - Solution to the problem

Algorithm - Prefix Sum
'''


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    number_list = [0] * n
    for query in queries:
        lower, upper, diff = query
        lower_index = lower - 1
        number_list[lower_index] += diff
        if upper < len(number_list):
            number_list[upper] -= diff

    max_number = 0
    accumulator = 0
    for number in number_list:
        accumulator += number
        if accumulator > max_number:
            max_number = accumulator
    return max_number


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
