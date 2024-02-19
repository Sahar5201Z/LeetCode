# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return None
        result =[]*100
        return self.preorderTraversalHelper(root,result)

    def preorderTraversalHelper(self, root: Optional[TreeNode], result:List[int]) -> List[int]:
        if root is None: 
            return result
        result.append(root.val)
        self.preorderTraversalHelper(root.left,result)
        self.preorderTraversalHelper(root.right,result)
        return result

        