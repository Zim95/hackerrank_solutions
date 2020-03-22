#!/bin/python3
import os


'''
Problem - https://www.hackerrank.com/
challenges/the-love-letter-mystery/problem
'''


def theLoveLetterMystery(s):
    weights = {
        'z': 26, 'h': 8, 'p': 16, 'e': 5,
        't': 20, 'v': 22, 'r': 18, 'd': 4,
        'a': 1, 'f': 6, 'u': 21, 'j': 10,
        'c': 3, 'g': 7, 'o': 15, 'k': 11,
        'b': 2, 'n': 14, 'i': 9, 'x': 24,
        'y': 25, 'm': 13, 'l': 12, 's': 19,
        'q': 17, 'w': 23
    }

    midpoint = int(len(s) / 2)
    stype = len(s) % 2
    if stype:
        fhalf = s[:midpoint]
        shalf = s[midpoint + 1:]
    else:
        fhalf = s[:midpoint]
        shalf = s[midpoint:]

    if fhalf == shalf[::-1]:
        return 0

    no_of_operations = 0
    for i in range(0, len(fhalf)):
        revi = -(i + 1)
        itema = fhalf[i]
        itemb = shalf[revi]
        no_of_operations += abs(weights[itema] - weights[itemb])
    return no_of_operations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
