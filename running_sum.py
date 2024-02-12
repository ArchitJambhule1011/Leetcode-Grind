"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

"""

class Solution:
    def runningsum(self, nums:list[int]) -> list[int]:
        res = []
        running_sum = 0
        for i in nums:
            running_sum += i
            res.append(running_sum)
        return res