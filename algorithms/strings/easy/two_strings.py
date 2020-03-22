#!/bin/python3
import os

'''
Problem - https://www.hackerrank.com/
challenges/two-strings/problem
'''


def twoStrings(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    if set_s1.intersection(set_s2):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
