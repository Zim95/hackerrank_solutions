#!/bin/python3
import os

'''
Problem - https://www.hackerrank.com/
challenges/anagram/problem
'''


def anagram(s):
    mid_point = int(len(s)/2)
    lhs = s[:mid_point]
    rhs = s[mid_point:]
    if len(lhs) != len(rhs):
        return -1
    no_of_changes = 0
    lhs_freq = dict([(item, lhs.count(item)) for item in set(lhs)])
    rhs_freq = dict([(item, rhs.count(item)) for item in set(rhs)])
    for rhs_item, rhs_item_count in rhs_freq.items():
        lhs_item_count = lhs_freq.get(rhs_item, 0)
        if rhs_item_count > lhs_item_count:
            no_of_changes += (rhs_item_count - lhs_item_count)
    return no_of_changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
