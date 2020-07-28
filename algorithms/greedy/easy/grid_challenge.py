#!/bin/python3


import os
from collections import defaultdict


'''
Problem - https://www.hackerrank.com/
challenges/grid-challenge/problem
'''


def gridChallenge(grid):
    column_wise = defaultdict(list)
    for grid_item in grid:
        sorted_grid_item = sorted(grid_item)
        for index, item in enumerate(sorted_grid_item):
            column_wise[index].append(item)
    for key, value in column_wise.items():
        if value != sorted(value):
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
