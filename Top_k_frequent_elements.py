from collections import Counter 

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        # Rther than using heap, we are just sorting the counter dictionary 
        sorted_items = sorted(count.items(), key= lambda x : x[1], reverse = True)
        sorted_dict = dict(sorted_items)
        output = [i for i in sorted_dict.keys()]
        return output[:k]
