"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

"""

class Solution:
    def shuffle(self, nums : list, n : int) -> list:
        first = nums[:n]
        second = nums[n:]
        output = []
        for i in range(n):
            output.append(first[i])
            output.append(second[i])
        return output