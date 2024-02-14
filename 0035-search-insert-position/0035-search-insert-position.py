"""class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch( nums, target,0, len(nums)-1)


    def binarySearch(self, nums: List[int], target: int,left:int, right:int) -> int:
        if(left>right):
            return left
        mid=(left+right)//2
        print(str(left)+"left")
        print(str(right)+"right")
        print(str(mid)+"middd")
        if(target> nums[mid]):
            return self.binarySearch( nums, target,mid+1,right )
        
        if(target<nums[mid]):
            return self.binarySearch( nums, target,left,mid-1)
        if(nums[mid]==target):
            ##print(str(nums.index(target))+"showww")
            return mid"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l

        
        