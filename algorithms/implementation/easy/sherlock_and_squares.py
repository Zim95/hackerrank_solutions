#!/bin/python3

import math
import os


'''
Problem - https://www.hackerrank.com/
challenges/sherlock-and-squares/problem

Explanation - This is a formula to find perfect
squares between two numbers
'''


def squares(a, b):
    return int(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
