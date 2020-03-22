#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/challenges/
cut-the-sticks/problem
'''


def cutTheSticks(arr):
    result = []
    while arr:
        cut_value = min(arr)
        number_of_cuts = 0
        for i in range(0, len(arr)):
            arr[i] -= cut_value
            number_of_cuts += 1
        arr = list(filter(lambda x: x > 0, arr))
        result.append(number_of_cuts)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
