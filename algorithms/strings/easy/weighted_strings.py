#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/weighted-uniform-string/problem
'''


def weightedUniformStrings(s, queries):
    numbers = set()
    prev_char = -1
    length = 0
    for char in s:
        weight = ord(char) - ord('a') + 1
        if char == prev_char:
            length += 1
            numbers.add(weight * length)
        else:
            prev_char = char
            length = 1
            numbers.add(weight)
    result = []
    for query in queries:
        if query in numbers:
            result.append('Yes')
        else:
            result.append('No')
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
