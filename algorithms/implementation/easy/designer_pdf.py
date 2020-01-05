#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
designer-pdf-viewer/problem
'''


def designerPdfViewer(h, word):
    base_ascii = 97
    height_list = list(
        map(
            lambda x: h[ord(x) - base_ascii],
            word
        )
    )
    max_height = max(height_list)
    return max_height * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
