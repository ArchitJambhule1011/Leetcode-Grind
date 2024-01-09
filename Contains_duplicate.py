from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = Counter(nums)
        max_value = max(count.values())
        if max_value > 1:
            return True
        else:
            return False