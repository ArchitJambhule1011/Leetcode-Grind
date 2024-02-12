"""
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

"""

import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            gcd = math.gcd(current.val , current.next.val)
            new_node = ListNode(gcd)
            new_node.next = current.next
            current.next = new_node

            current = current.next.next

        return head