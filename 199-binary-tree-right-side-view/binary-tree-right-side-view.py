# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side = []
        queue = [root]
        if root:
            while queue:
                level_length = len(queue)
                for i in range(level_length):
                    node = queue.pop(0)
                    if i == level_length-1:
                        right_side.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return right_side


        