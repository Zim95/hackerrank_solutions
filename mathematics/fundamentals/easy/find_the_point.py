#!/bin/python3

import os
import sys


'''
Problem - https://www.hackerrank.com/
challenges/find-point/problem
'''


def findPoint(px, py, qx, qy):
    diffx = qx - px
    diffy = qy - py
    rx = qx + diffx
    ry = qy + diffy
    return [rx, ry]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        pxPyQxQy = input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
