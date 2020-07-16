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

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        side = "left" * (value < self.value) + "right" * (value >= self.value)
        node = getattr(self, side, None)
        if side is "":
            pass
        elif node is None:
            setattr(self, side, BSTNode(value))
        else:
            getattr(node, "insert")(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        side = "left" * (target < self.value) + "right" * (target > self.value)
        node = getattr(self, side, None)
        return self.value == target or (node is not None and (node.value == target or node.contains(target)))

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        (not self.left is None) and self.left.for_each(fn)
        (not self.right is None) and self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        (not node.left is None) and node.in_order_print(node.left)
        print(node.value)
        (not node.right is None) and node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        print(node.value)
        (not self.left is None) and self.left.bft_print(self.left)
        (not self.right is None) and self.right.bft_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        (not self.right is None) and self.right.bft_print(self.right)
        (not self.left is None) and self.left.bft_print(self.left)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        (not self.right is None) and self.right.bft_print(self.right)
        (not self.left is None) and self.left.bft_print(self.left)
        print(node.value)

if __name__ == "__main__":
    bst = BSTNode(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)

    print(bst.bft_print(bst))
