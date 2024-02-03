"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

"""
class Solution:
    def sortSentence(self, s:str) -> str:
        s = list(s.split(' '))
        actual_word = []
        pos = []
        for i in s:
            actual_word.append(i[:-1])
        
        for i in s:
            pos.append(int(i[-1]))

        hash = {}
        for i in range(len(actual_word)):
            hash[pos[i]] = actual_word[i]

        reconstructed = ' '.join(hash[i] for i in range(1, len(s) + 1))
        return reconstructed