"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

"""

class Solution:
    def mostWordsFound(self, sentences : list[str]) -> int:
        words = [len(i.split(' ')) for i in sentences]
        return max(words)