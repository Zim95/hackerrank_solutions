#!/bin/python3


'''
Problem - https://www.hackerrank.com/challenges/
staircase/problem?h_r=next-challenge&h_v=zen
'''


def staircase(n):
    for i in range(0, n):
        a = [' '] * (n - i - 1)
        b = ['#'] * (i + 1)
        c = a + b
        d = ''.join(c)
        print(d)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
