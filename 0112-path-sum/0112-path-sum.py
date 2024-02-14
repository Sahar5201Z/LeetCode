# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        sum_result=0
        return self.hasPathSumHelper(root,targetSum,sum_result)
        
    def hasPathSumHelper(self, root: Optional[TreeNode], targetSum: int,sum_result: int) -> bool:
        if root is None:
            return False

        sum_result+=root.val
    
        if root.left is None and root.right is None and sum_result == targetSum:
            return True
        
        return self.hasPathSumHelper(root.left,targetSum,sum_result) or self.hasPathSumHelper(root.right,targetSum,sum_result) 
        