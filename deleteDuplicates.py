"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head : ListNode) -> ListNode:
        if head is None:
            return None
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head