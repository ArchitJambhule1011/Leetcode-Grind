"""
You are given a 0-indexed array of string words and two integers left and right.

A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

"""

class Solution:
    def vowelStrings(self, words: list[str], left: int, right:int) -> int:
        vowels = ['a','e','i','o','u']
        words = words[left: right + 1]
        count = 0
        for i in words:
            if i[0] in vowels and i[-1] in vowels:
                count += 1
            else:
                pass

        return count