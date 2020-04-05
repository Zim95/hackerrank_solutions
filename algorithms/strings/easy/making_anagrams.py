#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/making-anagrams/
problem?h_r=next-challenge&h_v=zen
'''


def makingAnagrams(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)
    freq_s1 = dict([(item, s1.count(item)) for item in s1_set])
    freq_s2 = dict([(item, s2.count(item)) for item in s2_set])

    common_set = s1_set.intersection(s2_set)

    s1_set_excluded = s1_set - common_set
    s2_set_excluded = s2_set - common_set

    s1_remove_count = sum([freq_s1[item] for item in s1_set_excluded])
    s2_remove_count = sum([freq_s2[item] for item in s2_set_excluded])

    exclude_count = s1_remove_count + s2_remove_count

    for item in common_set:
        s1_item_freq = freq_s1[item]
        s2_item_freq = freq_s2[item]
        exclude_count += abs(s1_item_freq - s2_item_freq)
    return exclude_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
