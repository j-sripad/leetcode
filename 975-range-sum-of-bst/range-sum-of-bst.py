# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = [0]
        def dfs(root):
            if root is None:
                return 
            if root.val >= low and root.val <= high:
                range_sum[0] += root.val
            dfs(root.right)
            dfs(root.left)  

            
        dfs(root)
        return range_sum[0]
            

             

            
            
        