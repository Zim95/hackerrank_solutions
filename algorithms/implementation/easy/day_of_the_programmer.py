#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
day-of-the-programmer/
problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''


def dayOfProgrammer(year):
    georgian_condition1 = (year % 400 == 0)
    georgian_condition2 = (year % 4 == 0 and year % 100 != 0)

    julian_condition = (year % 4 == 0)

    thirteen_response = '13.09.{}'.format(str(year))
    twelve_response = '12.09.{}'.format(str(year))

    if year == 1918:
        return '26.09.1918'

    if year > 1918:
        if georgian_condition1 and not georgian_condition2:
            return twelve_response
        if not georgian_condition1 and georgian_condition2:
            return twelve_response
        return thirteen_response
    else:
        if julian_condition:
            return twelve_response
        return thirteen_response


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
