"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height(left), height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res