"""
Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

"""

class Solution:
    def removeTrailingZeros(self, num : str) -> str:
        num_list = list(num)
        count = 0
        for i in num_list[::-1]:
            if i == '0':
                count += 1
            elif i != '0':
                break

        if count > 0:
            return ''.join(num_list[:-count])
        else:
            return ''.join(num_list)