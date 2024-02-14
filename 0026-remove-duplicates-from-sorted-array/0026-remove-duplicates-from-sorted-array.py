class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count=0
        for i in range(len(nums)):
            if i==0:
                count+=1
            elif nums[i-1]!=nums[i]:
                nums[count] = nums[i]
                count+=1

        return count

"""class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j"""

