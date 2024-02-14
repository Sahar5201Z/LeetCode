# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self.minDepthHelper(root)
        
    def minDepthHelper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left= self.minDepthHelper(root.left)
        right=self.minDepthHelper(root.right)
        #because we need to keep going to reach to the leaf
        if left == 0:
            return  right + 1
        if right == 0:
            return  left + 1
        
        return min(left,right)+1