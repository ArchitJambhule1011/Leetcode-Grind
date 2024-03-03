"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

"""

class Solution:
    def lemonadeChange(self, bills:list[int]) -> bool:
        stack = []
        for i in bills:
            if i == 5:
                stack.append(i)
            elif i == 10:
                if 5 in stack:
                    stack.remove(5)
                    stack.append(10)
                else:
                    return False
            elif i == 20:
                if 10 in stack and 5 in stack:
                    stack.remove(10)
                    stack.remove(5)
                elif stack.count(5) >= 5:
                    stack.remove(5)
                    stack.remove(5)
                    stack.remove(5)
                else:
                    return False
        return True