#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/luck-balance/
problem?h_r=next-challenge&h_v=zen
'''


def luckBalance(k, contests):
    filtered_scores = []
    extra_score = 0
    for contest in contests:
        if contest[1] == 1:
            filtered_scores.append(contest[0])
        else:
            extra_score += contest[0]
    sorted_filtered_scores = sorted(filtered_scores)
    need_to_win = len(filtered_scores) - k if len(filtered_scores) > k else 0
    result = sorted_filtered_scores[need_to_win:]
    final_score = sum(result) + extra_score - sum(
        sorted_filtered_scores[:need_to_win])
    return final_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
