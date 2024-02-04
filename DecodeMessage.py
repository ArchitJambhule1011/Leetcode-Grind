"""
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

    Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
    Align the substitution table with the regular English alphabet.
    Each letter in message is then substituted using the table.
    Spaces ' ' are transformed to themselves.


"""
import string


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        lower_case = list(string.ascii_lowercase)
        k = [i for i in key if i != ' ']
        hash_map = {k[i]:lower_case[i] for i in range(len(k))}

        words = message.split(' ')
        output = " ".join(''.join(hash_map[char] for char in word) for word in words)
        return output