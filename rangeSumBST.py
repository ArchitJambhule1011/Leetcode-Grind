"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def in_order_traversal(node):
            nonlocal total
            if node is not None:
                in_order_traversal(node.left)
                if low <= node.val <= high:
                    total += node.val
                in_order_traversal(node.right)

        total = 0
        in_order_traversal(root)
        return total