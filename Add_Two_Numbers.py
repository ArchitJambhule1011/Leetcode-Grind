class Node:
    def __init__(self, data = 0, next = None):
        self.data = data 
        self.next = next 

class Solution:
    def addTwoNumbers(self, l1 , l2):
        dummy_head = Node()
        current = dummy_head 
        carry = 0 

        while l1 or l2 or carry:
            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0 

            total_sum = val1 + val2 + carry 
            carry = total_sum // 10
            current.next = Node(total_sum % 10)

            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 
            
            current = current.next 
    
        return dummy_head.next