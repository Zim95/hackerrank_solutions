#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/extra-long-factorials/problem
'''


def extraLongFactorials(n):
    print(math.factorial(n))


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
