#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/strange-code/problem
'''


def strangeCounter(t):
    start_value = 3
    index = 0
    while True:
        index += start_value
        if t > index:
            start_value = start_value * 2
            continue
        else:
            break
    return (index - t) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
