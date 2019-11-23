#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
migratory-birds/problem?h_r=next-challenge&h_v=zen
'''


def migratoryBirds(arr):
    bird_count = {}
    for bird in arr:
        if bird in bird_count:
            bird_count[bird] += 1
        else:
            bird_count[bird] = 1

    max_frequency = 0
    max_frequency_list = []

    for bird, bird_freq in bird_count.items():
        if max_frequency == 0:
            max_frequency = bird_freq
            max_frequency_list.append(bird)
            continue

        if bird_freq == max_frequency:
            max_frequency_list.append(bird)
            continue

        if bird_freq > max_frequency:
            max_frequency = bird_freq
            max_frequency_list = [bird]

    return min(max_frequency_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
