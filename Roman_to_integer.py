class Solution:
    def roman_to_int(self, s: str) -> bool:
        data_dict = {'I' : 1,
             'V' : 5,
             'X' : 10,
             'L' : 50,
             'C' : 100,
             'D' : 500,
             'M' : 1000}
        result = data_dict[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if data_dict[s[i]] < data_dict[s[i + 1]]:
                result -= data_dict[s[i]]
            else:
                result += data_dict[s[i]]

        return result