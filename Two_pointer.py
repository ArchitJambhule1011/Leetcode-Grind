''' 
Given a sorted array of integers, find two numbers in the array that add up to a specific target.
'''

class Solution:
    def two_sum(self, nums, target):
        left = 0 
        right = len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [nums[left] , nums[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return None
