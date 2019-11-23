#!/bin/python3

import os
import sys


'''
Problem - https://www.hackerrank.com/
challenges/drawing-book/problem
'''


def backwardSearch(number_list, p):
    number_list_reverse = number_list[::-1]

    count = 0
    for item in number_list_reverse:
        if p in item:
            return count
        count += 1
    return count


def forwardSearch(number_list, p):
    count = 0

    for item in number_list:
        if p in item:
            return count
        count += 1
    return count


def pageCount(n, p):
    number_list = [(None, 1)]
    for i in range(2, n+1, 2):
        number_list.append(
            (
                i,
                i+1 if i+1 <= n else None
            )
        )

    forward_result = forwardSearch(number_list, p)
    backward_result = backwardSearch(number_list, p)
    if forward_result < backward_result:
        return forward_result
    else:
        return backward_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
