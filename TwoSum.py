class Two_Sum:
    def __init__(self, nums , target):
        self.nums = nums
        self.target = target
    
    def iterative(self):
        for i , num_0 in enumerate(self.nums):
            for j , num_1 in enumerate(self.nums):
                if num_0 + num_1 == self.target:
                    return i , j
                
    def two_sum_index(self):
        num_dict = {}
        for i , num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return None
    
    def two_sum_number(self):
        num_dict = {}
        for i in self.nums:
            complement = self.target - i
            if complement in num_dict:
                return [complement , i]
            
            num_dict[i] = True

        return None 
