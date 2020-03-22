#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/non-divisible-subset/problem
'''


def nonDivisibleSubset(k, s):
    # 1. There can be atmost k-1 remainders
    #    for any number/k. So we make a list
    #    whose length is equal to k with zeros
    remainders = [0] * k

    # 2. Now we calculate the frequency of remainders
    for item in s:
        r = item % k
        remainders[r] += 1

    # 3. Theory-
    #    For any sum of two numbers a and b to be divisible
    #    by k, a/k + b/k = k.
    #    We need to select two such numbers that a/k + b/k != k
    #    So first we need to find such pairs and make sure to
    #    include only one of them.
    #    A rule is that for any remainder r it's remainder counterpart
    #    for the sum to be divisible by k is k-r.
    #    eg: 1 and 4, 2 and 3 and so on.
    #    for first pair 1 and 4 our job is to select either 1 or 4
    #    for second pair 2 and 3 our job is to select either 2 or 4
    #    and so on.
    #    for remainder 0, if there are any, there will be atmost 1 count
    #    for the same number(midpoint condition), if there are any, there will
    #       be atmost 1 count
    count = 0
    # if there are numbers with zero remainders
    if remainders[0] > 0:
        count = 1
    for i in range(1, k//2 + 1):
        frequency_a = remainders[i]  # index 1
        frequency_b = remainders[k-i]  # len -1 , i.e. last element
        # midpoint condition: i.e. if both remainders are same
        if i == k - i:
            count = count+1 if remainders[i] else count + 0
            continue
        if frequency_a > frequency_b:
            count += frequency_a
        else:
            count += frequency_b
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
