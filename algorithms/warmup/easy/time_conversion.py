#!/bin/python3

import os
import sys

'''
Problem - https://www.hackerrank.com/challenges/
time-conversion/problem
'''


def timeConversion(s):
    timelist = s.split(":")
    if 'PM' in s:
        if timelist[0] != '12':
            add_time = str(int(timelist[0]) + 12)
            timelist[0] = add_time
        return ':'.join(timelist).replace('PM', '')
    else:
        if timelist[0] == '12':
            timelist[0] = '00'
        return ':'.join(timelist).replace('AM', '')


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
