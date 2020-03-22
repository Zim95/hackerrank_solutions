#!/bin/python3
import os


'''
Problem - https://www.hackerrank.com/
challenges/game-of-thrones/problem
'''


def gameOfThrones(s):
    freq_dict = dict([(item, s.count(item)) for item in set(s)])
    no_of_odds = 0
    for item, item_count in freq_dict.items():
        if item_count % 2 != 0:
            no_of_odds += 1
    if no_of_odds > 1:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
