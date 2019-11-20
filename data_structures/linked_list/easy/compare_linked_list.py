#!/bin/python3

import os
import sys

'''
Problem - https://www.hackerrank.com/challenges/compare-two-linked-lists/
problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def compare_lists(llist1, llist2):
    head1 = llist1
    head2 = llist2
    counter1 = head1
    counter2 = head2

    while True:
        if counter1 is not None and counter2 is None:
            return 0
        if counter2 is not None and counter1 is None:
            return 0
        if counter1.data != counter2.data:
            return 0
        counter1 = counter1.next
        counter2 = counter2.next
        if counter1 is None and counter2 is None:
            return 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
