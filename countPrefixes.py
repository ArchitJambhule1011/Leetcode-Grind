"""
You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.

Return the number of strings in words that are a prefix of s.

"""

class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        substrings = []
        l = 0
        r = 0
        while r < len(s):
            sub = s[l:r + 1]
            substrings.append(sub)
            r += 1

        output = []
        for i, j in enumerate(words):
            if j in substrings:
                output.append(i)

        return len(output)