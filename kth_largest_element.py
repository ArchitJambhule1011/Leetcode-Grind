class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]