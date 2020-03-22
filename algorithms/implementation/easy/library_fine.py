#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/challenges/
library-fine/problem
'''


def libraryFine(d1, m1, y1, d2, m2, y2):
    return_date = '{}-{}-{}'.format(y1, m1, d1)
    due_date = '{}-{}-{}'.format(y2, m2, d2)

    if return_date <= due_date:
        return 0
    else:
        if y1 == y2 and m1 == m2:
            return 15 * (d1 - d2)
        elif y1 == y2 and m1 > m2:
            return 500 * (m1 - m2)
        else:
            return 10000


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
