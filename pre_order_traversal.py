"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        def pre_order(node, output):
            if node is not None:
                output.append(node.val)
                pre_order(node.left, output)
                pre_order(node.right, output)

        output = []
        pre_order(root, output)
        return output