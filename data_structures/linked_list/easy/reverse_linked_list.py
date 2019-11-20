#!/bin/python3

import math
import os
import random
import re
import sys

'''
Problem link -
https://www.hackerrank.com/challenges/reverse-a-linked-list/
problem?h_r=next-challenge&h_v=zen
'''


class SinglyLinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = SinglyLinkedListNode(None)
        self.tail = SinglyLinkedListNode(None)

    def insert_node(self, item):
        node = SinglyLinkedListNode(item)

        if self.head.next is None and self.tail.next is None:
            node.next = self.tail
            self.head.next = node
        else:
            counter = self.head.next
            while counter.next != self.tail:
                counter = counter.next
            counter.next = node
            node.next = self.tail


def print_singly_linked_list(llist, delimeter, fptr):
    for item in llist:
        fptr.write(str(item) + delimeter)


def reverse(head):
    stack = []
    counter = head.next
    while counter.next is not None:
        stack.append(counter.data)
        counter = counter.next
    stack_reverse = stack[::-1]
    return stack_reverse


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
