#!/bin/python3


import os


'''
Problem - https://www.hackerrank.com/
challenges/maximum-perimeter-triangle/
problem?h_r=next-challenge&h_v=zen&
h_r=next-challenge&h_v=zen
'''


def is_triangle(points):
    return points[0] + points[1] > points[2]


def maximumPerimeterTriangle(sticks):
    sticks = sorted(sticks)
    all_triangles = []
    for i in range(0, len(sticks) - 2):
        points = sticks[i: i + 3]
        if not is_triangle(points):
            continue
        all_triangles.append(points)

    maximum_side = -1
    minimum_side = -1
    max_triangle = None
    if not all_triangles:
        return [-1]
    else:
        for triangle in all_triangles:
            longest_side = max(triangle)
            shortest_side = min(triangle)
            if longest_side > maximum_side:
                maximum_side = longest_side
                minimum_side = shortest_side
                max_triangle = triangle
            elif longest_side == maximum_side:
                if shortest_side > minimum_side:
                    maximum_side = longest_side
                    minimum_side = shortest_side
                    max_triangle = triangle
    return max_triangle


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
