#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/taum-and-bday/problem
'''


def taumBday(b, w, bc, wc, z):
    if bc == wc or bc == wc + z or wc == bc + z:
        return (b * bc) + (w * wc)

    if bc > wc + z:
        return ((b + w) * wc) + (b * z)

    if wc > bc + z:
        return ((b + w) * bc) + (w * z)

    return (b * bc) + (w * wc)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
