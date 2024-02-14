# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if not root:
            return result
        if not root.left and not root.right:
            result.append(root.val)
            return result

        self.inorder(root, result)
        return result

        
    def inorder(self, rootNode,result):
        if rootNode:
           self.inorder(rootNode.left, result) 
           result.append(rootNode.val)
           self.inorder(rootNode.right, result)  

      
            
        
        


            

        