"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
import dis

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        side = "left" if value < self.value else "right"
        node = getattr(self, side)
        return node is None and not setattr(self, side, BSTNode(value)) or node.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        side = "left" if target < self.value else "right"
        node = getattr(self, side)
        return self.value == target or (
        node is not None and (node.value == target or node.contains(target)))

    # Return the maximum value found in the tree
    def get_max(self):
        return self.value if self.right is None else self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        self.left is None or self.left.for_each(fn)
        return self.right is None or self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.left is None or node.in_order_print(node.left)
        print(node.value)
        return node.right is None or node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        print(node.value)
        self.left is None or self.left.bft_print(self.left)
        return self.right is None or self.right.bft_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        self.left is None or self.left.bft_print(self.left)
        return self.right is None or self.right.bft_print(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        self.left is None or self.left.bft_print(self.left)
        self.right is None or self.right.bft_print(self.right)
        return print(node.value)

if __name__ == "__main__":
    bst = BSTNode(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)

    dis.dis(bst.insert)
