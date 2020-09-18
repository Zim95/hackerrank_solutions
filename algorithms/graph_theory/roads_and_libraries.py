#!/bin/python3

import math
import os
import random
import re
import sys


'''
Problem - https://www.hackerrank.com/challenges/
torque-and-development/problem
'''


def dfs(node_id, graph, visited, count):
    connections = graph[node_id]
    for connection in connections:
        if visited[connection]:
            continue
        else:
            visited[connection] = True
            c, v= dfs(connection, graph, visited, count)
            visited = v
            count = c
    count += 1
    return count, visited


def roadsAndLibraries(n, c_lib, c_road, cities):
    # if cost of road is greater than just build libraries
    # on all the cities
    if c_road > c_lib:
        return n * c_lib

    graph = {}
    visited = {}
    component_costs = 0
    for i in range(1, n+1):
        graph[i] = []
        visited[i] = False
    
    # add edges
    for edge in cities:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    for node_id, connections in graph.items():
        if visited[node_id]:
            continue
        if not connections:
            component_costs += c_lib
            continue
        visited[node_id] = True
        count, v = dfs(node_id, graph, visited, 0)
        visited = v
        component_costs += ((count -1) * c_road) + c_lib
    return component_costs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
