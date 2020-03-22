#!/bin/python3
import os


'''
Problem - https://www.hackerrank.com/
challenges/alternating-characters/problem
'''


def alternatingCharacters(s):
    delete_count = 0
    i = 0
    j = i + 1
    while j < len(s) and i < len(s) - 1:
        item = s[i]
        expected_next_item = 'B' if item == 'A' else 'A'
        next_item = s[j]
        if next_item == expected_next_item:
            i = j
            j = i + 1
        else:
            delete_count += 1
            j += 1
    return delete_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
