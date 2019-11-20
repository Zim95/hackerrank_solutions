'''
Problem - https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/
problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&
h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&isFullScreen=false
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


# Enter your code here. Read input from STDIN. Print output to STDOUT
def height(root):
    if not root:
        return 0
    if root.left is None and root.right is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    if left_height > right_height:
        h = 1 + left_height
    else:
        h = 1 + right_height
    return h


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    print(height(tree.root))
