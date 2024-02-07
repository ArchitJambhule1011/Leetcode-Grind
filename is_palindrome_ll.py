"""
Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current = head
        nodes = []
        while current is not None:
            nodes.append(current.val)
            current = current.next
        
        return nodes == nodes[::-1]
