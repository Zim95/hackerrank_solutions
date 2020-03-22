#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/acm-icpc-team/problem
'''


def acmTeam(topic):
    n = len(topic)
    team_strength_dict = {}
    max_topic_strength = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            a = topic[i]
            b = topic[j]
            topic_strength = [
                '1' if a[k] == '1' or b[k] == '1'
                else '0'
                for k in range(0, len(topic[i]))
            ].count('1')
            if topic_strength > max_topic_strength:
                max_topic_strength = topic_strength
            team_strength_dict['{}_{}'.format(i, j)] = topic_strength
    result = list(team_strength_dict.values()).count(max_topic_strength)
    return [max_topic_strength, result]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
