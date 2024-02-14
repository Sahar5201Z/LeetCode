# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftSide=root.left
        rightSide=root.right
        return self.isSymmetricHelper(leftSide,rightSide)

    

    def isSymmetricHelper(self,firstTree,secondTree)->bool:
        if firstTree and secondTree:
           left_result=self.isSymmetricHelper(firstTree.left,secondTree.right) 
           print(firstTree.val)
           if(firstTree.val!=secondTree.val):
             return False
           right_result =self.isSymmetricHelper(firstTree.right,secondTree.left)  
           
           return left_result and right_result

        print("else")   
        return firstTree is None and secondTree is None
        
        