# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_list = []  # Each element: (col, row, val)
        queue = deque([(root, 0, 0)])  # node, row, col

        while queue:
            node, row, col = queue.popleft()
            if node:
                node_list.append((col, row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        # Step 2: Sort by col, row, value
        node_list.sort()
        
        # Step 3: Group by col
        res = []
        prev_col = float('-inf')
        for col, row, value in node_list:
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(value)
        return res