'''
Problem - https://www.hackerrank.com/challenges/tree-top-view/
problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r
%5B%5D=next-challenge&
h_v%5B%5D=zen&h_v%5B%5D=zen&h_v
%5B%5D=zen&isFullScreen=false&h_r=next-challenge&h_v=zen
'''


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def printLeft(root):
    left_list = []
    if not root:
        return []
    if root.left:
        result_left_list = printLeft(root.left)
        left_list.extend(result_left_list)
        left_list.append(root)
        return left_list
    else:
        left_list.append(root)
        return left_list


def printRight(root):
    right_list = []
    if not root:
        return []
    right_list.append(root)
    if root.right:
        result_right_list = printRight(root.right)
        right_list.extend(result_right_list)
    return right_list


def topView(root):
    # Write your code here
    import pdb; pdb.set_trace()
    if root.left:
        left_list = printLeft(root.left)
    else:
        left_list = []
    if root.right:
        right_list = printRight(root.right)
    else:
        right_list = []

    if left_list:
        for l in left_list:
            print(l, end=' ')
    print(root, end=' ')
    if right_list:
        for r in right_list:
            print(r, end=' ')


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    topView(tree.root)
