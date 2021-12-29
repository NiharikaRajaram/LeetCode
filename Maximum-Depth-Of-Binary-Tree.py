# recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        return max(l, r) + 1
      
# iterative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = []
        
        if root != None:
            s.append((1, root))
            
        level = 0
        
        while s!= []:
            c_level, root = s.pop()
            if root != None:
                level = max(level, c_level)
                s.append((c_level+1, root.left))
                s.append((c_level+1, root.right))
                
        return level
            
