"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head : ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            slow = slow.next

        while slow is not None:
            slow = slow.next
            fast = fast.next
        
        fast.next = fast.next.next
        return dummy.next