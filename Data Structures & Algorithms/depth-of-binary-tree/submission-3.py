# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0   
        return self.dfs(root, 0)

    def dfs(self, root, depth):

        if root is None: return 0  


        return 1 +  max(self.dfs(root.right, depth), self.dfs(root.left, depth))
        