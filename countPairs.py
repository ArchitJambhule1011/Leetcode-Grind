""" 
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
"""

class Solution:
    def countPairs(self, nums : list[int], target : int) -> int:
        nums.sort()
        count = 0
        lo = 0
        high = len(nums) - 1

        while lo < high:
            if nums[lo] + nums[high] < target:
                count += high - lo
                lo += 1
            else:
                high -= 1

        return count