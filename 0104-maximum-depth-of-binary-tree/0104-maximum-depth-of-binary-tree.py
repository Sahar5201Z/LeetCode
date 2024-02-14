#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count=0
        maxDep=0
        maxresult=self.maxDepthTreeHelper(root,count,maxDep)
        return maxresult
     


    def maxDepthTreeHelper(self,tree,count,maxDep)->int:
        if tree:
           count+=1

           if(count>maxDep):
               maxDep=count
           left_result=self.maxDepthTreeHelper(tree.left,count,maxDep) 
           right_result =self.maxDepthTreeHelper(tree.right,count,maxDep) 

           count-=1 
           
           return max(left_result, right_result) 
        else: 
            return maxDep


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)
        