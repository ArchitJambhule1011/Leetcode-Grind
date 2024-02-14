"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inordertraversal(self, root : TreeNode) -> list[int]:
        def in_order_traversal(node, output):
            if node is not None:
                in_order_traversal(node.left, output)
                output.append(node.val)
                in_order_traversal(node.right, output)

        output = []
        in_order_traversal(root, output)
        return output