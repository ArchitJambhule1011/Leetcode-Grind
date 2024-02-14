"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        def post_order(node, output):
            if node is not None:
                post_order(node.left, output)
                post_order(node.right, output)
                output.append(node.val)

        output = []
        post_order(root, output)
        return output
        