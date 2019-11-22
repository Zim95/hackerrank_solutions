#!/bin/python3

import math
import os
import random
import re
import sys
'''
Problem - https://www.hackerrank.com/challenges/
breaking-best-and-worst-records/
problem?h_r=next-challenge&h_v=zen
'''


def breakingRecords(scores):

    minimum_score = 0
    minimum_score_record = 0

    maximum_score = 0
    maximum_score_record = 0

    prev_score = 0
    for game_no, score in enumerate(scores):
        if game_no == 0:
            minimum_score = score
            maximum_score = score
            prev_score = score
        else:
            if score < prev_score:
                if score < minimum_score:
                    minimum_score = score
                    minimum_score_record += 1
            elif score > prev_score:
                if score > maximum_score:
                    maximum_score = score
                    maximum_score_record += 1
    return [maximum_score_record, minimum_score_record]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
