#!/bin/python3


import os
import bisect


'''
Problem - https://www.hackerrank.com/challenges/
climbing-the-leaderboard/problem
'''


def climbingLeaderboard(scores, alice):
    scores_set = sorted(list(set(scores)))
    result = []
    for alice_score in alice:
        rank = len(scores_set) - bisect.bisect_right(
            scores_set, alice_score) + 1
        result.append(rank)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
