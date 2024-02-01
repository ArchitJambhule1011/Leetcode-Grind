"""
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

"""

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        hash = {}
        for i in range(len(indices)):
            hash[indices[i]] = s[i]

        output = ''
        indices.sort()
        for i in indices:
            if i in hash.keys():
                output += hash[i]

        return hash

