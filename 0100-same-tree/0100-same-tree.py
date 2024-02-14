# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return self.isSameTreeHelper( p,q)
        

    def isSameTreeHelper(self,firstTree,secondTree)->bool:
        if firstTree and secondTree:
           left_result=self.isSameTreeHelper(firstTree.left,secondTree.left) 
           print(firstTree.val)
           if(firstTree.val!=secondTree.val):
             return False
           right_result =self.isSameTreeHelper(firstTree.right,secondTree.right)  
           
           return left_result and right_result

        print("else")   
        return firstTree is None and secondTree is None
        

        