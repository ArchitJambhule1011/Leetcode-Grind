# Consider it as a dict problem 

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anomaly_dict = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word in anomaly_dict:
                anomaly_dict[sorted_word].append(i)
            else:
                anomaly_dict[sorted_word] = [i]

        result = list(anomaly_dict.values())
        return result