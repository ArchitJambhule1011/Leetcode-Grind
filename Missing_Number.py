'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

'''

#Approach to use is to calculated the sum of n first natural elements and then subtract the actual sum. We will get the number

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual