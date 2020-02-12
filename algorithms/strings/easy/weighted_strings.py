#!/bin/python3

import math
import os
import random
import re
import sys


def weightedUniformStrings(s, queries):
    weights = {
        'z': 26, 'h': 8, 'p': 16, 'e': 5,
        't': 20, 'v': 22, 'r': 18, 'd': 4,
        'a': 1, 'f': 6, 'u': 21, 'j': 10,
        'c': 3, 'g': 7, 'o': 15, 'k': 11,
        'b': 2, 'n': 14, 'i': 9, 'x': 24,
        'y': 25, 'm': 13, 'l': 12, 's': 19,
        'q': 17, 'w': 23
    }

    import pdb; pdb.set_trace()
    print(s)
    frequency_dict = dict([(item, s.count(item))for item in set(s)])
    print(s)

    # the base weight of any one key of freqeueny dict should divide
    # the query number
    # then the count of the item should be greater than or equal to the
    # the quotient
    result = []
    for query in queries:
        status = 'No'
        for item, count in frequency_dict.items():
            item_weight = weights[item]
            remainder = query % item_weight
            if not remainder:
                quotient = query / item_weight
                if count >= quotient:
                    status = 'Yes'
                    break
                else:
                    continue
            else:
                continue
        result.append(status)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    print(','.join(result))
    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
