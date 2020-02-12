#!/bin/python3
import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # theory is:
    # rowwise difference and colwise difference
    # should be the same as per some value
    min_top_left = (r_q, c_q)
    min_top_right = (r_q, c_q)
    min_down_left = (r_q, c_q)
    min_down_right = (r_q, c_q)
    min_up = (r_q, c_q)
    min_down = (r_q, c_q)
    min_left = (r_q, c_q)
    min_right = (r_q, c_q)

    for obstacle in obstacles:
        obs_row = obstacle[0]
        obs_col = obstacle[1]

        x_diff = obs_row - r_q
        y_diff = obs_col - c_q

        if abs(x_diff) != abs(y_diff):
            continue
        if x_diff < 0 and y_diff > 0:
            # top left diagonal
            ed_obs = euclidian_distance(
                (r_q, c_q),
                (obs_row, obs_col)
            )
            ed_min_top_left = euclidian_distance(
                (r_q, c_q),
                min_top_left
            )
            if ed_obs < ed_min_top_left:
                ed_min_top_left = (obs_row, obs_col)
        elif x_diff < 0 and y_diff < 0:
            # down left diagonal
            ed_obs = euclidian_distance(
                (r_q, c_q),
                (obs_row, obs_col)
            )
            ed_min_top_left = euclidian_distance(
                (r_q, c_q),
                min_top_left
            )
            if ed_obs < ed_min_top_left:
                ed_min_top_left = (obs_row, obs_col)
        elif x_diff > 0 and y_diff > 0:
            # top right diagonal
            if obs_row < min_down_left[0]:
                min_down_left
        elif x_diff > 0 and y_diff < 0:
            # down right diagonal
            pass
        elif x_diff < 0 and y_diff == 0:
            # left
            pass
        elif x_diff > 0 and y_diff == 0:
            # right
            pass
        elif x_diff == 0 and y_diff > 0:
            # up
            pass
        elif x_diff == 0 and y_diff < 0:
            # down
            pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
