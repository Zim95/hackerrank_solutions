#!/bin/python3
import os


'''
Problem - https://www.hackerrank.com/
challenges/funny-string/problem
'''


def funnyString(s):
    ascii_values = {
        'z': 122, 'h': 104, 'p': 112, 'e': 101,
        't': 116, 'v': 118, 'r': 114, 'd': 100,
        'a': 97, 'f': 102, 'u': 117, 'j': 106,
        'c': 99, 'g': 103, 'o': 111, 'k': 107,
        'b': 98, 'n': 110, 'i': 105, 'x': 120,
        'y': 121, 'm': 109, 'l': 108, 's': 115,
        'q': 113, 'w': 119
    }
    r = s[::-1]
    for i in range(0, len(s)-1):
        frwrd_diff = abs(ascii_values[s[i+1]] - ascii_values[s[i]])
        rvrse_diff = abs(ascii_values[r[i+1]] - ascii_values[r[i]])
        if frwrd_diff != rvrse_diff:
            return 'Not Funny'
    return 'Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
