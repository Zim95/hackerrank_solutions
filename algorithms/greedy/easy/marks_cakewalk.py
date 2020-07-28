#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/marcs-cakewalk/problem
'''


def marcsCakewalk(calorie):
    reverse_calorie = sorted(calorie, reverse=True)
    total = 0
    for i in range(0, len(reverse_calorie)):
        total += (2 ** i) * reverse_calorie[i]
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
