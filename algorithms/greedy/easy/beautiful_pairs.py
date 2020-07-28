#!/bin/python3


import os
from collections import defaultdict


'''
Problem - https://www.hackerrank.com/
challenges/beautiful-pairs/problem

Solution was found from the discussion page
'''


def beautifulPairs(A, B):
    freq_A = defaultdict(int)
    freq_B = defaultdict(int)
    for i in range(0, len(A)):
        freq_A[A[i]] += 1
        freq_B[B[i]] += 1
    pairs = 0
    flag = False
    for number, count in freq_A.items():
        freq_B_count = freq_B[number]
        pairs += min([count, freq_B_count])
        if (count != freq_B_count):
            # if the frequency is different
            flag = True
    if flag:
        # if the frequency is different then there will be one addition
        # as we need to change one number from B to match the overall frequency
        return pairs + 1
    # if the frequency is the same, there will be one subtraction
    # because we will end up changing the value of one element from B
    # regardless
    return pairs - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
