#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/gem-stones/problem
'''


def gemstones(arr):
    final_set = set(arr[0])
    for i in range(1, len(arr)):
        final_set = final_set.intersection(set(arr[i]))
    return len(final_set)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
