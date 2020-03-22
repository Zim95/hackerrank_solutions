#!/bin/python3


'''
Problem - https://www.hackerrank.com/
challenges/separate-the-numbers/problem
'''


def separateNumbers(s):
    if len(s) == 1:
        print('NO')
        return

    if len(s) == 0:
        print('YES')
        return

    output = 'NO'
    for i in range(1, int(len(s)/2) + 1):
        pop_value = s[:i]
        start_value = pop_value
        total_visited = start_value
        while True:
            if total_visited == s:
                output = 'YES'
                break
            expected_value = str(int(start_value) + 1)
            retrieved_value = s[len(total_visited):][:len(expected_value)]
            if expected_value == retrieved_value:
                start_value = retrieved_value
                total_visited += retrieved_value
            else:
                break
        if output == 'YES':
            print('YES {}'.format(s[:i]))
            break
    if output == 'NO':
        print('NO')


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
