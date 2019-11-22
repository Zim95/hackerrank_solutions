#!/bin/python3

import math
import os
import random
import re
import sys

'''
Problem - https://www.hackerrank.com/challenges/
grading/problem
'''


def gradingStudents(grades):
    # Write your code here
    length_of_multiples = int(max(grades)/5) + 1
    grade_list = []
    for i in range(0, length_of_multiples + 1):
        grade_list.append(i * 5)
    grade_list = sorted(grade_list)

    result = []
    for grade in grades:
        index = int(grade/5) + 1
        target_grade = grade_list[index]
        if target_grade - grade < 3 and target_grade >= 40:
            result.append(target_grade)
        else:
            result.append(grade)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
