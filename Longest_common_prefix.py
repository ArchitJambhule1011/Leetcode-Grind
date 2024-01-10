class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        common = []

        first , last = strs[0] , strs[-1]
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                common.append(first[i])
            else:
                break 

        return ''.join(common) 