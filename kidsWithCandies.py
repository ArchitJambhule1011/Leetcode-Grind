"""
Kids with greates number of candies
"""

class Solution:
    def kidsWithCandies(self, candies:list[int], extraCandies:int) -> list[bool]:
        return [i + extraCandies >= max(candies) for i in candies]