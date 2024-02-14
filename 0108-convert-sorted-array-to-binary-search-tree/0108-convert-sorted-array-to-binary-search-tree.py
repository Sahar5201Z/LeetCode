# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums :
            return None
        
        left= 0
        right= len(nums)-1
        mid=(right + left)//2
        root = TreeNode(nums[mid])
        root.left=self.sortedArrayToBSTHelper( nums,left,mid-1)
        root.right=self.sortedArrayToBSTHelper( nums,mid+1, right)
        return root

    def sortedArrayToBSTHelper(self, nums,left,right)-> Optional[TreeNode]:
        if left > right:
            return None
        mid=(right + left)//2
        root = TreeNode(nums[mid])
        root.left=self.sortedArrayToBSTHelper( nums,left,mid-1)
        root.right=self.sortedArrayToBSTHelper( nums,mid+1,right)
        return root'''

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


        

        