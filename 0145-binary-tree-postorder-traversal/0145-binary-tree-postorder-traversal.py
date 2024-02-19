# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]: 
        if root is None: 
            return None
        result =[]*100
        return self.postorderTraversalHelper(root,result)

    def postorderTraversalHelper(self, root: Optional[TreeNode], result:List[int]) -> List[int]:
        if root is None: 
            return result
        self.postorderTraversalHelper(root.left,result)
        self.postorderTraversalHelper(root.right,result)
        result.append(root.val)
        return result

        