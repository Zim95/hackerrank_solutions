#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/angry-professor/problem
'''


def angryProfessor(k, a):
    sorted_a = sorted(a)

    student_count = 0
    for student_arrival_time in sorted_a:
        if student_arrival_time > 0:
            break
        student_count += 1

    if student_count < k:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
