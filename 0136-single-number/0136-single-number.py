class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''min_num = min(nums)
        nums_helper = [0] * (max(nums) - min_num + 1)
        
        for i in nums:
            ##print (i - min_num)
            nums_helper[i - min_num] += 1

        for j in range(len(nums_helper)):
            if nums_helper[j] == 1:
                return j + min_num'''
        result = 0
        for num in nums:
            result ^= num
        return result
        