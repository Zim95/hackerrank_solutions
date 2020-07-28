#!/bin/python3
import math


'''
Problem - https://www.hackerrank.com/
challenges/lowest-triangle/problem
'''


def lowestTriangle(base, area):
    # Theory: area = 1/2 * base * height
    h = 2 * (area / base)
    return int(math.ceil(h))


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
