"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

"""

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        word_1 = ''
        for i in word1:
            word_1 += i

        word_2 = ''
        for i in word2:
            word_2 += i

        return word_1 == word_2