#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/beautiful-binary-string/problem
'''


def beautifulBinaryString(b):
    return b.count("010")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
