class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] == val and nums[i]!=-1:
                j = len(nums) - 1
                while j > i:
                    if nums[j] != val and nums[j]!=-1:
                        nums[i] = nums[j]
                        nums[j]=-1
                        count += 1
                        break
                    j -= 1
            elif nums[i] != val and nums[i]!=-1:
                print(str(nums[i])+"show")
                count += 1

        return count

    
"""class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index"""