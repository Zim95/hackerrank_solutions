#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/
challenges/mars-exploration/
problem?h_r=next-challenge&h_v=zen
'''


def marsExploration(s):
    index = 0
    message_list = []
    while index < len(s):
        try:
            message_list.append(s[index: index+3])
        except Exception as e:
            message_list.append(s[index: len(s)])
        index = index + 3
    difference = 0
    for message in message_list:
        for i in range(0, 3):
            message_list = ['S', 'O', 'S']
            if message[i] != message_list[i]:
                difference += 1
    return difference


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
