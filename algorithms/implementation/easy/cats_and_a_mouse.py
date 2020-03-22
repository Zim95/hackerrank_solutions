#!/bin/python3
import os


'''
Problem - https://www.hackerrank.com/
challenges/cats-and-a-mouse/problem
'''


def catAndMouse(x, y, z):
    x_diff = abs(x - z)
    y_diff = abs(y - z)

    if x_diff == y_diff:
        return 'Mouse C'

    if x_diff > y_diff:
        return 'Cat B'
    else:
        return 'Cat A'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
