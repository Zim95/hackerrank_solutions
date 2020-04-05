#!/bin/python3
import os


'''
Problem - https://www.hackerrank.com/
challenges/palindrome-index/problem
'''


def check_palindrome(s):
    return s == s[::-1]


def palindromeIndex(s):
    if check_palindrome(s):
        return -1

    for index in range(0, len(s)//2):
        negative_index = -(index + 1)
        if s[index] == s[negative_index]:
            continue
        if check_palindrome(s[:index] + s[index + 1:]):
            return index
        else:
            return len(s) - (-1 * negative_index)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
