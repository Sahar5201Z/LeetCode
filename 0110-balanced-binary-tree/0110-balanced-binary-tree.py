# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.isBalancedHelper(root)!=-1
    

    def isBalancedHelper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left= self.isBalancedHelper(root.left)
        if left==-1:
            return -1
        right=self.isBalancedHelper(root.right)
        if right==-1:
            return -1

        if(abs(left-right)>1):
             return -1
        
        return max(left,right)+1